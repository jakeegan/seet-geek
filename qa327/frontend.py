from flask import render_template, request, session, redirect, flash
from qa327 import app
import qa327.backend as bn

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', message='Oops! Looks like you\'ve come to the wrong page ')

@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    if 'logged_in' in session:
        return redirect('/')
    return render_template('register.html', message='')

@app.route('/register', methods=['POST'])
def register_post():
    # Retrieve data from user
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    balance = 5000
    error_message = None
    
    # Validate user registration
    registration_ret, registration_error = bn.check_registration(email, name, password, password2)
    
    if not registration_ret:
        error_message = registration_error
    # Check if user already exists
    else:
        user = bn.get_user(email)
        if user:
            error_message = "This email has already been used"
        else:
            error_message = bn.register_user(email, name, password, password2, balance)

    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/login', methods=['GET'])
def login_get():
    # If user is already logged in, send them to index, otherwise send them to login
    if 'logged_in' in session:
        return redirect('/')
    else:
        return render_template('login.html', message='please login')


@app.route('/login', methods=['POST'])
def login_post():
    # Retrieve data from user
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Validate email and password
    email_ret, email_error = bn.check_email(email)
    password_ret, password_error = bn.check_password(password)
    
    if not email_ret or not password_ret:
        return render_template('login.html', message='email/password format is incorrect.')
    user = bn.login_user(email, password)
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='email/password combination incorrect')


@app.route('/logout')
def logout():
    # log user out if they are logged in
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    bn.add_new_ticket(name="test ticket",quantity=10,price=20,expiration_date=20201231)
    bn.add_new_ticket(name="test_ticket2",quantity=10,price=20,expiration_date=20201231)
    bn.add_new_ticket(name="test_ticket_old",quantity=10,price=20,expiration_date=20101101)
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, ticket=tickets)

@app.route('/sell', methods=['GET', 'POST'])
def sell_post():
    if 'logged_in' in session:
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        price = request.form.get('price')
        expiration_date = request.form.get('expiration_date')
        # templates are stored in the templates folder
        return render_template('sell.html', name=name, quantity=quantity, price=price, expiration_date=expiration_date)
    else:
        flash('You cannot access /sell while being logged out')
        return redirect('/login')


@app.route('/buy', methods=['GET', 'POST'])
def buy_post():
    if 'logged_in' in session:
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        email = session['logged_in']
        user = bn.get_user(email)
        # Check if buying a ticket is valid
        ret, error = bn.check_buy_ticket(name, quantity, user)
        if not ret:
            # If not valid, return error
            tickets = bn.get_all_tickets()
            return render_template('index.html', user=user,ticket=tickets, message=error)
        else:
            # If valid, call buy ticket and update GUI
            bn.buy_ticket(name, quantity, user)
            return render_template('buy.html', name=name, quantity=quantity)
    else:
        flash('You cannot access /buy while being logged out')
        return redirect('/login')


@app.route('/update', methods=['GET', 'POST'])
def update_post():
    if 'logged_in' in session:
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        price = request.form.get('price')
        expiration_date = request.form.get('expiration_date')
        # templates are stored in the templates folder
        return render_template('update.html', name=name, quantity=quantity, price=price, expiration_date=expiration_date)
    else:
        flash('You cannot access /update while being logged out')
        return redirect('/login')
