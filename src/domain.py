# 1. Typing args en python2.7 y 3.9
# Docs
"""
users: List users. per each user, concat a hi
*args = saludos: ("hi", "hola") -> solo uno
return ["{saludo} user.name", ]
users is empty or args empty -> []
"""

from src.models.user import User


def get_hi_for_users(users: list, *args):
    """ Greetings to all users that are in the list
    users (List)
    *args

    Returns: a List
    """
    greetings = []

    if bool(users):
        for user in users:
            greetings.append(f"{args[0]} {user.name}")

    return greetings
