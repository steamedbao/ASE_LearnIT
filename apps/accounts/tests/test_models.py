from django.test import TestCase

from ..models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='testuser',
                            first_name='Test', last_name='User')

    def test_profile_get_absolute_url(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.profile.get_absolute_url(),
                          '/profiles/testuser')

    def test_profile_get_string_representation(self):
        user = User.objects.get(id=1)
        self.assertTrue(str(user) == user.username)

    def test_profile_reciever_working(self):
        user = User.objects.get(pk=1)
        self.assertTrue(user.profile)
