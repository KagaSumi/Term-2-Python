import string
import getpass

def has_uppercase(password: str) -> bool:
    """checks if password has an upper case character

    Args:
        password (str): password to be validated

    Returns:
        bool: True if password contains an uppercase character otherwise False
    """
    pass


def has_lowercase(password: str) -> bool:
    """checks if password contains an lower case character

    Args:
        password (str): password to be validated

    Returns:
        bool: True if password contains a lowercase character otherwise False
    """
    pass


def has_number(password: str) -> bool:
    """checks if password contains a number

    Args:
        password (str): password to be validated

    Returns:
        bool: True if password contains a number otherwise False
    """
    pass


def has_special(password: str) -> bool:
    """checks if password contains one of ~!@#$%^&*_+-=")

    Args:
        password (str): password to be validated

    Returns:
        bool: True if password contains a special character otherwise False
    """
    pass

def has_length(password: str, min_length: int = 10):
    """checks if password length is at least min_length
    
    Args:
        password (str): password to be validated
        
    Returns:
        bool: True if password has at least the required length otherwise False
    """
    pass

def strong_password(password: str) -> bool:
    """Verifies password is at least 10 chars and contains an uppercase, lowercase, special, number

    Args:
        password (str): password to check

    Returns:
        bool: True if a "strong" password otherwise False
    """
    if (
        has_lowercase(password)
        and has_uppercase(password)
        and has_number(password)
        and has_special(password)
        and has_length(password)
    ):
        return True
    else:
        return False


def main():
    """prompts user for and validates users password indicating if it is strong enough
    This function asks the user for their password without displaying it
    and
    """
    password = getpass.getpass("Please enter your password: ")
    if True: # add code as needed
        print("Strong Password")
    else:
        print("Weak Password")


if __name__ == "__main__":
    main()