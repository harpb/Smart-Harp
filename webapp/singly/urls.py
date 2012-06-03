from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
urlpatterns = patterns('singly.views',
    url(r'^authenticate/(?P<service>[a-z]+)/$', 
            'authenticate_redirect', 
            name='authenticate_redirect'
        ),
    url(r'^authorize/callback/$', 
            'authorize_callback', 
            name='authorize_callback'
        ),
    url(r'^logout/$', 
            'logout', 
            name='logout'
        ),
    url(r'^$', 'index', name='index'),
)
