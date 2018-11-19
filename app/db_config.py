import psycopg2
import os

class DbConnect:
    def __init__(self):
        self.DB_URL = os.getenv('DB_URL')
        self.conn = get_connection(self.DB_URL)
        self.cursor = self.conn.cursor()

    def create_tables(self, url):
        """Create tabes"""
        queries = create_queries()
        try:
            for query in queries:
                self.cursor.execute(query)
        except psycopg2.IntegrityError:
            pass
        self.conn.commit()

def get_connection(url):
    """Creates and return connection"""
    conn = psycopg2.connect(url)
    return conn

def create_queries():
    """Return queries"""
    user_table = """
        CREATE TABLE IF NOT EXISTS users(
        user_id SERIAL PRIMARY KEY,
        username VARCHAR (100) UNIQUE NOT NULL,
        password VARCHAR (50) NOT NULL,
        role VARCHAR (10),
        created_on TIMESTAMP DEFAULT NOW(),
        last_login TIMESTAMP,
        login_status BOOL DEFAULT TRUE
        );"""

    comments = """
        CREATE TABLE IF NOT EXISTS  comments (
        comment_id SERIAL PRIMARY KEY,
        author INTEGER REFERENCES users(user_id) ,
        message VARCHAR (200),     
        is_ative BOOL DEFAULT TRUE,
        parent INTEGER,
        created_on TIMESTAMP DEFAULT NOW()
        );"""
    
    create_admin ="""INSERT INTO users (username, password, role)
                VALUES ('admin', 'password', 'admin');"""


    return [user_table, comments, create_admin]

#get_connection('postgresql://elmonstro:password@localhost:5432/comments')
#DbConnect().create_tables('postgresql://elmonstro:password@localhost:5432/comments')