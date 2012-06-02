from django.contrib.auth.models import User
from django.db import models
from singly.managers import UserProfileManager, SinglyCodeManager

class SinglyCode(models.Model):
    access_token = models.CharField(max_length=260)
    code = models.CharField(max_length=32)
    
    objects = SinglyCodeManager()
    
    class Meta:
        db_table = 'singly_code'
        
class UserProfile(models.Model):
    access_token = models.CharField(max_length=260, null=True, blank=True)
    user = models.ForeignKey(User, related_name='profile')
    
    objects = UserProfileManager()
    
    class Meta:
        db_table = 'user_profile'