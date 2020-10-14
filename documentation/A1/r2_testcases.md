## R2 Test Cases




#### Test case R2.1 - If the user has logged in, redirect back to the user profile page /
Mocking: 
* Mock backend.get_user to return a test_user interface  

#### Test case R2.2 - Otherwise, show the user registration page

#### Test case R2.3 - The registration page shows a registration form requesting: email, user name, password, password2

#### Test case R2.4 - The registration form can be submitted as a POST request to the current URL (/register)

#### Test case R2.5 - Email, password, password2, all have to satisfy the same required as defined in R1

#### Test case R2.6 - Password and password2 have to be exactly the same

#### Test case R2.7 - Username has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or last character.

#### Test case R2.8 - User name has to be longer than 2 characters and less than 20 characters.

#### Test case R2.9 - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)

#### Test case R2.10 - If the email already exists, show message 'this email has been ALREADY used'

#### Test case R2.11 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
