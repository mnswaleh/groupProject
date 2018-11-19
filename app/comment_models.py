import psycopg2
from datetime import datetime
from db_config import DbConnect


class Comments(DbConnect):
    def __init__(self, message = None, author = None):
        self.message = message
        self.author = author
        self.time = str(datetime.now())
    
    def add(self):
        '''add a comment table'''
        self.cursor.execute(
            '''INSERT INTO comments(message,author,time,date) VALUES(%s, %s, %s, %s)''',
            (self.message,self.author,self.author,self.date)
        )

        self.connection.commit()
        self.cursor.close()

    def edit_comment(self,message,comment_id):
        '''edit a comment'''
        self.cursor.execute(
            '''UPDATE comments SET message=%s WHERE id=%s''',
            (message, comment_id)
        )

        self.connection.commit()
        self.cursor.close()

    def delete_comment(self, comment_id):
        '''delete a comment'''
        self.cursor.execute(
            '''DELETE FROM comments WHERE id=%s''',
            (comment_id,)
        )

        self.connection.commit()
        self.cursor.close()

