import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

test_user = User(
    email='testing@test.com',
    name='Test',
    password=generate_password_hash('Testing!')
)

# Test case R7.1 - Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.
class TestCase7_1(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase7_1_1(self, *_):
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.open(base_url + '/logout')
        self.assert_text("please login","#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase7_1_2(self, *_):
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.open(base_url + '/logout')
        self.open(base_url + '/update')
        self.assert_text("You cannot access /update while being logged out","#flash")

    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase7_1_3(self, *_):
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.open(base_url + '/logout')
        self.open(base_url + '/sell')
        self.assert_text("You cannot access /sell while being logged out","#flash")

    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase7_1_4(self, *_):
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.open(base_url + '/logout')
        self.open(base_url + '/buy')
        self.assert_text("You cannot access /buy while being logged out","#flash")