import sqlite3

class UsernamesDB:
    def __init__(self, user):
        self.connect = sqlite3.connect(user)
        self.cursor = self.connect.cursor()

    def new_word(self, username):
        self.cursor.execute(
            'INSERT OR IGNORE INTO programmers (word) VALUES (?)', (username))
        self.connect.commit()

    def list_words(self):
        self.cursor.execute('SELECT username FROM user')
        usernames = self.cursor.fetchall()
        my_list = [(username[0]) for username in usernames]
        return (my_list)

    def close(self):
        self.cursor.close()
        self.connect.close()
