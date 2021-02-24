from django.core.mail import EmailMultiAlternatives

from task_manager_pro import settings


def send_mail(to_mail):
    subject, from_email, to = 'Created!', settings.EMAIL_HOST_USER, to_mail
    text_content = 'CREATED!'
    html_content = f'{to_mail}-Created'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
