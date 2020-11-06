from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
import re

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


def register_user(email, name, password, password2):
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
    new_user = User(email=email, name=name, password=hashed_pw)

    db.session.add(new_user)
    db.session.commit()
    return None


def get_all_tickets():
    return []
    
def check_email(email):
    """
    Check if the email is valid (RFC 5322)
    :param email: the email of the user
    :return: true if the email is valid, false if the email is invalid
    """
    email_rules = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if email != "" and re.search(email_rules, email):
        return True
    else:
        return False
    
def check_password(password):
    """
    Check if the password is valid
    :param password: the password of the user
    :return: true if the password is valid, false if the password is invalid
    """
    contains_upper = False
    contains_lower = False
    contains_special = False
    if password == "" or len(password) < 6:
        return False
    for ch in password:
        if ch.isupper():
            contains_upper = True
        elif ch.islower():
            contains_lower = True
        elif not ch.isalnum():
            contains_special = True
    if contains_upper and contains_lower and contains_special:
        return True
    else:
        return False
