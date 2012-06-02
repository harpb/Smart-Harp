from django.conf.urls.defaults import *
from tastypie.api import Api
from resources import PhotoResource
from singly.v1.resources import PhotoFeedResource

api = Api(api_name='v1')
api.register(PhotoResource(), canonical=True)
api.register(PhotoFeedResource(), canonical=True)

urlpatterns = api.urls