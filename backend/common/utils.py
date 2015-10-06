from django.core.mail import EmailMessage
from django.conf import settings
import time
from django.contrib.auth import get_user_model


class SendEmail(object):
    """
        Base Class for sending emails
    """

    def __init__(self, subject, to, message, template=None):
        self.subject = subject
        self.to = to
        self.template = template
        self.msg = self._setup_message()

    def send(self):
        self.msg.send()

    def _setup_message(self):
        msg = EmailMessage(
            subject=self.subject,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=self.to)
        if self.template:
            msg.template_name = self.template["name"]
            msg.global_merge_vars = self.template["global_merge_vars"]
            msg.merge_vars = self.template.get("merge_vars", {})
            msg.merge_language = self.template.get(
                "merge_language", "mailchimp")

        return msg


class UserRegistrationEmail(SendEmail):
    """
        Specialized Class for sending User Registraion Email
    """

    def __init__(self, to, token, user_id):
        subject = "Welcome to 2-Factor App,  [{}]".format(
            time.strftime("%d,%b %Y %H:%M"))
        msg = subject
        user = get_user_model().objects.get(pk=user_id)

        template = {
            "name": "two-factor",
            "global_merge_vars": {
                "EMAIL_VERIFY_LINK": "{}/{}/{}".format(
                    settings.EMAIL_VERIFY_UI_LINK, token, str(user_id)),
                "FNAME": user.first_name,
                "MESSAGE": msg
            }
        }
        super(UserRegistrationEmail, self).__init__(
            subject, [to], msg, template)
