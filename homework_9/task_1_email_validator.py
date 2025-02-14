"""
Email Validation Module
This module provides a function `email_validator` to validate email addresses.
"""

import re


def email_validator(email: str) -> bool:
    """
    Validates an email address using a regular expression.
    :param email: email to validate
    :return: bool value if email is valid
    :raises TypeError: if email is not a string
    """
    if not isinstance(email, str):
        raise TypeError("Email must be a string")
    email = email.strip().lower()
    email_pattern = re.compile(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$")

    return bool(re.fullmatch(email_pattern, email))


if __name__ == "__main__":
    print(email_validator("test@example.com"))
    print(email_validator("invalid-email.com"))
    print(email_validator("another.test@example.co.uk"))
    print(email_validator("user@domain.co"))
    print(email_validator("  user@domain.com  "))
    print(email_validator("USER@EXAMPLE.COM"))
