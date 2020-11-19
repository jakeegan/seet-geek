import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Test case R1.1 - If the user hasn't logged in, show the login page
test_user = User(
    email='testing@test.com',
    name='Test',
    password=generate_password_hash('Testing!')
)

class TestCase8_1(BaseCase):
    # Test Case R1.1.1 - If the user navigates to /
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase8_1_1(self, *_):
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.open(base_url + '/randomNonExistentPage')
        self.assert_element('#message')
        self.assert_title('Error 404')

    def testcase8_1_2(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/randomNonExistentPage')
        self.assert_element('#message')
        self.assert_title('Error 404')