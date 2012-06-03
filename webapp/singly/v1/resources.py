from tastypie.resources import ModelResource, Resource
from tastypie.utils.urls import trailing_slash
from django.conf.urls.defaults import url
from tastypie import fields
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from singly.singly_client import SinglyApiHelper, SinglyApi
from singly.models import Photo
from tastypie.serializers import Serializer
import random

class MediaResource(Resource):
    
    description = fields.CharField()
    name = fields.CharField()
    service = fields.CharField()
    thumbnail_url = fields.CharField()
    url = fields.CharField()
    
    class Meta():
        resource_name = 'media'
        serializer = Serializer(formats=['json'])
        
    def make_singly_request(self, django_request):
        access_token = django_request.user.profile.all()[0].access_token
        singly_client = SinglyApi(access_token = access_token)
        response = self.Meta.singly_api_method(singly_client)
        return response
        
    def obj_get_list(self, request=None, **kwargs):
        medias = self.make_singly_request(request)
        return [ media['oembed'] for media in medias]
                
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
        
class PhotoResource(MediaResource):
    class Meta(MediaResource.Meta):
        resource_name = 'photo'
        singly_api_method = SinglyApi.get_user_photos
        
class PhotoFeedResource(MediaResource):
    class Meta(MediaResource.Meta):
        resource_name = 'photo_feed'
        singly_api_method = SinglyApi.get_photos_feed
    
class VideoResource(MediaResource):
    class Meta(MediaResource.Meta):
        resource_name = 'video'
        singly_api_method = SinglyApi.get_user_videos
        
class VideoFeedResource(MediaResource):
    class Meta(MediaResource.Meta):
        resource_name = 'video_feed'
        singly_api_method = SinglyApi.get_videos_feed
        
class ServiceResource(MediaResource):
    def obj_get_list(self, request=None, **kwargs):
        medias = self.make_singly_request(request)
        return [media['data'] for media in medias]
                
class FacebookResource(ServiceResource):
    class Meta(MediaResource.Meta):
        resource_name = 'facebook'
        singly_api_method = SinglyApi.get_facebook_media
        
    def dehydrate_thumbnail_url(self, bundle):
        return bundle.obj.get('picture')
        
    def dehydrate_url(self, bundle):
        return bundle.obj['source']
        
class InstagramResource(ServiceResource):
    class Meta(MediaResource.Meta):
        resource_name = 'instagram'
        singly_api_method = SinglyApi.get_instagram_media
        
    def dehydrate_thumbnail_url(self, bundle):
        return bundle.obj['images']['thumbnail']['url']
        
    def dehydrate_url(self, bundle):
        return bundle.obj['images']['standard_resolution']['url']
        
class TumblrResource(ServiceResource):
    class Meta(MediaResource.Meta):
        resource_name = 'tumblr'
        singly_api_method = SinglyApi.get_tumblr_media
        
class TwitterResource(ServiceResource):
    class Meta(MediaResource.Meta):
        resource_name = 'twitter'
        singly_api_method = SinglyApi.get_twitter_media
    