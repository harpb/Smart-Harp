from django.test.testcases import TestCase
from singly.models import UserProfile

class TestUserProfileManager(TestCase):
    
    def setUp(self):
        pass
        
    def test_get_or_create_user(self):
        self.access_token = 'R5tUA184W3NHCeHGFnKJmCzN13k=6iddoAr651c768406c01ca44fc78bd88aec0b14694c0a0712ee50e76f089164e311d5435ccbcf7d68882599da7080af996acf7ebf9bd4393fd820284f56764873a01b4c8562be329d8ec2e8bdd02e1a393a8b50bb851c3269348b977ba5ce798882a064d4c997caf63151747abeaa2aa7cdfc887'
        # CALL
        user_profile, created = UserProfile.objects.get_or_create_user(self.access_token)
        # ASSERT
        self.assertEqual(1, user_profile.user.id)
        self.assertEqual(self.access_token, user_profile.access_token)
        self.assertEqual('_HarpB', user_profile.user.username)