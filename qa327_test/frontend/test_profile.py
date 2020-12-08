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
test_ticket_old = Ticket(
    name='test ticket old',
    quantity='10',
    price='10',
    expiration_date=20101101
)
test_update = Ticket(
    name='update ticket',
    quantity='10',
    price='10',
    expiration_date=20201201
)
test_sell = Ticket(
    name='sell ticket',
    quantity='10',
    price='10',
    expiration_date=20201201
)
test_buy = Ticket(
    name='test ticket',
    quantity='10',
    price='10',
    expiration_date=20201201
)

# Test case R3.1 - If the user is not logged in, redirect to login page
class TestCase3_1(BaseCase):
    # Test Case R3.1.1 - If the user is not logged in
    def testcase3_1_1(self):
        self.open(base_url + '/logout')
        self.open(base_url)
        self.assert_title("Log In")

    # Test Case R3.1.2 - If the user is logged in
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_1_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.assert_element('#welcome-header')
    
# Test case 3.2 - This page shows a header 'Hi {}'.format(user.name)
class TestCase3_2(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Hi Test","#welcome-header")

# Test case 3.3 - This page shows user balance
class TestCase3_3(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#balance")

# Test case 3.4 - This page shows a logout link, pointing to /logout
class TestCase3_4(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_4(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.click_link_text('logout')

# Test case 3.5 - This page lists all available tickets. Information including the quantity of each ticket
# the owner's email, and the price, for tickets that are not expired
class TestCase3_5(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    # Test Case R3.5.1 - The page lists available tickets
    def testcase3_5_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#tickets")

    # Test Case R3.5.2 - Information of quantity of each ticket
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_5_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#tickets")
        self.assert_text("Quantity: 10","#tickets")

    # Test Case R3.5.3 - Information of ticket owner's email
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_5_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#tickets")
        self.assert_text("Owners Email: testing@test.com","#tickets")

    # Test Case R3.5.4 - Information of the price of the tickets
    @patch('qa327.backend.get_user', return_value=test_user)
    def testscase3_5_4(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#tickets")
        self.assert_text("Price: 20","#tickets")

    # Test Case R3.5.5/R3.5.6 - Expired tickets do not show 
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_5_5(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.assert_element("#tickets")
        self.assert_false(self.is_text_visible("Name: test ticket old"))

# Test case R3.6 - This page contains a form that a user can submit new tickets for sale.
# Fields: name, quantity, price, expiration date
class TestCase3_6(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_6(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.assert_element("#name")
        self.assert_element("#quantity")
        self.assert_element("#price")
        self.assert_element("#expiration_date")

# Test case R3.7 - This page contains a form that a user can buy new tickets. 
# Fields: name, quantity 
class TestCase3_7(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_7(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#buy_form').click()
        self.assert_element("#bname")
        self.assert_element("#bquantity")

# Test case R3.8 - This page contains a form that a user can update tickets. 
# Fields: name, quantity, price, expiration date 
class TestCase3_8(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_8(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.assert_element("#uname")
        self.assert_element("#uquantity")
        self.assert_element("#uprice")
        self.assert_element("#uexpiration_date")

# Test case R3.9 - The ticket-selling form can be posted to /sell
class TestCase3_9(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_9(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name","sell ticket")
        self.type("#quantity","10")
        self.type("#price","10")
        self.type("#expiration_date","20201201")
        self.click('input[type="submit"]')
        self.assert_title("Sell")
        self.assert_text("Ticket Name: sell ticket")
        self.assert_text("Ticket Quantity: 10")
        self.assert_text("Ticket Price: 10")
        self.assert_text("Ticket Expiration Date: 20201201")

# Test case R3.10 - The ticket-buying form can be posted to /buy
class TestCase3_10(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_ticket', return_value=test_buy)
    def testcase3_10(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#buy_form').click()
        self.type("#bname","test ticket")
        self.type("#bquantity","10")
        self.get_element('#bsubmit').click()
        self.assert_title("Buy")
        self.assert_text("Ticket Name: test ticket")
        self.assert_text("Ticket Quantity: 10")

# Test case R3.11 - The ticket-update form can be posted to /update
class TestCase3_11(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase3_11(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#update_form').click()
        self.type("#uname","test ticket")
        self.type("#uquantity","10")
        self.type("#uprice","20")
        self.type("#uexpiration_date","20201231")
        self.get_element('#usubmit').click()
        self.assert_title("Update")
        self.assert_text("Ticket Name: test ticket")
        self.assert_text("Ticket Quantity: 10")
        self.assert_text("Ticket Price: 20")
        self.assert_text("Ticket Expiration Date: 20201231")
'''