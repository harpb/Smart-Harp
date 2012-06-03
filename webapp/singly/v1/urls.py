from django.conf.urls.defaults import *
from tastypie.api import Api
from resources import PhotoResource, PhotoFeedResource,\
    VideoResource, VideoFeedResource
from singly.v1.resources import FacebookResource, InstagramResource,\
    TumblrResource, TwitterResource

api = Api(api_name='v1')
api.register(PhotoResource(), canonical=True)
api.register(PhotoFeedResource(), canonical=True)
api.register(VideoResource(), canonical=True)
api.register(VideoFeedResource(), canonical=True)

api.register(FacebookResource(), canonical=True)
api.register(InstagramResource(), canonical=True)
api.register(TumblrResource(), canonical=True)
api.register(TwitterResource(), canonical=True)


urlpatterns = api.urls