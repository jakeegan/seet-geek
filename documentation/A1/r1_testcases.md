## R1 Test Cases

Test User:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

Invalid emails:
```
invalid_email_test_user1 = User(
    email='Abc.example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
invalid_email_test_user2 = User(
    email='A@b@c@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
invalid_email_test_user3 = User(
    email='a"b(c)d,e:f;g<h>i[j\k]l@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
invalid_email_test_user4 = User(
    email='just"not"right@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
invalid_email_test_user5 = User(
    email='this is"not\allowed@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
invalid_email_test_user6 = User(
    email='this\ still\"not\\allowed@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
invalid_email_test_user7 = User(
    email='1234567890123456789012345678901234567890123456789012345678901234+x@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
invalid_email_test_user8 = User(
    email='i_like_underscore@but_its_not_allow_in_this_part.example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

Valid emails:
```
valid_emial_test_user1 = User(
    email='simple@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user2 = User(
    email='very.common@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user3 = User(
    email='disposable.style.email.with+symbol@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user4 = User(
    email='other.email-with-hyphen@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user5 = User(
    email='fully-qualified-domain@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user6 = User(
    email='user.name+tag+sorting@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user7 = User(
    email='x@example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user8 = User(
    email='example-indeed@strange-example.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user9 = User(
    email='admin@mailserver1',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user10 = User(
    email='example@s.example',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user11 = User(
    email='" "@example.org',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user12 = User(
    email='"john..doe"@example.org',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user13 = User(
    email='mailhost!username@example.org',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
valid_email_test_user14 = User(
    email='user%example.com@example.org',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

Invalid password:
```
invalid_password_test_user1 = User(
    email='simple@example.com',
    name='test_frontend',
    password='Test_'
)
invalid_password_test_user2 = User(
    email='simple@example.com',
    name='test_frontend',
    password='test_ing'
)
invalid_password_test_user3 = User(
    email='simple@example.com',
    name='test_frontend',
    password='TEST_ING'
)
invalid_password_test_user4 = User(
    email='simple@example.com',
    name='test_frontend',
    password='Testing'
)
```

Valid password:
```
valid_password_test_user1 = User(
    email='simple@example.com',
    name='test_frontend',
    password='Test_ing'
)

valid_password_test_user2 = User(
    email='simple@example.com',
    name='test_frontend',
    password='Testing!'
)
valid_password_test_user3 = User(
    email='simple@example.com',
    name='test_frontend',
    password='tEst_1'
)
```

#### Test case R1.1 - If the user hasn't logged in, show the login page

##### Test Case R1.1.1 - If the user navigates to /

Actions:
 - open /logout
 - open /
 - validate that current page contains `#message` element
 
##### Test Case R1.1.2 - If the user navigates to /sell

Actions:
 - open /logout
 - open /sell
 - validate that current page contains `#message` element
 
##### Test Case R1.1.3 - If the user navigates to /buy

Actions:
 - open /logout
 - open /buy
 - validate that current page contains `#message` element

#### Test case R1.2 - The login page has a message that by default says 'please login'

Actions:
 - open /logout
 - open /login
 - validate that `#message` element contains the text 'please login'


#### Test case R1.3 - If the user has logged in, redirect to the user profile page

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /login again
 - validate that current page contains `#welcome-header` element
 
#### Test case R1.4 - The login page provides a login form which requests two fields: email and passwords

Actions:
 - open /logout
 - open /login
 - validate that current page contains `#email` element
 - validate that current page contains `#password` element
 
#### Test case R1.5 - The login form can be submitted as a POST request to the current URL (/login)

Actions:
 - open /logout
 - open /login
 - validate form element contains `method="post"`
 - validate that current page contains `#btn-submit` element with `value="Log In"`

#### Test case R1.6 - Email and password both cannot be empty

##### Test case R1.6.1 - Email and password are empty
 
Actions:
 - open /logout
 - open /login
 - click element `input[type="submit"]`
 - validate that `#message` element contains the text 'missing email/password'
 
##### Test case R1.6.2 - Password is empty

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout
 - open /login
 - enter test_user's email into element `#email`
 - click element `input[type="submit"]`
 - validate that `#message` element contains the text 'missing email/password'
 
##### Test case R1.6.3 - Email is empty

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout
 - open /login
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - validate that `#message` element contains the text 'missing email/password'

#### Test case R1.7 - Email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a human-friendly explanation)

##### Test case R1.7.1 - Invalid email entered

Mocking:
 - Mock backend.get_user to return a invalid_email_test_user instance
 
Actions:
 - open /logout
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - validate that `#message` element contains the text 'email/password format is incorrect.'
 
##### Test case R1.7.2 - Valid email entered

Mocking:
 - Mock backend.get_user to return a valid_email_test_user instance
 
Actions:
 - open /logout
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - validate that `#message` element contains the text 'please login'

#### Test case R1.8 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character

##### Test case R1.8.1 - Password doesn't meet requirements

Mocking:
 - Mock backend.get_user to return a invalid_password_test_user instance
 
Actions:
 - open /logout
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - validate that `#message` element contains the text 'email/password format is incorrect.'

##### Test case R1.8.2 - Password meets requirements

Mocking:
 - Mock backend.get_user to return a valid_password_test_user instance
 
Actions:
 - open /logout
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - validate that `#message` element contains the text 'please login'

#### Test case R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'

Mocking:
 - Mock backend.get_user to return a invalid_password_test_user instance or invalid_email_test_user instance
 
Actions:
 - open /logout
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - validate that `#message` element contains the text 'email/password format is incorrect.'

#### Test case R1.10 - If email/password are correct, redirect to /

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - validate that current page contains `#welcome-header` element

#### Test case R1.11 - Otherwise, redict to /login and show message 'email/password combination incorrect'

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - delete test_user instance
 - click element `input[type="submit"]`
 - validate that `#message` element contains the text 'email/password combination incorrect.'