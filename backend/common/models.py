from two_factor.models import PhoneDevice
from django_otp.oath import totp
from binascii import unhexlify
from django.db import models
from django_otp.models import Device
from django_otp.util import hex_validator, random_hex
import tasks


def get_default_key():
    return random_hex(20)


class TwoFactorPhoneDevice(PhoneDevice):
    """
        Override phone device
    """
    def generate_challenge(self):
        from two_factor.utils import totp_digits

        """
            Sends the current TOTP token to `self.number`
        """
        no_digits = totp_digits()
        token = str(totp(self.bin_key, digits=no_digits)).zfill(no_digits)
        tasks.send_sms_task(self, token)

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
        token = totp(self.bin_key)
        tasks.send_email_task(self.user, token)
        message = "sent by email"
        return message

    def verify_token(self, token):
        try:
            token = int(token)
        except Exception:
            verified = False
        else:
            verified = any(
                totp(self.bin_key, drift=drift) == token for drift in [0, -1])
        return verified
