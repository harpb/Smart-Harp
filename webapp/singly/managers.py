from django.db import models
from singly.singly_client import SinglyApi
from django.contrib.auth.models import User
from pprint import pprint
from django.core.exceptions import ObjectDoesNotExist
class UserProfileManager(models.Manager):   
         
    def get_or_create_user(self, singly_access_token):
        try:
            created = False
            user_profile = self.get(access_token = singly_access_token)
        except ObjectDoesNotExist:
            created = True
            profiles = SinglyApi(access_token=singly_access_token).get_user_profiles()
            for service in profiles:
                if service != 'id':
                    service_profile = SinglyApi(access_token=singly_access_token).get_profile_by_service(service)
                    username = service_profile['data']['screen_name']
            user = User.objects.create_user(username, username +'@gmail.com', 'password')
#            user, user_created = User.objects.get_or_create(username=username)
            user_profile = self.model(access_token = singly_access_token, user=user)
            user_profile.save()
        return user_profile, created