from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField()
    submitted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user
    
class Timesheet(models.Model):
    user = models.ForeignKey(User)
    email = 
user = User.symmetric_difference(Timesheet.objects.all())