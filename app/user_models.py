from datetime import date
from .db_config import DbConnect

class UsersModel():
    def __init__(self):
        self.user_db = DbConnect

    def create_user(self, user_data):
        user = {
                "username": user_data['username'],
                "password": user_data['password'],
                "last_login": user_data['password'],
                "role": user_data['role']
            }

        query = """INSERT INTO users(username, password, last_login, role) VALUES(%(username)s, %(password)s, %(last_login)s, %(role)s"""

        curr = self.user_db.cursor
        curr.execute(query, user)

        self.user_db.conn.commit()

        return True


    def user_login(self, username, password):
        query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)
        curr = self.user_db.curso
        curr.execute(query)

        data = curr.fetchone()

        if data:
            query = """UPDATE users SET loggin_status = TRUE where username='{}'""".format(username)

            curr = self.user_db.cursor
            curr.execute(query)

            self.user_db.conn.commit()
            return True
        else:
            return False

    
    
