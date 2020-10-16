## R3 Test Cases

Test User:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')

```
```
test_tickets = [
    {'name':'t1','price':'100'}
]
```

### Test case R3.1 - If the user is not logged in, redirect to login page

Actions:
 - open /logout
 - open /login
 - validate user
 - open /

### Test case R3.2 - This page shows a header 'Hi {}'.format(user.name)

Actions:
 - open /logout
 - open /login
 - validate user
 - open / 
 - validate current page '#welcome-header' element displays 'Hi test_frontend'

### Test case R3.3 - This page shows user balance

Mocking:
- Mock backend.get_balance to return the users balance

Actions:
 - open /logout
 - open /login
 - validate user
 - open /
 - validate current page contains '#balance' element

### Test case R3.4 - This page shows a logout link, pointing to /logout

Actions:
- open /logout
- open /login
- validate user
- open /
- click element 'input[type="logout"]'
- validate /logout is open


### Test case R3.5 - This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.

Mocking:
- Mock backend.get_all_tickets

#### Test Case R3.5.1 - This page lists available tickets

Actions:
- open /logout
- open /login
- validate user
- open /
- validate element '#tickets' displays text 'name' 

#### Test Case R3.5.2 - Information of quantity of each ticket

Actions:
- open /logout
- open /login
- validate user
- open /
- count number of '#tickets' displayed 
- validate element '#tickets' displays text 'quantity' and that value matches the counted value


#### Test Case R3.5.3 - Information of ticket owner's email

Actions:
- open /logout
- open /login
- validate user
- open /
- validate element '#tickets' displays owner's email
- validate email matches 'test_frontend@test.com'

#### Test Case R3.5.4 - Information of the price of the tickets

Actions:
- open /logout
- open /login
- validate user
- open /
- validate all element '#tickets' displays text 'price'

#### Test Case R3.5.5 - Expired Tickets not shown

Actions:
- open /logout
- open /login
- validate user
- open /
- validate no element '#tickets displays date older than current date

### Test case R3.6 - This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date

Actions:
- open /logout
- open /login
- validate user
- open /
- open element '#form-sell'
- validate '#form-sell' element contains '#name' field
- validate '#form-sell' element contains '#quantity' field
- validate '#form-sell' element contains '#price' field
- validate '#form-sell' element contains '#expiration date' field


### Test case R3.7 - This page contains a form that a user can buy new tickets. Fields: name, quantity

Actions:
- open /logout
- open /login
- validate user
- open /
- open element '#form-buy'
- validate '#form-buy' element contains '#name' field
- validate '#form-buy' element contains '#quantity' field

### Test case R3.8 - The ticket-selling form can be posted to /sell

Actions:
- open /logout
- open /login
- validate user
- open /
- fill in '#form-sell'
- click element 'input[type="sell"]'
- validate /sell opens
- click element 'input[type="confirm-sell"]'
- validate '#form-sell' is posted

### Test case R3.9 - The ticket-buying form can be posted to /buy

### Test case R3.10 - The ticket-update form can be posted to /update

