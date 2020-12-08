import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

test_user = User(
    email='testing@test.com',
    name='Test',
    balance=5000,
    password=generate_password_hash('Testing!')
)

test_user_low_balance = User(
    email='testing2@test.com',
    name='Test',
    balance=4,
    password=generate_password_hash('Testing!')
)

test_ticket = Ticket(
    name='test ticket',
    quantity='10',
    price='10',
    expiration_date=20201201
)

# Test Case R6.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
class TestCase6_1(BaseCase):   
    # Test Case R6.1.1 - The name of the ticket is alphanumeric-only
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_ticket)
    def testcase6_1_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.get_element('#buy_form').click()
        self.type("#bname","test ticket")
        self.type("#bquantity","1")
        self.get_element('#bsubmit').click()
        self.assert_title("Buy")
        
    # Test Case R6.1.2 - The name of the ticket is not alphanumeric-only
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase6_1_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.get_element('#buy_form').click()
        self.type("#bname","test_ticket")
        self.type("#bquantity","1")
        self.get_element('#bsubmit').click()
        self.assert_text("Ticket name must be alphanumeric")
        
    # Test Case R6.1.3 - Space allowed only if it is not the first or the last character.
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase6_1_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.get_element('#buy_form').click()
        self.type("#bname"," testticket")
        self.type("#bquantity","1")
        self.get_element('#bsubmit').click()
        self.assert_text("space allowed only if it is not the first or the last character")
        
# Test Case R6.2 - 	The name of the ticket is no longer than 60 characters
class TestCase6_2(BaseCase):   
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase6_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.get_element('#buy_form').click()
        self.type("#bname","test tickettttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt")
        self.type("#bquantity","1")
        self.get_element('#bsubmit').click()
        self.assert_text("The name of the ticket must be no longer than 60 characters")
        
# Test Case R6.3 - 	The quantity of the tickets has to be more than 0, and less than or equal to 100.
class TestCase6_3(BaseCase):   
    # Test Case R6.3.1 - The quantity of the tickets is not more than 0
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase6_3_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.get_element('#buy_form').click()
        self.type("#bname","test ticket")
        self.type("#bquantity","0")
        self.get_element('#bsubmit').click()
        self.assert_text("The quantity of the tickets has to be more than 0, and less than or equal to 100.")
        
    # Test Case R6.3.2 - The quantity of the tickets is greater than 100
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase6_3_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.get_element('#buy_form').click()
        self.type("#bname","test ticket")
        self.type("#bquantity","101")
        self.get_element('#bsubmit').click()
        self.assert_text("The quantity of the tickets has to be more than 0, and less than or equal to 100.")
    
# Test Case R6.4 - The ticket name exists in the database and the quantity is more than the quantity requested to buy
class TestCase6_4(BaseCase):  
    # Test Case R6.4.1 - The ticket name does not exist in the database
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase6_4_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.get_element('#buy_form').click()
        self.type("#bname","nonexistant ticket")
        self.type("#bquantity","1")
        self.get_element('#bsubmit').click()
        self.assert_text("The ticket name must exist in the database and the quantity must be more than the quantity requested to buy")
        
    # Test Case R6.4.2 - the quantity is not more than the quantity requested to buy
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase6_4_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.get_element('#buy_form').click()
        self.type("#bname","test ticket")
        self.type("#bquantity","30")
        self.get_element('#bsubmit').click()
        self.assert_text("The ticket name must exist in the database and the quantity must be more than the quantity requested to buy")
        
# Test Case R6.5 - The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)
class TestCase6_5(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user_low_balance)
    def testcase6_4_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing2@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.get_element('#buy_form').click()
        self.type("#bname","test ticket")
        self.type("#bquantity","1")
        self.get_element('#bsubmit').click()
        self.assert_text("The user has less balance than the ticket price * quantity + service fee (35%) + tax (5%)")