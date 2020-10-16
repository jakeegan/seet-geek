## R3 Test Cases

Test User:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')

```
```
test_tickets = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=10,
    price=10
    date='20201101'
),
TicketOld(
    owner='test_frontend@test.com',
    name='test_ticket_old',
    quantity=10,
    price=10
    date='201001101'
)
```
```
test_update = TicketUp(
    name='update_ticket'
    quantity=10
    price=10
    date='20201101'
)
test_sell = TicketSe(
    name='sell_ticket'
    quantity=10
    price=10
    date='20201101'
)
test_buy = TicketBu(
    name='buy_ticket'
    quantity=10
)
```

### Test case R3.1 - If the user is not logged in, redirect to login page

#### Test Case R3.1.1 - If the user is not logged in

Actions:
- open /logout
- open /
- validate /login opens

#### Test Case R3.1.2 - If the user is logged in
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- validate / opens

### Test case R3.2 - This page shows a header 'Hi {}'.format(user.name)

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- validate current page `#welcome-header` element displays `Hi test_frontend`

### Test case R3.3 - This page shows user balance

Mocking:
- Mock backend.get_balance to return the users balance

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- validate current page contains `#balance` element

### Test case R3.4 - This page shows a logout link, pointing to /logout

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- click element `input[type="logout"]`
- validate /logout is open


### Test case R3.5 - This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired

Mocking:
- Mock backend.get_all_tickets

#### Test Case R3.5.1 - This page lists available tickets

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- validate element `#Ticket` displays text `test_ticket_yo` 

#### Test Case R3.5.2 - Information of quantity of each ticket

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- validate element `#Ticket` displays text `quantity` and that value is `10`


#### Test Case R3.5.3 - Information of ticket owner's email

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- validate element `#Ticket` displays owner's email
- validate email matches `test_frontend@test.com`

#### Test Case R3.5.4 - Information of the price of the tickets

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- validate all element `#Ticket` displays text `price` and a value of `10`

#### Test Case R3.5.5 - Expired Tickets not shown - Not expired

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- validate no element `#Ticket` displays date older than current date
- validate element `#Ticket` displayes date `20201101`

#### Test Case R3.5.6 - Expired Tickets not shown - Expired

Actions
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- validate element `#TicketOld` displays field `date` with a value of `20101101`
- validate element `#TicketOld` displays field `name` with a value of `test_ticket_old`
- validate element `#TicketOld` does not display `quantity`,`user email`, and `price`

### Test case R3.6 - This page contains a form that a user can submit new tickets for sale. Fields: name, quantity, price, expiration date

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- open element `#form-sell`
- validate `#form-sell` element contains `#name` field
- validate `#form-sell` element contains `#quantity` field
- validate `#form-sell` element contains `#price` field
- validate `#form-sell` element contains `#expiration date` field
- validate `#form-sell` element contains button `#submit`


### Test case R3.7 - This page contains a form that a user can buy new tickets. Fields: name, quantity

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- open element `#form-buy`
- validate `#form-buy` element contains `#name` field
- validate `#form-buy` element contains `#quantity` field
- validate `#form-buy` element contians button `#submit`

### Test case R3.8 - This page contains a form that a user can update tickets. Fields: name, quantity, price, expiration date

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- open element `#form-update`
- validate `#form-update` element contains `#name` field
- validate `#form-update` element contains `#quantity` field
- validate `#form-update` element contains `#price` field
- validate `#form-update` element contains `#expiration date` field
- validate `#form-update` element contains button `#submit`

### Test case R3.9 - The ticket-selling form can be posted to /sell

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- input `ticket_se` in `#form_sell`
- click element `input[type="submit"]`
- validate /sell opens
- click element `input[type="confirm-sell"]`
- validate `#form-sell` is posted

### Test case R3.10 - The ticket-buying form can be posted to /buy

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- input `ticket_bu` in `#form-buy`
- click element `input[type="submit"]`
- validate /buy opens
- click element `input[type="confirm-buy"]`
- validate `#form-buy` is posted

### Test case R3.11 - The ticket-update form can be posted to /update

Actions:
- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- input `ticket_up` in `#form-update`
- click element `input[type="submit"]`
- validate /update opens
- click element `input[type="confirm-update"]`
- validate `#form-update` is posted

