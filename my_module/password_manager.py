from cryptography.fernet import Fernet
from tabulate import tabulate
import random
import string
import os


class PasswordManager:

    def __init__(self):
        self.path = None
        self.key = None
        self.table = []
        self.headers = ["site", "password"]

    def set_path_key(self, path, key):
        self.path = path
        self.key = key

    def read_existing_file(self):
        # Reset Table
        self.table.clear()
        f = Fernet(self.key)
        with open(self.path, "r") as file:
            file.readline()  # skip first line
            for line in file:
                site, password = line.split(",")
                self.table.append([f.decrypt(site).decode("utf-8"), f.decrypt(password).decode("utf-8")])

    def write_existing_file(self):
        f = Fernet(self.key)

        with open(self.path, "w") as file:
            # Write the first line: site,password
            file.write(f"{f.encrypt(b'site').decode('utf-8')},{f.encrypt(b'password').decode('utf-8')}\n")

            for row in self.table:
                site = f.encrypt(row[0].encode()).decode("utf-8")
                password = f.encrypt(row[1].encode()).decode("utf-8")
                file.write(f"{site},{password}\n")

    def create_new_file(self, path):
        self.set_path_key(path, Fernet.generate_key().decode("utf-8"))
        self.write_existing_file()

        return self.key

    def show_password_file(self):
        self.read_existing_file()
        print(tabulate(self.table, headers=self.headers, tablefmt="outline"))

    def add_password(self, site, password):
        index = self.site_exists(site)
        if index >= 0:
            self.table[index][1] = password
        else:
            self.table.append([site, password])

        self.write_existing_file()

    def remove_password(self, site):
        index = self.site_exists(site)
        if index >= 0:
            self.table.pop(index)
            self.write_existing_file()
        else:
            raise ValueError("Site not found!")

    def delete_file(self):
        os.remove(self.path)

    def site_exists(self, site):
        for i in range(len(self.table)):
            if self.table[i][0] == site:
                return i
        return -1

    @classmethod
    def valid_key(cls, key):
        try:
            f = Fernet(key)
            return True
        except:
            return False

    @classmethod
    def key_matched(cls, path, key):
        try:
            f = Fernet(key)
            with open(path, "r") as file:
                site, password = file.readline().split(",")

            site = f.decrypt(site).decode("utf-8")
            password = f.decrypt(password).decode("utf-8")
        except:
            return False

        cls.set_path_key(cls, path, key)
        return site == "site" and password == "password"

    @staticmethod
    def generate_random_password(length, uppercase=False, lowercase=False, numbers=False, symbols=False):

        if length < 1:
            raise ValueError("Length can not be less than 1.")

        upper = list(string.ascii_uppercase)
        lower = list(string.ascii_lowercase)
        numbs = list(string.digits)
        symbs = list(string.punctuation)

        chars = []
        password = []

        if uppercase:
            chars += upper
            password.append(random.choice(upper))
        if lowercase:
            chars += lower
            password.append(random.choice(lower))
        if numbers:
            chars += numbs
            password.append(random.choice(numbs))
        if symbols:
            chars += symbs
            password.append(random.choice(symbs))

        remain = length - len(password)
        if remain < 1:
            random.shuffle(password)
            return "".join(password)[:length]

        random.shuffle(chars)

        for _ in range(remain):
            password.append(random.choice(chars))

        random.shuffle(password)
        return "".join(password)
