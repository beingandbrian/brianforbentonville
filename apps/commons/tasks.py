from django.core.mail import send_mail
from django.core.mail import EmailMessage
from celery.decorators import task
from celery.utils.log import get_task_logger

from time import sleep

logger = get_task_logger(__name__)


@task(name="send_mail_to")
def send_mail_to(subject, message, sender, receivers, cc=None, bcc=None, attachment=None):
    is_task_completed = False
    try:
        sleep(0)
        is_task_completed = True
    except Exception as err:
        error = str(err)
        logger.error(error)
    if is_task_completed:
        mail = EmailMessage(subject, message, sender, receivers)
        if cc:
            mail.cc = cc
        if bcc:
            mail.bcc = bcc
        if attachment:
            mail.attach(attachment.name, attachment.read())
    else:
        mail = EmailMessage(subject, message, sender, receivers)
        if cc:
            mail.cc = cc
        if bcc:
            mail.bcc = bcc
        if attachment:
            mail.attach(attachment.name, attachment.read())
    return 'Mail sent to {}'.format(receivers)
