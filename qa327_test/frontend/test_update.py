import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

test_user = User(
    email='testing@test.com',
    name='Test',
    password=generate_password_hash('Testing!'),
    balance=5000
)
test_ticket = Ticket(
    name='test ticket yo',
    quantity='10',
    price='10',
    expiration_date=20201201
)
invalid_ticket_name1 = Ticket(
    name='@testTicket',
    quantity='10',
    price='10',
    expiration_date=20201201
)
invalid_ticket_name2 = Ticket(
    name=' testTicket',
    quantity='10',
    price='10',
    expiration_date=20201201
)
invalid_ticket_name3 = Ticket(
    name='testTicket ',
    quantity='10',
    price='10',
    expiration_date=20201201
)
invalid_ticket_name4 = Ticket(
    name='testTicketxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    quantity='10',
    price='10',
    expiration_date=20201101
)
invalid_ticket_quantity1 = Ticket(
    name='testTicket',
    quantity='0',
    price='10',
    expiration_date=20201101
)
invalid_ticket_quantity2 = Ticket(
    name='testTicket',
    quantity='101',
    price='10',
    expiration_date=20201101
)

# Test case R5.1 - The name of the ticket has to be alphanumeric-only, and space 
# allowed only if it is not the first or last character
class TestCase5_1(BaseCase):
    # Test Case R5.1.1 - Non-alphanumeric
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_1_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","@testTicket")
        self.type("#uquantity","10")
        self.type("#uprice","10")
        self.type("#uexpiration_date","20201201")
        self.get_element('#usubmit').click()
        self.assert_text("Ticket Name must be alphanumeric")

    # Test Case R5.1.2 - First character is a space
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_1_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname"," testTicket")
        self.type("#uquantity","10")
        self.type("#uprice","10")
        self.type("#uexpiration_date","20201201")
        self.get_element('#usubmit').click()
        self.assert_text("Ticket Name must not include a space at the beginning")

    # Test Case R5.1.3 - Last character is a space
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_1_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","testTicket ")
        self.type("#uquantity","10")
        self.type("#uprice","10")
        self.type("#uexpiration_date","20201201")
        self.get_element('#usubmit').click()
        self.assert_text("Ticket Name must not include a space at the end")

# Test case R5.2 - The name of the ticket is no longer than 60 characters
class TestCase5_2(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","testTicketxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.type("#uquantity","10")
        self.type("#uprice","10")
        self.type("#uexpiration_date","20201201")
        self.get_element('#usubmit').click()
        self.assert_text("The name of the ticket must be no longer than 60 characters")

# Test case R5.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100
class TestCase5_3(BaseCase):
    # Test Case R5.3.1 - 0 quantity
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_3_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","testTicket")
        self.type("#uquantity","0")
        self.type("#uprice","10")
        self.type("#uexpiration_date","20201201")
        self.get_element('#usubmit').click()
        self.assert_text("The quantity of the tickets has to be more than 0, and less than or equal to 100.")

    # Test Case R5.3.2  - 101 quantity
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_3_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","testTicket")
        self.type("#uquantity","101")
        self.type("#uprice","10")
        self.type("#uexpiration_date","20201201")
        self.get_element('#usubmit').click()
        self.assert_text("The quantity of the tickets has to be more than 0, and less than or equal to 100.")

class TestCase5_4(BaseCase):

    # Test Case R5.4.1 - Below 10 price
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_4_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","testTicket")
        self.type("#uquantity","10")
        self.type("#uprice","9")
        self.type("#uexpiration_date","20201201")
        self.get_element('#usubmit').click()
        self.assert_text("Ticket Price cannot be less than 10")

    # Test Case R5.4.2 - Above 100 price
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_4_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","testTicket")
        self.type("#uquantity","10")
        self.type("#uprice","10")
        self.type("#uexpiration_date","20201201")
        self.get_element('#usubmit').click()
        self.assert_text("Ticket Price cannot be more than 100")

class TestCase5_5(BaseCase):

    # Test Case R5.5.1 - Below 10 price
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_5_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","testTicket")
        self.type("#uquantity","10")
        self.type("#uprice","10")
        self.type("#uexpiration_date","20/11/01")
        self.get_element('#usubmit').click()
        self.assert_text("Ticket Date must not include non-numeric characters")

    def testcase5_5_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","testTicket")
        self.type("#uquantity","10")
        self.type("#uprice","10")
        self.type("#uexpiration_date","2020111")
        self.get_element('#usubmit').click()
        self.assert_text("Ticket Date must be 8 characters long")

class TestCase5_6(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_6_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","testTicket")
        self.type("#uquantity","10")
        self.type("#uprice","10")
        self.type("#uexpiration_date","20201201")
        self.get_element('#usubmit').click()
        self.assert_text("Update")

    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_6_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "testing@test.com")
        self.type("#password", "Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","nonexistent ticket")
        self.type("#uquantity","10")
        self.type("#uprice","10")
        self.type("#uexpiration_date","20201201")
        self.get_element('#usubmit').click()
        self.assert_text("Ticket name not found")

class TestCase5_7(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase5_7(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","@testTicket")
        self.type("#uquantity","10")
        self.type("#uprice","10")
        self.type("#uexpiration_date","20201201")
        self.get_element('#usubmit').click()
        self.assert_text("Here are all available tickets")
        self.assert_text("Ticket Name must be alphanumeric")