from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

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
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Leave(models.Model):
    leaveDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    staff = models.ForeignKey('Staff', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.staff} {self.leaveDate} {self.startTime}-{self.endTime}'

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    print(instance, created)

post_save.connect(post_user_created_signal, sender=User)