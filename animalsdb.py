import sqlite3


class AnimalsDB:
    def __init__(self, database):
        self.connect = sqlite3.connect(database)
        self.cursor = self.connect.cursor()

    def new_word(self, word):
        self.cursor.execute(
            'INSERT OR IGNORE INTO animals (word) VALUES (?)', (word,))
        self.connect.commit()

    def list_words(self):
        self.cursor.execute('SELECT word FROM animals')
        words = self.cursor.fetchall()
        my_list = [(word[0]) for word in words]
        return (my_list)

    def close(self):
        self.cursor.close()
        self.connect.close()
