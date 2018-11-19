import psycopg2
from datetime import datetime
from .db_config import DbConnect


class Comments:
    def __init__(self):
        self.db = DbConnect()
    
    def add(self, message, author, parent=0 ):
        '''add a comment table'''
        self.db.cursor.execute(
            '''INSERT INTO comments(message,author, parent) VALUES('{}',{} ,{} )'''.format(message,author, parent)
        )

        self.db.conn.commit()
        self.db.cursor.close()

    def edit_comment(self,message,comment_id):
        '''edit a comment'''
        self.db.cursor.execute(
            '''UPDATE comments SET message=%s WHERE id=%s''',
            (message, comment_id)
        )

        self.db.conn.commit()
        self.db.cursor.close()

    def delete_comment(self, comment_id):
        '''delete a comment'''
        self.db.cursor.execute(
            '''DELETE FROM comments WHERE id=%s''',
            (comment_id,)
        )

        self.db.conn.commit()
        self.db.cursor.close()

    def get_comments(self):
        '''fetch all comments'''
        self.db.cursor.execute(
            '''SELECT comment_id , message FROM comments'''
        )

        comments = self.db.cursor.fetchall()

        self.db.conn.commit()
        self.db.cursor.close()
        return comments

    def get_user_comments(self, user_id):
        '''fetch all comments'''
        self.db.cursor.execute(
            '''SELECT comment_id , message FROM comments WHERE author = {}'''.format(user_id)
        )

        comments = self.db.cursor.fetchall()

        self.db.conn.commit()
        self.db.cursor.close()
        return comments

