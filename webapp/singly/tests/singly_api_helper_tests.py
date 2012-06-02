from utilities.harp_test_case import HarpTestCase
from singly.singly_client import SinglyApiHelper, SinglyApi
from pprint import pprint
#===============================================================================
# https://dev.singly.com/api
#===============================================================================
class TestSinglyApiHelper(HarpTestCase):
    
    def setUp(self):
        self.access_token = 'R5tUA184W3NHCeHGFnKJmCzN13k=6iddoAr651c768406c01ca44fc78bd88aec0b14694c0a0712ee50e76f089164e311d5435ccbcf7d68882599da7080af996acf7ebf9bd4393fd820284f56764873a01b4c8562be329d8ec2e8bdd02e1a393a8b50bb851c3269348b977ba5ce798882a064d4c997caf63151747abeaa2aa7cdfc887'
        
    #===========================================================================
    # get_authorize_url
    #===========================================================================
    def test_get_authorize_url(self):
        service = 'twitter'
        expected = 'https://api.singly.com/oauth/authorize?client_id=0d1f05ad869020e160bafa96596543b7&redirect_uri=http://localhost:6230/auth/singly/callback/&service=twitter'
        # CALL
        actual = SinglyApiHelper.get_authorize_url(service)
        # ASSERT
        self.assertEqual(expected, actual)
        
    #===========================================================================
    # get_access_token
    #===========================================================================
    def t3st_get_access_token(self):
        code = 'dhbpPiUqniGh_ODXaihbKY'
        # CALL
        print SinglyApiHelper.get_access_token(code)
        
    #===========================================================================
    # get_user_profiles
    #===========================================================================
    def t3st_get_user_profiles(self):
        # CALL
        print SinglyApiHelper.get_profiles(self.access_token)
        
    #===========================================================================
    # get_profile_by_service
    #===========================================================================
    def test_get_profile_by_service(self):
        service = 'twitter'
        # CALL
        actual = SinglyApi(access_token = self.access_token)\
                .get_profile_by_service(service)
        pprint(actual, indent=4)
        
    #===========================================================================
    # get_user_photos
    #===========================================================================
    def t3st_get_user_photos(self):
        # CALL
        actual = SinglyApiHelper.get_user_photos(self.access_token)
#        pprint(actual[0], indent=4)
        
    #===========================================================================
    # get_photos_feed
    #===========================================================================
    def t3st_get_photos_feed(self):
        # CALL
        actual = SinglyApiHelper.get_photos_feed(self.access_token)
        pprint(actual[0], indent=4)
        
    #===========================================================================
    # get_user_videos
    #===========================================================================
    def t3st_get_user_videos(self):
        # CALL
        actual = SinglyApiHelper.get_user_videos(self.access_token)
#        pprint(actual[0], indent=4)
        
    #===========================================================================
    # get_videos_feed
    #===========================================================================
    def t3st_get_videos_feed(self):
        # CALL
        actual = SinglyApiHelper.get_videos_feed(self.access_token)
        for video in actual:
            print video['oembed']