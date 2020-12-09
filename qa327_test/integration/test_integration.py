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

test_ticket = Ticket(
    name='test ticket',
    quantity='10',
    price='10',
    expiration_date=20201201
)

# Test Case R9.1 - Integration: User create postings and purchasing
class TestCase9_1(BaseCase):   
    @patch('qa327.backend.get_user', return_value=test_user)
    # Test Case R9.1.1 - User creates a posting for a ticket
    def testcase9_1_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.get_element('#sell_form').click()
        self.type("#name","new ticket")
        self.type("#quantity","10")
        self.type("#price","10")
        self.type("#expiration_date","20201201")
        self.click('input[type="submit"]')
        self.assert_title("Sell")
        self.open(base_url)
        self.assert_element("#tickets")
        self.assert_text("Name: new ticket","#tickets")
        self.open(base_url + '/logout')
        self.assert_element("#message")
        self.assert_text("please login", "#message")
    
    @patch('qa327.backend.get_user', return_value=test_user)
    # Test Case R9.1.2 - User purchases a ticket
    def testcase9_1_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.get_element('#buy_form').click()
        self.type("#bname","test ticket")
        self.type("#bquantity","1")
        self.get_element('#bsubmit').click()
        self.assert_title("Buy")
        self.open(base_url)
        self.assert_element("#tickets")
        self.assert_text("Quantity: 9","#tickets")
        self.assert_text("Available balance: $4972.0", "#balance")
        self.open(base_url + '/logout')
        self.assert_element("#message")
        self.assert_text("please login", "#message")