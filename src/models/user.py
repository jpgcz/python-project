from pony.orm import Required, PrimaryKey

from db import app_db

class User:
    """Represents a User.

        Attributes:
            name (str)
            age (int)
            is_active (bool)
    """
    def __init__(self, name, age, is_active):
        self.name = name
        self.age = age
        self.is_active = is_active


class UserEntity(app_db.Entity):
    _table_ = "user"
    user_id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    age = Required(int)
    is_active = Required(bool)
