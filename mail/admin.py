from django.contrib import admin

# Register your models here.
from mail.models import User

class Userreg(admin.ModelAdmin):
    list_display = ['user', 'email', 'submitted']

    def __str__(self) -> str:
        return self.user

admin.site.register(User, Userreg)