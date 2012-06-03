from tastypie.resources import ModelResource, Resource
from tastypie.utils.urls import trailing_slash
from django.conf.urls.defaults import url
from tastypie import fields
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from singly.singly_client import SinglyApiHelper, SinglyApi
from singly.models import Photo
from tastypie.serializers import Serializer
import random

class PhotoResource(Resource):
    
    description = fields.CharField()
    name = fields.CharField()
    service = fields.CharField()
    thumbnail_url = fields.CharField()
    url = fields.CharField()
    
    class Meta():
        resource_name = 'photo'
        serializer = Serializer(formats=['json'])
        singly_api_method = SinglyApi.get_user_photos
        
    def make_singly_request(self, django_request):
        access_token = django_request.user.profile.all()[0].access_token
        singly_client = SinglyApi(access_token = access_token)
        response = self.Meta.singly_api_method(singly_client)
        return response
        
    def obj_get_list(self, request=None, **kwargs):
        photos = self.make_singly_request(request)
        return [ photo['oembed'] for photo in photos]
                
    def dehydrate_name(self, bundle):
        return bundle.obj.get('title') or bundle.obj.get('author_name', '')
        
    def dehydrate_description(self, bundle):
        return bundle.obj.get('description', '')
        
    def dehydrate_service(self, bundle):
        return bundle.obj.get('provider_name', '').lower()
        
    def dehydrate_thumbnail_url(self, bundle):
        return bundle.obj.get('thumbnail_url') or bundle.obj['url']
        
    def dehydrate_url(self, bundle):
        return bundle.obj['url']
        
class PhotoFeedResource(PhotoResource):
    class Meta(PhotoResource.Meta):
        resource_name = 'photo_feed'
        singly_api_method = SinglyApi.get_photos_feed
    