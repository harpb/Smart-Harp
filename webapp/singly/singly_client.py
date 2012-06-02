from oauth_hook import OAuthHook
import requests
import simplejson
from webapp import settings
from webapp.settings import SINGLY_CLIENT_ID, SINGLY_CLIENT_SECRET 

class SinglyApiError(Exception):
    pass
    
class SinglyApi(object):
    
    hostname = 'https://api.singly.com'
    api_version = 0
    
    def __init__(self, client_id=None, client_secret=None, access_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        
    def make_client_request(self, endpoint, method='GET', payload={}):
        # create consumer and token
        url = self.hostname + endpoint
        
        if method == 'GET':
            if self.access_token is not None:
                payload['access_token'] = self.access_token
            response = requests.get(url, params=payload)
        else:
            response = requests.post(url, payload)
        
        if response.status_code < 300:
            return response.status_code, simplejson.loads(response.content)
        else:
            raise SinglyApiError("%s: %s" % (response.status_code, response.content))
        
    def authorize(self, code):
        endpoint = '/oauth/access_token'
        payload = {
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'code': code
            }
        status_code, content = self.make_client_request(endpoint, 'POST', payload)
        return content['access_token']
        
    def get_profile_by_service(self, service, include_tokens = True):
        endpoint = '/v%s/profiles/%s' % (self.api_version, service)
        if include_tokens:
            payload = {'auth': 'true'}
        else:
            payload = {}
        status_code, content = self.make_client_request(endpoint, payload=payload)
        return content
        
    def get_user_profiles(self, include_tokens = True):
        endpoint = '/v%s/profiles' % self.api_version
        if include_tokens:
            payload = {'auth': 'true'}
        else:
            payload = {}
        status_code, content = self.make_client_request(endpoint, payload=payload)
        return content
        
    def get_user_photos(self):
        return self.get_content_by_type('photos')
        
    def get_photos_feed(self):
        return self.get_content_by_type('photos_feed')
        
    def get_content_by_type(self, type):
        endpoint = '/v%s/types/%s/' % (self.api_version, type)
        status_code, content = self.make_client_request(endpoint)
        return content
        
    def get_user_videos(self):
        return self.get_content_by_type('videos')
        
    def get_videos_feed(self):
        return self.get_content_by_type('videos_feed')
        
class SinglyApiHelper(object):
    redirect_url = '%s/authorize/callback/' % settings.HOSTNAME
    
    @classmethod
    def get_authorize_url(cls, service, redirect_url=None):
        if redirect_url is None:
            redirect_url = cls.redirect_url
            
        url = '%s/oauth/authorize?client_id=%s&redirect_uri=%s&service=%s' % (
                SinglyApi.hostname, SINGLY_CLIENT_ID, redirect_url, service
            ) 
        return url
        
    @classmethod
    def get_access_token(cls, code):
        api_handle = SinglyApi(SINGLY_CLIENT_ID, SINGLY_CLIENT_SECRET)
        access_token = api_handle.authorize(code)
        return access_token
        
    @classmethod
    def get_profiles(cls, access_token):
        api_handle = SinglyApi(access_token=access_token)
        profiles = api_handle.get_user_profiles()
        return profiles
        
    @classmethod
    def get_user_photos(cls, access_token):
        return SinglyApi(access_token=access_token).get_user_photos()
        
    @classmethod
    def get_photos_feed(cls, access_token):
        return SinglyApi(access_token=access_token).get_photos_feed()
        
    @classmethod
    def get_user_videos(cls, access_token):
        return SinglyApi(access_token=access_token).get_user_videos()
        
    @classmethod
    def get_videos_feed(cls, access_token):
        return SinglyApi(access_token=access_token).get_videos_feed()
