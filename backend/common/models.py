from two_factor.models import PhoneDevice
from django_otp.oath import totp
from binascii import unhexlify
from django.db import models
from django_otp.models import Device
from django_otp.util import hex_validator, random_hex
import tasks


def get_default_key():
    return random_hex(20)


def verify_generated_token(cls, token):
    """
        Verified generated tokens
    """
    # local import to avoid circular import
    from two_factor.utils import totp_digits
    try:
        token = int(token)
    except ValueError:
        return False

    for drift in range(-100, 100):  # bigger range for emails
        if totp(cls.bin_key, drift=drift, digits=totp_digits()) == token:
            return True
    return False


def generate_challenge_token(cls):
    """
        Generates a token challenge delivered to a user
        either via email or phone which is then verified.
    """
    # local import to avoid circular import
    from two_factor.utils import totp_digits
    no_digits = totp_digits()
    token = str(totp(cls.bin_key, digits=no_digits)).zfill(no_digits)
    return token


class TwoFactorPhoneDevice(PhoneDevice):
    """
        Override phone device
    """
    def generate_challenge(self):
        """
            Sends the current TOTP token to `self.number`
        """
        token = generate_challenge_token(self)
        tasks.send_sms_task(self, token)

        """
            Added this to also send token via email, Twilio test
            account doesn't deliver messages to the phone.
        """
        tasks.send_token_via_email_task(self.user, token)

    def verify_token(self, token):
        return verify_generated_token(self, token)

    class Meta:
        app_label = 'common'


class TwoFactorEmailDevice(Device):
    """
    A :class:`~django_otp.models.Device` that delivers a token to the user's
    registered email address (``user.email``). This is intended for
    demonstration purposes; if you allow users to reset their passwords via
    email, then this provides no security benefits.

    .. attribute:: key

        *CharField*: A hex-encoded secret key of up to 40 bytes. (Default: 20
        random bytes)
    """
    key = models.CharField(
        max_length=80,
        default=get_default_key,
        validators=[hex_validator],
        help_text='A hex-encoded secret key of up to 20 bytes.')

    @property
    def bin_key(self):
        return unhexlify(self.key.encode())

    def generate_challenge(self):
        token = generate_challenge_token(self)
        tasks.send_email_task(self.user, token)
        message = "sent by email"
        return message

    def verify_token(self, token):
        return verify_generated_token(self, token)
