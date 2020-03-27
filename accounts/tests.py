from django.test import TestCase, Client
from .models import User
from django.urls import reverse
# Create your tests here.

class AccountsAuthTest(TestCase):
    # this method will be intialize once for all the methods bcoz it is class method

    #or use- https://docs.djangoproject.com/en/3.0/topics/testing/tools/#django.test.Client.login
    def test_login_auth(self):
        c= Client()
        url = reverse('accounts:login_page')
        response = c.post(url,{'username':'krish27@gmail.com','password':'@P1q2w3e4r'})
        print("response.redirect_chain-",response)
        self.assertEqual(response.status_code,200)