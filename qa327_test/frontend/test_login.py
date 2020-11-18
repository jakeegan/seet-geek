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

# Test case R1.1 - If the user hasn't logged in, show the login page
class TestCase1_1(BaseCase):
    # Test Case R1.1.1 - If the user navigates to /
    def testcase1_1_1(self):
        self.open(base_url + '/logout')
        self.open(base_url)
        self.assert_element("#message")
    
    # Test Case R1.1.2 - If the user navigates to /sell
    def testcase1_1_2(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/sell')
        self.assert_element("#message")
        
    # Test Case R1.1.3 - If the user navigates to /buy
    def testcase1_1_3(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/buy')
        self.assert_element("#message")
        
    # Test Case R1.1.4 - If the user navigates to /update
    def testcase1_1_4(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/update')
        self.assert_element("#message")
        
# Test case R1.2 - The login page has a message that by default says 'please login'
class TestCase1_2(BaseCase):
    def testcase1_2_0(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_text("please login", "#message")
        
# Test case R1.3 - If the user has logged in, redirect to the user profile page
class TestCase1_3(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase1_3_0(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.open(base_url + '/login')
        self.assert_element("#welcome-header")
        
# Test case R1.4 - The login page provides a login form which requests two fields: email and passwords
class TestCase1_4(BaseCase):
    def testcase1_4_0(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_element("#email")
        self.assert_element("#password")
        
# Test case R1.5 - The login form can be submitted as a POST request to the current URL (/login)
class TestCase1_5(BaseCase):
    def testcase1_5_0(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.assert_element('form[method="post"]')
        self.assert_element("#btn-submit")
        self.assert_element('input[value="Log In"]')
        
# Test case R1.6 - Email and password both cannot be empty
class TestCase1_6(BaseCase):
    # Test case R1.6.1 - Email and password are empty
    def testcase1_6_1(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.click('input[type="submit"]')
        self.assert_element("#message")
        
    # Test case R1.6.2 - Password is empty 
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase1_6_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        
    # Test case R1.6.3 - Email is empty 
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase1_6_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#message")

# Test case R1.7 - Email has to follow addr-spec defined in RFC 5322 
class TestCase1_7(BaseCase):
    # Test case R1.7.1 - Invalid email entered
    def testcase1_7_1(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "Abc.example.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.assert_text("email/password format is incorrect.", "#message")
        
    # Test case R1.7.2 - Valid email entered
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase_1_7_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

# Test case R1.8 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
class TestCase1_8(BaseCase):
    # Test case R1.8.1 - Password doesn't meet requirements: minimum length of 6
    def testcase1_8_1(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Test_")
        self.click('input[type="submit"]')
        self.assert_text("email/password format is incorrect.", "#message")
        
    # Test case R1.8.2 - Password doesn't meet requirements: at least one upper case
    def testcase1_8_2(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "testing!")
        self.click('input[type="submit"]')
        self.assert_text("email/password format is incorrect.", "#message")
        
    # Test case R1.8.3 - Password doesn't meet requirements: at least one lower case
    def testcase1_8_3(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "TESTING!")
        self.click('input[type="submit"]')
        self.assert_text("email/password format is incorrect.", "#message")
        
    # Test case R1.8.4 - Password doesn't meet requirements: at least one special character
    def testcase1_8_4(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing")
        self.click('input[type="submit"]')
        self.assert_text("email/password format is incorrect.", "#message")
        
    # Test case R1.8.5 - Password meets requirements
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase1_8_5(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")

# Test case R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'
class TestCase1_9(BaseCase):
    def testcase1_9(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "4x@")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.assert_text("email/password format is incorrect.", "#message")
        
# Test case R1.10 - If email/password are correct, redirect to /
class TestCase1_10(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase1_10(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        
# Test case R1.11 - Otherwise, redict to /login and show message 'email/password combination incorrect'
class TestCase1_11(BaseCase):
    def testcase1_11(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing258@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.assert_text("email/password combination incorrect", "#message")

#class FrontEndHomePageTest(BaseCase):
#
#    @patch('qa327.backend.get_user', return_value=test_user)
#    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
#    def test_login_success(self, *_):
#        """
#        This is a sample front end unit test to login to home page
#        and verify if the tickets are correctly listed.
#        """
#        # open login page
#        self.open(base_url + '/login')
#        # fill email and password
#        self.type("#email", "test_frontend@test.com")
#        self.type("#password", "test_frontend")
#        # click enter button
#        self.click('input[type="submit"]')
#        
#        # after clicking on the browser (the line above)
#        # the front-end code is activated 
#        # and tries to call get_user function.
#        # The get_user function is supposed to read data from database
#        # and return the value. However, here we only want to test the
#        # front-end, without running the backend logics. 
#        # so we patch the backend to return a specific user instance, 
#        # rather than running that program. (see @ annotations above)
#        
#        
#        # open home page
#        self.open(base_url)
#        # test if the page loads correctly
#        self.assert_element("#welcome-header")
#        self.assert_text("Welcome test_frontend", "#welcome-header")
#        self.assert_element("#tickets div h4")
#        self.assert_text("t1 100", "#tickets div h4")
#
#    @patch('qa327.backend.get_user', return_value=test_user)
#    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
#    def test_login_password_failed(self, *_):
#        """ Login and verify if the tickets are correctly listed."""
#        # open login page
#        self.open(base_url + '/login')
#        # fill wrong email and password
#        self.type("#email", "test_frontend@test.com")
#        self.type("#password", "wrong_password")
#        # click enter button
#        self.click('input[type="submit"]')
#        # make sure it shows proper error message
#        self.assert_element("#message")
#        self.assert_text("login failed", "#message")
