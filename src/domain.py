# 1. Typing args en python2.7 y 3.9
# Docs
"""
users: List users. per each user, concat a hi
*args = saludos: ("hi", "hola") -> solo uno
return ["{saludo} user.name", ]
users is empty or args empty -> []
"""

from src.models.user import User

"""
py3.10: get_hi_for_users(users: list[str], *args: tuple[str]) -> list[str]:
py3.7: get_hi_for_users(users: List[str], *args):
p2.7:
    :param n datatype:
    :param nom:
    :type: list[str3]

    #
"""
def get_hi_for_users(users, *args):
    """ Greetings to all users that are in the list
    users (List)
    *args

    Returns: a List
    """
    if not isinstance(users, list):
        raise ValueError("users must be a list")

    his = args or ("hi",)
    greetings = ["{hi} {name}".format(hi=his[0], name=user.name) for user in users]

    return greetings
