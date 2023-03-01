from pony.orm import Required, PrimaryKey

from db import app_db

class User:
    name: str
    age: int
    is_active: bool


class UserEntity(app_db.Entity):
    _table_ = "user"
    user_id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    age = Required(int)
    is_active = Required(bool)
