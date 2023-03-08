import sqlite3

class PasswordsDB:
    def __init__(self, password):
        self.connect = sqlite3.connect(password)
        self.cursor = self.connect.cursor()

    def new_word(self, password):
        self.cursor.execute(
            'INSERT OR IGNORE INTO programmers (word) VALUES (?)', (password))
        self.connect.commit()

    def list_words(self):
        self.cursor.execute('SELECT password FROM user')
        passwords = self.cursor.fetchall()
        my_list = [(password[0]) for password in passwords]
        return (my_list)

    def close(self):
        self.cursor.close()
        self.connect.close()