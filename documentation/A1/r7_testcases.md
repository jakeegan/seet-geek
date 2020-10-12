## R7 Test Cases

Test data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

### R7.1 Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.

#### R7.1.1 Logout redirects to the login page

Mocking:
 - Mock backend.get_user to return a test_user instance
 
Actions:
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /logout
 - validate that current page contains `#message` element

#### R7.1.2 After logout, user can't access /update page

Mocking:
 - Mock backend.get_user to return a test_user instance
 
Actions:
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /logout
 - open /update
 - validate that current page contains `#message` element
 
#### R7.1.3 After logout, user can't access /sell page

Mocking:
 - Mock backend.get_user to return a test_user instance
 
Actions:
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /logout
 - open /sell
 - validate that current page contains `#message` element
 
#### R7.1.4 After logout, user can't access /buy page

Mocking:
 - Mock backend.get_user to return a test_user instance
 
Actions:
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /logout
 - open /buy
 - validate that current page contains `#message` element