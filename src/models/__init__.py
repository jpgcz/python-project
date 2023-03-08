from .user import UserEntity
from db import app_db

app_db.generate_mapping(create_tables=False)
