import sqlite3


class UsersDB:
    def __init__(self, database):
        self.connect = sqlite3.connect(database)
        self.cursor = self.connect.cursor()

    def new_user(self, username, password, score):
        self.cursor.execute(
            'INSERT OR IGNORE INTO users (username, password, score) VALUES (?, ?, ?)', (username, password, score))
        self.connect.commit()

    def add_score(self, score, username):
        self.cursor.execute(
            'UPDATE "users" SET "score"=? WHERE "username"=?', (score, username))
        self.connect.commit()

    def search_user(self, value):
        self.cursor.execute(
            'SELECT * FROM users WHERE username LIKE ?', (f'%{value}%',))
        for line in self.cursor.fetchall():
            return True

    def search_password(self, value):
        self.cursor.execute(
            'SELECT * FROM users WHERE password LIKE ?', (f'%{value}%',))
        for line in self.cursor.fetchall():
            return True

    def search_score(self, username):
        self.cursor.execute(
            'SELECT score FROM users WHERE username LIKE ?', (f'%{username}%',))
        for line in self.cursor.fetchall():
            return (line[0])

    def close(self):
        self.cursor.close()
        self.connect.close()
