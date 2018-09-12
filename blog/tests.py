from django.test import TestCase
from .models import Author, Blog, Tag, Comment, Website
from django.contrib.auth.models import User
from selenium import webdriver

# Create your tests here.
class ModelsTestCase(TestCase):
    
    def setUp(self):
        Website().save()

        username = 'akhilguttula'
        email = 'guttula.akhil@gmail.com'
        password = 'password'
        first_name = 'akhil'

        self.driver = webdriver.Firefox()
        self.localhost = 'http://127.0.0.1:8000'

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
        user.save()

        Author(user=user).save()
        
    
    def test_website_duplication(self):
        try:
            Website.objects.create()
        except AssertionError:
            return
    
    def test_user_signup_page(self):
        driver = self.driver
        url = self.localhost + '/signup'
        
        driver.get(url)
        signup_form = driver.find_element_by_css_selector('form')
        fullname_input = driver.find_element_by_css_selector('form > [name=fullname]')
        username_input = driver.find_element_by_css_selector('form > [name=username]')
        email_input = driver.find_element_by_css_selector('form > [name=email]')
        password_input = driver.find_element_by_css_selector('form > [name=password]')

        signup_form.clear()

        password_input.submit()

        self.driver.close()

        