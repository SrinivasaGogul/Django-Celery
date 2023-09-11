from django.shortcuts import render

# Create your views here.
from .tasks import dj_send_mail
from django.http import HttpResponse

def mail(request):
    dj_send_mail.delay()
    return HttpResponse("Mail Sent")

