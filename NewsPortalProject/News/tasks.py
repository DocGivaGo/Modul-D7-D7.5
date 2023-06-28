from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@shared_task
def send_notification(preview, pk, title,
                      subscribers):  # отдельно делаем функцию отправки сообщения о новом посте для подписчика
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/post/{pk}'  # http://127.0.0.1:8000/post/pk
        }
    )
    msg = EmailMultiAlternatives(subject=title, body='', from_email=settings.DEFAULT_FROM_EMAIL, to=subscribers)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
