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

# Test Case R8.1 - For any other requests except the ones above, the system should return a 404 error
class TestCase8_1(BaseCase):
    
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