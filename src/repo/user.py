from pony.orm import db_session, select

from models.user import UserEntity

class User:
    @db_session
    def get_all(self):
        users = select(user for user in UserEntity)
        users = [user.to_dict() for user in users]

        #TODO: users map them to User and return list[User]
