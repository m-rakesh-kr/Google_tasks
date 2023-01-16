import re
from tasks_api import constants
from fastapi import HTTPException, status


def email_validation(email):
    """
    This method validate the user email.
    :param email: user email
    :return: validate email
    """
    regex = constants.EMAIL_REGEX

    if not re.fullmatch(regex, email):
        raise HTTPException(detail=constants.ERR_EMAIL_WRONG, status_code=status.HTTP_401_UNAUTHORIZED)
    else:
        return email


def password_validation(password):
    """
    This method validate the user password according to the regx pattern.
    :param password: user password
    :return: validate password
    """
    regex = constants.PASSWORD_REGEX
    # print(f"REGEXXXXXXXXXXXXXXXXXXXXXXX{re.fullmatch(regex, password)}")
    if re.fullmatch(regex, password):
        return password
    else:
        raise HTTPException(detail=constants.ERR_PASSWORD_WRONG, status_code=status.HTTP_401_UNAUTHORIZED)


def check_confirm_password(password, confirm_password):
    if password != confirm_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=constants.ERR_PASSWORD_NOT_MATCH)
    else:
        valid_pass = password_validation(password)
        return valid_pass
