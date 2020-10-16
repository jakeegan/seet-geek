## R2 Test Cases

Test User:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

Invalid Emails
``` 
invalid_emails = [
    'Abc.example.com',
    'A@b@c@example.com',
    'a"b(c)d,e:f;g<h>i[j\k]l@example.com',
    'just"not"right@example.com',
    'this is"not\allowed@example.com',
    'this\ still\"not\\allowed@example.com',
    '1234567890123456789012345678901234567890123456789012345678901234+x@example.com',
    'i_like_underscore@but_its_not_allow_in_this_part.example.com'
]
```

#### Test case R2.1 - If the user has logged in, redirect back to the user profile page /
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions: 
 - open /logout
 - open /login
 - enter test_user's email into `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /register
 - validate that current page contains `#welcome-header` element

#### Test case R2.2 - Otherwise, show the user registration page
Actions:
 - open /logout
 - open /register
 - validate that current page contains `register-header` element

#### Test case R2.3 - The registration page shows a registration form requesting: email, user name, password, password2
Actions:
 - open /logout
 - open /register
 - validate `#form-register` element contains `#email` field
 - validate `#form-register` element contains `#user-name` field
 - validate `#form-register` element contains `#password` field
 - validate `#form-register` element contains `#password2` field

#### Test case R2.4 - The registration form can be submitted as a POST request to the current URL (/register)
Actions:
 - open /logout
 - open /register
 - validate form element contains `method="post"`
 - validate that current page contains `#btn-submit` element with `value="Register"`

#### Test case R2.5 - Email, password, password2, all have to satisfy the same required as defined in R1
##### Test case R2.5.1 - Password is less shorter than 6 characters
Actions: 
 - open /logout
 - open /register 
 - enter text 'simple@example.com' into `#email`
 - enter text 'user' into `#user-name`
 - enter text 'Test@' into `#password`
 - enter text 'Test@' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'Password must be 6 or more characters'

##### Test case R2.5.2 - Password has no special character
 Actions: 
 - open /logout
 - open /register 
 - enter text 'simple@example.com' into `#email`
 - enter text 'user' into `#user-name`
 - enter text 'Testpassword' into `#password`
 - enter text 'Testpassword' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'Password must contain at least one special character'

##### Test case R2.5.3 - Password has no lower case character
 Actions: 
 - open /logout
 - open /register 
 - enter text 'simple@example.com' into `#email`
 - enter text 'user' into `#user-name`
 - enter text 'TESTPASSWORD@' into `#password`
 - enter text 'TESTPASSWORD@' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'Password must contain at least one lower case character'

##### Test case R2.5.4 - Password has no upper case character
 Actions: 
 - open /logout
 - open /register 
 - enter text 'simple@example.com' into `#email`
 - enter text 'user' into `#user-name`
 - enter text 'testpassword@' into `#password`
 - enter text 'testpassword@' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'Password must contain at least one upper case character'

##### Test case R2.5.5 - Email address does not meet RFC 5322 spec
Mocking:
 - load elements of invalid_emails into invalid_email

Actions:
 - open /logout
 - open /register
 - enter invalid_email into `#email`
 - entner text 'user' into `#user-name`
 - enter text 'testpassword@' into `#password`
 - enter text 'testpassword@' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'Email format is invalid'


#### Test case R2.6 - Password and password2 have to be exactly the same
Actions:
 - open /logout
 - open /register 
 - enter text 'simple@example.com' into `#email`
 - enter text 'user' into `#user-name`
 - enter text 'Test_frontend!' into `#password`
 - enter text 'x' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `#register-message` contains 'Passwords must match'

#### Test case R2.7 - Username has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or last character.
##### Test case R2.7.1 - Username is blank 
Actions: 
 - open /logout
 - open /register 
 - enter text 'simple@example.com' into `#email`
 - enter text '' into `#user-name` (leave blank)
 - enter text 'Test_frontend!' into `#password`
 - enter text 'Test_frontend!' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'Username cannot be blank'

##### Test case R2.7.2 - Username has symbols
Actions:
 - open /logout
 - open /register 
 - enter text 'simple@example.com' into `#email`
 - enter text 'user@' into `#user-name`
 - enter text 'Test_frontend!' into `#password`
 - enter text 'Test_frontend!' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'Username must be alphanumeric'

##### Test case R2.7.3 - Username has spaces as first or last character
Actions:
 - open /logout
 - open /register 
 - enter text 'simple@example.com' into `#email`
 - enter text 'user ' into `#user-name`
 - enter text 'Test_frontend!' into `#password`
 - enter text 'Test_frontend!' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'Username cannot contain trailing spaces'
 - enter text ' user' into `#user-name`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'Username cannot contain leading spaces'

#### Test case R2.8 - Username has to be longer than 2 characters and less than 20 characters.
##### Test case R2.8.1 - Username is less than 2 characters 
Actions:
 - open /logout
 - open /register 
 - enter text 'simple@example.com' into `#email`
 - enter text 'x' into `#user-name`
 - enter text 'Test_frontend!' into `#password`
 - enter text 'Test_frontend!' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'Username must be longer than 2 characters'


##### Test case R2.8.2 - Username is more than 20 characters
Actions:
 - open /logout
 - open /register 
 - enter text 'simple@example.com' into `#email`
 - enter text 'xxxxxxxxxxxxxxxxxxxxxxxxx' into `#user-name`
 - enter text 'Test_frontend!' into `#password`
 - enter text 'Test_frontend!' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'Username must be less than 20 characters.'

#### Test case R2.9 - If the email already exists, show message 'this email has been ALREADY used'
Mocking:
 - Mock backend.get_user to return a test_user interface

Actions:
 - open /logout
 - open /register
 - enter test_user's email into element `#email`
 - enter text 'user' into element `#user-name`
 - enter text 'TestingPassword!' into element `#password`
 - enter text 'Testingpassword!' into element `#password2`
 - click element `input[type="submit"]`
 - validate that current page contains `register-header` element
 - validate that `register-message` contains 'this email has already been used'

#### Test case R2.10 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_balance(test_user) to return the user's balance

Actions:
 - open /logout
 - open /register 
 - enter text 'simple@example.com' into `#email`
 - enter text 'user' into `#user-name`
 - enter text 'Test_frontend!' into `#password`
 - enter text 'Test_frontend!' into element `#password2`
 - click element `input[type="submit"]`
 - validate that test_user's balance is 5000
 - validate that current page contains `#message` element
