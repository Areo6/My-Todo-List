import re
import string


def is_valid_name(name):
    """
    This function checks the validity of the input Name.
    """
    if not isinstance(name, str):
        return "Bad input. Name should be a string"
    if len(name.strip()) == 0:
        return "Name can't be empty. Please enter a valid name"
    elif len(name.strip()) < 3:
        return "Invalid Name. Name must be at least 3 characters"
    else:
        return "Valid 1"
    
def is_valid_email(email):
    """
    This function checks the validity of email.
    """
    is_valid = re.search(r"[\w-]+@[\w-]+\.+", email)
    if not is_valid:
        return "Invalid email. Email should be of format 'john12@gmail.com'"
    else:
        return "Valid 2"

def is_valid_password(password):
    """
    This function checks the validity of a password
    """
    if not isinstance(password, str):
        return "Invalid input. Password must be a string of characters"
    if len(password) < 6:
        return "Invalid password. Password must be at least 6 characters long"
    
    upper, lower, symbol, digit = False, False, False, False
    for char in password:
        if char in string.ascii_uppercase:
            upper = True
        elif char in string.ascii_lowercase:
            lower = True
        elif char in string.digits:
            digit = True
        elif char in string.punctuation + ' \t\r\x0b\x0c':
            symbol = True
    if upper == True and lower == True and symbol == True and digit == True:
        return "Valid 3"
    else:
        return "Weak password. Password must contain at least one upper case, lower case and a special caracter"
    
def is_existing_user(account, email):
    """
    This function return True if the user with email has an account and False otherwise
    """
    existing_user = [x for x in account if x["email"] == email]
    if len(existing_user) != 0:
        return True
    return False

def valid_task(task):
    """
    This function checks if a task is a valid or not
    """
    if not isinstance(task, str):
        return "Invalid format. Tsk must be a string"
    if len(task.strip()) < 2:
        return "Task must be at least 2 characters long"
    return "Valid"
    