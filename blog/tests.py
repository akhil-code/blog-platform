from django.test import TestCase
from .models import Author, Blog, Tag, Comment
from django.contrib.auth.models import User
from selenium import webdriver

# Create your tests here.
class ModelsTestCase(TestCase):
    
    def setUp(self):
        # test user details
        self.user_info = {
            'username' : 'nikhilguttula',
            'email' : 'guttulanikhil@gmail.com',
            'password' : 'password',
            'first_name' : 'nikhil',
        }

        # creating user
        user = User.objects.create_user(
            username = self.user_info['username'],
            email = self.user_info['email'],
            password = self.user_info['password'],
            first_name = self.user_info['first_name'],
        )
        user.save()
        Author(user=user).save()