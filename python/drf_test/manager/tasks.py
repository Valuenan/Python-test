from django.core.mail import send_mail

from drf_test.celery import app

from .models import User


def send(user_data):
    send_mail(
        'Ваша статистика',
        f'{user_data["username"]} ваш баланс {user_data["balance"]}',
        'django.drf@mail.ru',
        [user_data['email']],
        fail_silently=False,
    )


@app.task
def send_user_statistic():
    users_data = User.objects.values('username', 'balance', 'email')
    for data in users_data:
        send(data)
