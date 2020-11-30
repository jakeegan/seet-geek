## R3 Test Cases

Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
    balance=15
)
low_balance_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
    balance=5
)
```
```
test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo'
    quantity=10,
    price=10
    date='20201101'
)
buy_ticket = Ticket(
    name='test_ticket_yo'
    quantity=10
)
test_ticket_named = Ticket(
    name='test_ticketzzz'
    quantity=10
)
test_ticket_low = Ticket(
    name='test_ticket_yo'
    quantity=15
)
```
```
invalid_ticket_name1 = Ticket(
    owner='test_frontend@test.com',
    name='@testTicket',
    quantity=10,
    price=10
    date='20201101'
)
invalid_ticket_name2 = Ticket(
    owner='test_frontend@test.com',
    name=' testTicket',
    quantity=10,
    price=10
    date='20201101'
)
invalid_ticket_name3 = Ticket(
    owner='test_frontend@test.com',
    name='testTicket ',
    quantity=10,
    price=10
    date='20201101'
)
invalid_ticket_name4 = Ticket(
    owner='test_frontend@test.com',
    name='testTicketxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    quantity=10,
    price=10
    date='20201101'
)
```
```
invalid_ticket_quantity1 = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=0,
    price=10
    date='20201101'
)
invalid_ticket_quantity2 = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=101,
    price=10
    date='20201101'
)
```

### Test case R6.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or last character

#### Test Case R6.1.1 - The name of the ticket is not alphanumeric

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_name1's name into element `#buy_name`
- enter invalid_ticket_name1's quantity into element `#buy_quantity`
- enter invalid_ticket_name1's price into element `#buy_price`
- enter invalid_ticket_name1's date into element `#buy_date`
- click element `#buy_submit`
- validate `#error-message` displays message `Ticket Name must be alphanumeric`
- open /logout

#### Test Case R6.1.2 - The name of the ticket does not have a space as the first character

- open logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_name2's name into element `#buy_name`
- enter invalid_ticket_name2's quantity into element `#buy_quantity`
- enter invalid_ticket_name2's price into element `#buy_price`
- enter invalid_ticket_name2's date into element `#buy_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Name must not include a space at the beginning`


#### Test Case R6.1.3 - The name of the ticket does not have a space as the last character

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_name3's name into element `#buy_name`
- enter invalid_ticket_name3's quantity into element `#buy_quantity`
- enter invalid_ticket_name3's price into element `#buy_price`
- enter invalid_ticket_name3's date into element `#buy_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Name must not include a space at the end`

### Test case R6.2 - The name of the ticket is no longer than 60 characters

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_name4's name into element `#buy_name`
- enter invalid_ticket_name4's quantity into element `#buy_quantity`
- enter invalid_ticket_name4's price into element `#buy_price`
- enter invalid_ticket_name4's date into element `#buy_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Name must not be longer than 60 characters`

### Test case R6.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100

#### Test Case R6.3.1 - The quantity of the tickets has to be more than 0

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_quantity1's name into element `#buy_name`
- enter invalid_ticket_quantity1's quantity into element `#buy_quantity`
- enter invalid_ticket_quantity1's price into element `#buy_price`
- enter invalid_ticket_quantity1's date into element `#buy_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Quantity must be more than 0`

#### Test Case R6.3.2 - The quantity of the tickets is less than or equal to 100

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_quantity2's name into element `#buy_name`
- enter invalid_ticket_quantity2's quantity into element `#buy_quantity`
- enter invalid_ticket_quantity2's price into element `#buy_price`
- enter invalid_ticket_quantity2's date into element `#buy_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Quantity cannot be more than 100`

### Test case R6.4 - The ticket name exists in the database and the quantity is more than the quantity requested to buy

#### Test Case R6.4.1 - The ticket name and quantity exists in the database

Mocking:
- Mock backened.get_ticket to try to find the ticket

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- open element `#form-buy` 
- input buy_ticket into `#form-buy`
- click element `input[type="submit"]`
- validate ticket `test_ticket_yo` is displayed

#### Test Case R6.4.2 - The ticket name does not exist

Mocking:
- Mock backened.get_ticket to try to find the ticket

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- open element `#form-buy` 
- input test_ticket_named into `#form-buy`
- click element `input[type="submit"]`
- validate element `#error-message` displays 'Ticket name not found'

#### Test Case R6.4.3 - The ticket quantity is too high

Mocking:
- Mock backened.get_ticket to try to find the ticket

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- open element `#form-buy` 
- input test_ticket_low into `#form-buy`
- click element `input[type="submit"]`
- validate element `#error-message` displays 'Ticket quantity too high'

### Test case R6.5 - The user has more balance than the ticket price*quantity + service fee (35%) + tax (5%)

#### Test Case R6.5.1 - The user does not have enough funds

Mocking:
- Mock backend.get_user_balance to get user balance

Actions:
- open /logout
- open /login
- enter low_balance_user's email into element `#email`
- enter low_balance_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- open element `#form-buy` 
- input buy_ticket into `#form-buy`
- validate element `#error-message` displays 'Not enough funds'

#### Test Case R6.5.2 - The user does have enough funds

Mocking:
- Mock backend.get_user_balance to get user balance

Actions:
- open /logout
- open /login
- enter low_balance_user's email into element `#email`
- enter low_balance_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- open element `#form-buy` 
- input buy_ticket into `#form-buy`
- validate element `#error-message` displays 'Not enough funds'

### Test case R6.6 - For any errors, redirect back to / and show an error message


Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_name1's name into element `#buy_name`
- enter invalid_ticket_name1's quantity into element `#buy_quantity`
- enter invalid_ticket_name1's price into element `#buy_price`
- enter invalid_ticket_name1's date into element `#buy_date`
- click element `input[type="submit"]`
- validate page is redirected to /
- validate `#error-message` displays message `Ticket Date must be 8 characters long`
