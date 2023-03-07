class login:
    def __init__(self, id, password):
        self.id = id
        self.password = password

    def check(self, id, password):
        print(self.id)
        if self.id == id and self.password == password:
            print("Login success!")
        else:
            print("Login failure!")

log = login("admin", "password")
log.check(input("Enter Login ID: "),
          input("Enter Password: "))