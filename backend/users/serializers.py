from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_auth.serializers import (
    TokenSerializer,
    PasswordResetSerializer
)
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.conf import settings
from models import User
from common.models import (
    TwoFactorPhoneDevice, TwoFactorEmailDevice)


class UserSerializer(serializers.ModelSerializer):

    short_name = serializers.ReadOnlyField(source='get_short_name')
    full_name = serializers.ReadOnlyField(source='get_full_name')

    class Meta(object):
        model = User
        extra_kwargs = {'password': {'write_only': True}}


class UserAuthTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Token
        fields = ('key', 'user')


class UserPasswordResetSerializer(PasswordResetSerializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        # Check if user exists
        try:
            get_user_model().objects.get(email=value)
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError(
                {'user': ["{} does not exist".format(value)]})

    def save(self):
        email = self.initial_data['email']
        get_user_model().objects.get(email=email)
        """
            send password reset email/sms
        """


def verify_token(user_id, token, device):
    try:
        user = User.objects.get(id=user_id)
        dev = device.objects.get(user=user)
        try:
            dev.verify_token(token)
            user.is_email_verified = True
            user.save()
        except Exception:
            raise ValidationError({'user': 'Invalid Token'})
    except User.DoesNotExist:
        raise ValidationError({'user': 'User does not exist'})

    return user


class VerifyEmailSerializer(serializers.Serializer):
    user = serializers.CharField()
    token = serializers.CharField(max_length=settings.TWO_FACTOR_TOTP_DIGITS)

    def create(self, validated_data):
        user = verify_token(
            validated_data['user'],
            validated_data['token'],
            TwoFactorEmailDevice
        )
        return {'id': str(user.id)}


class SmsTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=settings.TWO_FACTOR_TOTP_DIGITS)
    user = serializers.CharField()

    def create(self, validated_data):
        user = verify_token(
            validated_data['user'],
            validated_data['token'],
            TwoFactorPhoneDevice
        )
        user_token = Token.objects.get(user=user)
        return UserAuthTokenSerializer(user_token).data
