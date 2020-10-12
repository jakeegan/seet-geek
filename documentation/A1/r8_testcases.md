## R8 Test Cases

Test data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

test_page=generate_random_nonexistent_page()
```

### R8.1 For any other requests except the ones above, the system should return a 404 error

#### R8.1.1 User logged in and tries to make a request to a nonexistent page

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_page to return a test_page instance
 
Actions:
 - open /logout
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /test_page
 - validate that current page contains message '404 error'
 
#### R8.1.1 User not logged in and tries to make a request to a nonexistent page
Mocking:
 - Mock backend.get_page to return a test_page instance
 
Actions:
 - open /logout
 - open /test_page
 - validate that current page contains message '404 error'