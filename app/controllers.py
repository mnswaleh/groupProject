from .comment_models import Comments


comments = Comments()

def create_comment(user_id):
    """Adds comment"""
    message = input('Enter Comment: ')
    comments = Comments()
    comments.add(message, user_id)

def edit_comment(message, comment_id):
    """Edit comment"""
    message = input('Enter message: ')
    comments.edit_comment(message, comment_id)


def edit():
    comment_id = input("Enter option ")
    try:
        int(comment_id)
    except:
        print('Invalid option, try again')
        edit()
    message = input("Enter new comment: ")
    edit_comment(message, comment_id)

def get_all_comments():
    comms = comments.get_comments()
    return comms

def get_user_comments(user_id):
    comms = comments.get_user_comments(user_id)
    return comms

def view_comments(comms):
    """view comments"""
    print('comment_id  |  comment')
    print('-----------------------')
    for comment in comms:
        string = "{}           |   {}".format(comment[0], comment[1])
        print(string)

def options_user():
    """Presents options"""
    print('-------MENU-------')
    print('1:  View comments)')
    print('2:  Edit comments')
    print()
    option = input('What do you want to do: ')
    try:
        option_int = int(option)
    except:
        print('Invalid option try again')
        options_user()
    if option_int == 1:
        comms = get_all_comments()
        view_comments(comms)
    if option == 2:
        comms = get_user_comments(user_id)
        view_comments(comms)
        edit()
    else: 
        print('Invalid option try again')
        options_user()

    



#def main():
 #   """Main function"""

if __name__ == '__main__':
    view_comments()

    


