from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
import re
from sqlalchemy import exc

"""
This file defines all backend logic that interacts with database and other services
"""


def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user
    
def get_ticket(name):
    """
    Get a ticket by a given name
    :param name: the name of the ticket
    :return: a ticket object
    """
    ticket = Ticket.query.filter_by(name=name).first()
    return ticket


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2, balance):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw, balance=balance)

    try:
        db.session.add(new_user)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return(e._message)

    return None

def add_new_ticket(name,quantity,price,expiration_date):
    """
    Create new ticket to database
    :param name: the name of the ticket
    :param quantity: the quantity of tickets
    :param price: the price of the ticket
    :param expiration_date: the expiration date of the ticket
    :return: returns None
    """
    new_ticket = Ticket(name=name,quantity=quantity,price=price,expiration_date=expiration_date)
    if new_ticket.expiration_date < 20200831:
        return None
    elif not Ticket.query.filter_by(name=new_ticket.name).count():
        db.session.add(new_ticket)
        db.session.commit()

    return None


def get_all_tickets():
    """
    Returns all the user's tickets
    :return: all the tickets
    """
    tickets = Ticket.query.all()
    return tickets
    
def check_registration(email, name, password1, password2):
    """
    Check if all the registration data is valid
    :param email: the email of the user
    :param name: username of the user
    :param password1: first password of the user
    :param password2: second password of the user
    :return: true if the registration is valid, false if the registration is invalid
    :return: error message if there is any
    """
    error = None
    
    # Validate email, name, and password
    email_ret, email_error = check_email(email)
    name_ret, name_error = check_username(name)
    password_ret, password_error = check_password(password1)
    
    if password1 != password2:
        error = "Passwords must match"
    elif not email_ret:
        error = email_error
    elif not name_ret:
        error = name_error
    elif not password_ret:
        error = password_error
    return not error, error

    
def check_username(name):
    """
    Check if the username is valid
    :param name: the username of the user
    :return: true if the name is valid, false if the name is invalid
    :return: error message if there is any
    """
    error = None
    if name == "":
        error = "Username cannot be blank"
    elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(name):
        error = "Username must be alphanumeric"
    elif name.startswith(' '):
        error = "Username cannot contain leading spaces"
    elif name.endswith(' '):
        error = "Username cannot contain trailing spaces"
    elif len(name) < 2:
        error = "Username must be longer than 2 characters"
    elif len(name) >= 20:
        error = "Username must be less than 20 characters."
    return not error, error
    
def check_email(email):
    """
    Check if the email is valid according to RFC 5322
    :param email: the email of the user
    :return: true if the email is valid, false if the email is invalid
    :return: error message if there is any
    """
    error = None
    email_rules = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if email == "":
        error = "Email is empty"
    elif not re.search(email_rules, email):
        error = "Email format is invalid"
    return not error, error
    
def check_password(password):
    """
    Check if the password is valid
    :param password: the password of the user
    :return: true if the password is valid, false if the password is invalid
    :return: error message if there is any
    """
    error = None
    if len(password) < 6:
        error = "Password must be 6 or more characters"
    elif not set('[~!@#$%^&*()_+{}":;\']+$').intersection(password):
        error = "Password must contain at least one special character"
    elif not any(c.isupper() for c in password):
        error = "Password must contain at least one upper case character"
    elif not any(c.islower() for c in password): 
        error = "Password must contain at least one lower case character"
    return not error, error    

# For sell and update
def check_ticket(name,quantity,price,expiration_date):
    """
    Check if the ticket information is valid
    :param name: name of the ticket
    :param quantity: quantity of tickets
    :param price: price of the ticket
    :param expiration_date: the expiration date of the ticket
    :return: true if the ticket is valid, false if the ticket is invalid
    :return: error message if there is any
    """
    error = None
    if set('[~!@#$%^&*()_+{}":;\']+$').intersection(name):
        error = "Ticket Name must be alphanumeric"
    elif name.startswith(' '):
        error = "Ticket Name must not include a space at the beginning"
    elif name.endswith(' '):
        error = "Ticket Name must not include a space at the end"
    elif int(price) < 10:
        error = "Ticket Price cannot be less than 10"
    elif int(price) > 100:
        error = "Ticket Price cannot be more than 100"
    elif not expiration_date.isdecimal(): 
        error = "Ticket Date must not include non-numeric characters"
    elif len(expiration_date) != 8:
        error = "Ticket Date must be 8 characters long"
    elif len(name) > 60:
        error = "The name of the ticket must be no longer than 60 characters"
    elif int(quantity) <= 0 or int(quantity) > 100:
        error = "The quantity of the tickets has to be more than 0, and less than or equal to 100."
    return not error, error


def check_update_ticket(name,quantity,price,expiration_date):
    """
    Check if the ticket information is valid
    :param name: name of the ticket
    :param quantity: quantity of tickets
    :param price: price of the ticket
    :param expiration_date: the expiration date of the ticket
    :return: true if the ticket is valid, false if the ticket is invalid
    :return: error message if there is any
    """
    error = None
    if set('[~!@#$%^&*()_+{}":;\']+$').intersection(name):
        error = "Ticket Name must be alphanumeric"
    elif name.startswith(' '):
        error = "Ticket Name must not include a space at the beginning"
    elif name.endswith(' '):
        error = "Ticket Name must not include a space at the end"
    elif int(price) < 10:
        error = "Ticket Price cannot be less than 10"
    elif int(price) > 100:
        error = "Ticket Price cannot be more than 100"
    elif not expiration_date.isdecimal(): 
        error = "Ticket Date must not include non-numeric characters"
    elif len(expiration_date) != 8:
        error = "Ticket Date must be 8 characters long"
    elif len(name) > 60:
        error = "The name of the ticket must be no longer than 60 characters"
    elif int(quantity) <= 0 or int(quantity) > 100:
        error = "The quantity of the tickets has to be more than 0, and less than or equal to 100."
    elif Ticket.query.filter_by(name=name).count() == 0:
        error = "Ticket name not found"
    return not error, error
 
# For buy
def check_buy_ticket(name,quantity, user):
    """
    Check if the ticket can be bought
    :param name: name of the ticket
    :param quantity: quantity of tickets
    :param user: the user buying the ticket
    :return: true if the ticket is valid, false if the ticket is invalid
    :return: error message if there is any
    """
    error = None

    if set('[~!@#$%^&*()_+{}":;\']+$').intersection(name):
        error = "Ticket name must be alphanumeric"
    elif name.startswith(' ') or name.endswith(' '):
        error = "space allowed only if it is not the first or the last character"
    elif len(name) > 60:
        error = "The name of the ticket must be no longer than 60 characters"
    elif int(quantity) <= 0 or int(quantity) > 100:
        error = "The quantity of the tickets has to be more than 0, and less than or equal to 100."
    elif Ticket.query.filter_by(name=name).count() == 0 or int(quantity) > int(get_ticket(name).quantity):
        error = "The ticket name must exist in the database and the quantity must be more than the quantity requested to buy"
    elif user.balance < int(get_ticket(name).price)*int(quantity)*1.4:
        error = "The user has less balance than the ticket price * quantity + service fee (35%) + tax (5%)"
    return not error, error
    
def buy_ticket(name, quantity, user):
    """
    Perform the action of buying a ticket by updating ticket and user objects in database
    :param name: name of the ticket
    :param quantity: quantity of tickets
    :param user: the user buying the ticket
    """
    update_ticket = get_ticket(name)
    update_ticket.quantity = int(update_ticket.quantity) - int(quantity)
    update_user = user
    update_user.balance = int(update_user.balance) - int(update_ticket.price)*int(quantity)*1.4
    
    try:
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return(e._message)
    

