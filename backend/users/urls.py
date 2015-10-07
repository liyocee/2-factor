from django.conf.urls import patterns, url

from .views import (
    UserListView, UserDetailView, UsersCreateView,
    VerifyEmailView, SmsTokenView
)

urlpatterns = patterns(
    '',
    url(r'^create/$', UsersCreateView.as_view(), name="create"),
    url(r'^verify_email/$', VerifyEmailView.as_view(), name="verify_email"),
    url(r'^sms_token/$', SmsTokenView.as_view(), name="sms_token"),
    url(r'^$', UserListView.as_view(), name="users"),
    url(r'^(?P<pk>[^/]+)/$', UserDetailView.as_view(), name="user_detail"),
)
