from celery import shared_task
from .models import User
from django.conf import settings
from django.core.mail import send_mail

@shared_task(bind= True)
def dj_send_mail(self):
    subject = "Remainder for submitting The Timesheet"
    email_from = settings.EMAIL_HOST_USER
    data = User.objects.filter(submitted = 0)
    for user in data:
        name = user.user
        to_mail = [user.email]
        message = f'Hi {name} Hope you Finding this email, This is a remainder mail, Just to remaind that you havent submitted the Timesheet for thsi Week So please submit before leaving today'
        send_mail(subject, message, email_from, to_mail, fail_silently = True)
    return "Mail sent"





    

