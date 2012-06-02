from django.http import HttpResponseRedirect, HttpResponse
from singly.singly_client import SinglyApiHelper, SinglyApi, SinglyApiError
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from singly.models import UserProfile, SinglyCode
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def authenticate_redirect(request, service):
    url = SinglyApiHelper.get_authorize_url(service)
    print url 
    return HttpResponseRedirect(url)
    
def authorize_callback(request):
    code = request.GET.get('code')
    if not request.user.is_authenticated():
        access_token = SinglyCode.objects.get_access_token(code)
        user_profile, created = UserProfile.objects.get_or_create_user(access_token)
        user = authenticate(username=user_profile.user.username, password='password')
        auth_login(request, user)
    return HttpResponseRedirect('/')
        
def index(request, template = 'index.html'):
    if request.user.is_authenticated():
        access_token = request.user.profile.all()[0].access_token
        photos = SinglyApiHelper.get_user_photos(access_token)
        photos_feed = SinglyApiHelper.get_photos_feed(access_token)
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )        
    return response
