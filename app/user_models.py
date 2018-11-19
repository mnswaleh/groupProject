from datetime import datetime
from db_config import DbConnect

class UsersModel():
    def __init__(self):
        self.user_db = DbConnect
        self.today = datetime.now()

    def create_user(self, user_data):
        
        user = {
                "username": user_data['username'],
                "password": user_data['password'],
                "last_login": self.today,
                "role": user_data['role']
            }

        query = """INSERT INTO users(username, password, last_login, role) VALUES(%(username)s, %(password)s, %(last_login)s, %(role)s"""

        curr = self.user_db.cursor
        curr.execute(query, user)

        self.user_db.conn.commit()

        return True


    def user_login(self, username, password):
        query = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)
        curr = self.user_db.cursor
        curr.execute(query)

        data = curr.fetchone()

        if data:
            query = """UPDATE users SET loggin_status = TRUE ,last_login = '{}' where username='{}'""".format(self.today, username)

            curr = self.user_db.cursor
            curr.execute(query)

            self.user_db.conn.commit()
            return True
        else:
            return False

    def user_logout(self, username):
        query = """UPDATE users SET loggin_status = FALSE where username='{}'""".format(username)

        curr = self.user_db.cursor
        curr.execute(query)

        self.user_db.conn.commit()
        return True

    def fetch_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id={}".format(user_id)

        curr = self.user_db.cursor
        curr.execute(query)

        data = curr.fetchone()
        if data:
            result = {}
            for i, key in enumerate(curr.description):
                result[key[0]] = data[i]
            return result
        else:
            return "unknown"
    
