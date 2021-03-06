from huey.djhuey import db_task
from two_factor.gateways import send_sms
from common.utils import UserRegistrationEmail, UserTokenEmail


@db_task(retries=1, retry_delay=30)
def send_email_task(user, token):
    UserRegistrationEmail(user.email, token, user.id).send()


@db_task(retries=1, retry_delay=30)
def send_sms_task(device, token):
    send_sms(device=device, token=token)


@db_task(retries=1, retry_delay=30)
def send_token_via_email_task(user, token):
    UserTokenEmail(user.email, token, user.id).send()
