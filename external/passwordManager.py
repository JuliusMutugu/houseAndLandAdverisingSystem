import random
import hashlib

class Password:
    numbers = "1234567890"
    letters = "abcdefghijklmnopqrstuvwxyz"
    upperLetters = letters.upper()
    characters = "!@#$%^&*()"
    password_list = list()

    def __init__(self, password_length, number_of_passwords= 10):
        self.password_length = password_length
        self.number_of_passwords = number_of_passwords

    def generate_password(self):
        password_values = self.numbers + self.letters + self.upperLetters + self.characters
        pass_value = ''.join(random.choices(password_values, k=self.password_length))
        # print(pass_value)
        return pass_value

    def password_regenerate(self):
        for i in range(self.number_of_passwords):
            self.generate_password()
            self.password_list.append(self.generate_password())

    def hash_password(self):
        passcode = self.generate_password()
        password_hash = hashlib.md5(passcode.encode('utf8'))
        print("password: "+ self.password_list[3]) 
        print("hashed: " + password_hash.hexdigest())
        return password_hash.hexdigest()
        


password1 = Password(password_length=7)
password1.password_regenerate()
password1.hash_password()
