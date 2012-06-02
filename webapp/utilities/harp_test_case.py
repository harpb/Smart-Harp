from django.test import TestCase
from mock import Mock, patch
from django import http
from django.contrib.auth.models import User
from types import DictType, ListType
from django.utils import simplejson
from webapp import settings

class HarpTestCase(TestCase):
    fixtures = [
        'attendee_convention.json',
        'attendee_event.json',
    ]
    RESOURCES_PATH = '%s/static/tests_resources' % settings.PROJECT_ROOT
    
    @patch.object(http, 'HttpRequest')
    def request_mock(self, 
                     request, 
                     request_method='GET', 
                     payload={}, 
                     login=False):
        """
        Not sure whether to mock everything about the request object or to create an instance
        so I created this function if I want to switch between the two ideas.
        """
        request = http.HttpRequest()
        request.method = request_method
        request.META = {
                        'HTTP_HOST': self.HTTP_HOST,
                        'HTTP_USER_AGENT': self.HTTP_USER_AGENT,
                        }
        request.session = {'uid': self.user_id}
        
        if request_method == 'POST':
            request.POST = payload
        else:
            request.GET = payload
        
        if not login:
            request.user.is_authenticated.return_value = login
            request.user.is_anonymous = True
        else:
            request.user.is_anonymous = False
            request.user.email = self.user_email
            
        return request
    
    def get(self, payload={}, login=False):
        request = self.request_mock(request_method = 'GET', 
                                    payload=payload,
                                    login=login)
        return request
    
    def post(self, 
             payload={},
             login=False):
        request = self.request_mock(request_method = 'POST', 
                                    payload=payload,
                                    login=login)
        return request
    
    def put(self, payload={}, login=False):
        request = self.request_mock(request_method = 'PUT', 
                                    payload=payload,
                                    login=login)
        return request
    
    def delete(self, 
             payload={},
             login=False):
        request = self.request_mock(request_method = 'DELETE', 
                                    payload=payload,
                                    login=login)
        return request

    def mock(self, parent, obj_class):
        mock = Mock(spec=obj_class)
        parent.return_value = mock
        return mock
    
        
    def patch(self, *args):
        if len(args) == 2:
            patcher = patch.object(args[0], args[1])
        else:
            patcher = patch(args[0])
        instance = patcher.start()
        self.addCleanup(patcher.stop)
        return instance
    
    def assertCalled(self, instance):
        self.assertTrue(instance.called)
        
    def assertCalledOnce(self, instance):
        self.assertEqual(instance.call_count, 1)
    
    def assertIsOne(self, instance):
        self.assertEqual(instance, 1)
    
    def assertAsExpected(self):
        self.assertEqual(self.expected, self.actual)

    def assertEmpty(self, instance):
        self.assertEqual(len(instance), 0)
        
    def assertNone(self, instance):
        self.assertEqual(instance, None)
     
    def assertEqualDict(self, actual, expected):
        for key in expected:            
            if isinstance(expected[key], DictType):
                self.assertEqualDict(self, actual[key], expected[key])
            else:
                self.assertEqual(actual[key], expected[key])
        
        self.assertEqual(len(actual), len(expected) )

    def print_json(self, output = None):
        if not output:
            output = self.output
        if not (isinstance(output, DictType) or isinstance(output, ListType)):
            output = simplejson.loads(output)
        
        print simplejson.dumps(output, sort_keys=True, indent=4)
        return output


    def json_to_dict(self, content = None):
        return simplejson.loads(content)
