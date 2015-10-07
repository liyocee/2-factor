from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.test import APIClient


class LoginMixin(object):

    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            email='tester@2factor.co.ke',
            first_name='Test',
            last_name='Test',
            password='tester'
        )
        self.user.is_email_verified = True
        self.user.is_phone_verified = True
        self.user.save()
        login_url = settings.LOGIN_URL
        login_data = {
            'username': 'tester@2factor.co.ke', 'password': 'tester'
        }
        response = self.client.post(login_url, login_data)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(response.data['key']))
        self.maxDiff = None
        super(LoginMixin, self).setUp()
