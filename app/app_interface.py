from user_models import UsersModel
user_db = UsersModel()
def start_app():
    print("CHOOSE ACTION: \n 1. Sign up 2. Login")
    action = input("Action:")

    if action == 1:
        create_user()
    elif action == 2:
        user_login()
    else:
        print("invalid input")
        
def create_user():
    user_data = {}
    user_data['username'] = input("Enter username:")
    user_data['password'] = input("Enter Password:")
    user_data['role'] = input("Enter role:")

    if user_data['role'] != "user" or user_data['role'] != "moderator" or user_data['role'] != "admin":
        print("invalid role!")

    user_db.create_user(user_data)

def user_login():
    username = input("Enter username:")
    password = input("Enter Password:")

    user = user_db.user_login(username, password)

    if user:
        print('Logged in')
    else:
        print('invalid username or password')

    