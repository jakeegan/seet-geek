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
