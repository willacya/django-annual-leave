from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Staff(models.Model):
    PROFESSION = (
        ('PT','Physiotherapist'),
        ('OT','Occupational Therapist'),
        ('TTL','Therapy Team Lead'),
    )
    band = models.CharField(max_length=2)
    prof = models.CharField(max_length=50, choices=PROFESSION)
    allowance = models.FloatField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Leave(models.Model):
    leaveDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.staff} {self.leaveDate} {self.startTime}-{self.endTime}'