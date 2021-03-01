from django.contrib import admin
from .models import User, Staff, Leave, UserProfile

# Register your models here.
admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Leave)
admin.site.register(UserProfile)