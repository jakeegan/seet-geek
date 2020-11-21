import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend homepage.

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.backend.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Test_frontend!')
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100'}
]

#Test case R2.1 - If the user has logged in, redirect back to the user profile page /
class TestCase2_1(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase2_1_0(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend!")
        self.click('input[type="submit"]')
        self.open(base_url + '/register')
        self.assert_element("#welcome-header")

#Test case R2.2 - Otherwise, show the user registration page
class TestCase2_2(BaseCase):
    def testcase2_2_0(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.assert_element("#register-header")

#Test case R2.3 - The registration page shows a registration form requesting: email, user name, password, password2
class TestCase2_3(BaseCase):
    def testcase2_3_0(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.assert_element('#email')
        self.assert_element('#name')
        self.assert_element('#password')
        self.assert_element('#password2')
#Test case R2.4 - The registration form can be submitted as a POST request to the current URL (/register)
class TestCase2_4(BaseCase):
    def testcase2_4_0(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.assert_element('form[method="post"]')
        self.assert_element('#btn-submit[value="Register"]')

#Test case R2.5 - Email, password, password2, all have to satisfy the same required as defined in R1
class TestCase2_5(BaseCase):
    #Test case R2.5.1 - Password is less shorter than 6 characters
    def testcase2_5_1(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "simple@example.com")
        self.type("#name", "user")
        self.type("#password", "Test@")
        self.type("#password2", "Test@")
        self.click('input[type="submit"]')
        self.assert_element("#register-header")
        self.assert_text("Password must be 6 or more characters", "#message")

    #Test case R2.5.2 - Password has no special character
    def testcase2_5_2(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "simple@example.com")
        self.type("#name", "user")
        self.type("#password", "Testpassword")
        self.type("#password2", "Testpassword")
        self.click('input[type="submit"]')
        self.assert_element("#register-header")
        self.assert_text("Password must contain at least one special character", "#message")    

    #Test case R2.5.3 - Password has no lower case character
    def testcase2_5_3(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "simple@example.com")
        self.type("#name", "user")
        self.type("#password", "TESTPASSWORD@")
        self.type("#password2", "TESTPASSWORD@")
        self.click('input[type="submit"]')
        self.assert_element("#register-header")
        self.assert_text("Password must contain at least one lower case character", "#message")    

    #Test case R2.5.4 - Password has no upper case character
    def testcase2_5_4(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "simple@example.com")
        self.type("#name", "user")
        self.type("#password", "testpassword@")
        self.type("#password2", "testpassword@")
        self.click('input[type="submit"]')
        self.assert_element("#register-header")
        self.assert_text("Password must contain at least one upper case character", "#message")  

    #Test case R2.5.5 - Email address does not meet RFC 5322 spec
    def testcase2_5_5(self): 
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "abc.example.com")
        self.type("#name", "user")
        self.type("#password", "Testpassword!")
        self.type("#password2", "Testpassword!")
        self.click('input[type="submit"]')
        self.assert_element("#register-header")
        self.assert_text("Email format is invalid", "#message") 

#Test case R2.6 - Password and password2 have to be exactly the same
class TestCase2_6(BaseCase):
    def testcase2_6_0(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "simple@example.com")
        self.type("#name", "user")
        self.type("#password", "Test_frontend!")
        self.type("#password2", "x")
        self.click('input[type="submit"]')
        self.assert_element('#register-header')
        self.assert_text("Passwords must match", "#message")

#Test case R2.7 - Username has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or last character.  
class TestCase2_7(BaseCase):
    # R2.7.1 handled by template blank input checking
    # def testcase2_7_1(self):
    #     self.open(base_url + '/logout')
    #     self.open(base_url + '/register')
    #     self.type("#email", "simple@example.com")
    #     self.type("#name", "")
    #     self.type("#password", "Test_frontend!")
    #     self.type("#password2", "Test_frontend!")
    #     self.click('input[type="submit"]')
    #     self.assert_element('#register-header')
    #     self.assert_text("Username cannot be blank", "#message")

    #Test case R2.7.2 - Username has symbols
    def testcase2_7_2(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "simple@example.com")
        self.type("#name", "user@")
        self.type("#password", "Test_frontend!")
        self.type("#password2", "Test_frontend!")
        self.click('input[type="submit"]')
        self.assert_element('#register-header')
        self.assert_text("Username must be alphanumeric", "#message")

    #Test case R2.7.3 - Username has spaces as first or last character
    def testcase2_7_3(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "simple@example.com")
        self.type("#name", "user ")
        self.type("#password", "Test_frontend!")
        self.type("#password2", "Test_frontend!")
        self.click('input[type="submit"]')
        self.assert_element('#register-header')
        self.assert_text("Username cannot contain trailing spaces", "#message")
        self.type("#email", "simple@example.com")
        self.type("#name", " user")
        self.type("#password", "Test_frontend!")
        self.type("#password2", "Test_frontend!")
        self.click('input[type="submit"]')
        self.assert_element('#register-header')
        self.assert_text("Username cannot contain leading spaces", "#message")

#Test case R2.8 - Username has to be longer than 2 characters and less than 20 characters.
class TestCase2_8(BaseCase):
    #Test case R2.8.1 - Username is less than 2 characters
    def testcase2_8_1(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "simple@example.com")
        self.type("#name", "x")
        self.type("#password", "Test_frontend!")
        self.type("#password2", "Test_frontend!")
        self.click('input[type="submit"]')
        self.assert_element('#register-header')
        self.assert_text("Username must be longer than 2 characters", "#message")
    
    #Test case R2.8.2 - Username is more than 20 characters
    def testcase2_8_2(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "simple@example.com")
        self.type("#name", "xxxxxxxxxxxxxxxxxxxxxxxxx")
        self.type("#password", "Test_frontend!")
        self.type("#password2", "Test_frontend!")
        self.click('input[type="submit"]')
        self.assert_element('#register-header')
        self.assert_text("Username must be less than 20 characters.", "#message")

#Test case R2.9 - If the email already exists, show message 'this email has been ALREADY used'
class TestCase2_9(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase2_9_0(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "user")
        self.type("#password", "TestingPassword!")
        self.type("#password2", "TestingPassword!")
        self.click('input[type="submit"]')
        self.assert_element('#register-header')
        self.assert_text("This email has already been used", "#message")

#Test case R2.10 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
class TestCase2_10(BaseCase):
    def testcase2_10_0(self):
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        self.type("#email", "simple@example.com")
        self.type("#name", "user")
        self.type("#password", "Test_frontend!")
        self.type("#password2", "Test_frontend!")
        self.click('input[type="submit"]')
        if(self.get_text("#message") == "This email has already been used" 
           or self.get_current_url() == base_url + '/login'): 
            self.open(base_url + '/login')
            self.type("#email", "simple@example.com")
            self.type("#password", "Test_frontend!")
            self.click('input[type="submit"]')           
        self.assert_element("#welcome-header")
        self.assert_text("Available balance: $5000", "#balance")

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
