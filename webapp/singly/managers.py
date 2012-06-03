from django.db import models
from singly.singly_client import SinglyApi, SinglyApiHelper
from django.contrib.auth.models import User
from pprint import pprint
from django.core.exceptions import ObjectDoesNotExist

class SinglyCodeManager(models.Manager):
    
    def get_access_token(self, code):
        try:
            singly_code = self.get(code=code)
            return singly_code.access_token
        except ObjectDoesNotExist:
            access_token = SinglyApiHelper.get_access_token(code)
            self.model(code = code, access_token = access_token).save()
            return access_token
            
class UserProfileManager(models.Manager):   
         
    def get_or_create_user(self, singly_id, singly_access_token):
        try:
            created = False
            user_profile = self.get(singly_id = singly_id)
        except ObjectDoesNotExist:
            created = True
            profiles = SinglyApi(access_token=singly_access_token).get_user_profiles()
            for service in profiles:
                if service != 'id':
                    service_profile = SinglyApi(access_token=singly_access_token).get_profile_by_service(service)
                    try:
                        username = service_profile['types']['contact']
                    except KeyError:
                        try:
                            username = service_profile['data']['name']
                        except KeyError:
                            username = service_profile['data']['username']
            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist:
                user = User.objects.create_user(username, username +'@gmail.com', 'password')
#            user, user_created = User.objects.get_or_create(username=username)
            user_profile = self.model(
                    access_token = singly_access_token,
                    singly_id = singly_id,
                    user=user
                )
            user_profile.save()
        return user_profile, created