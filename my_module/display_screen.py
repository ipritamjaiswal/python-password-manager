from tabulate import tabulate


class DisplayScreen:

    @staticmethod
    def create_table(headers, table):
        return tabulate(table, headers, tablefmt="grid")

    @classmethod
    def show_options(cls, menu):
        headers = ["    The Password Manager    "]
        table = [
            ["(1) Generate a random password"],
            ["(2) Create a new password file"],
            ["(3) Open existing password file"],
            ["(q) Quit"]
        ]

        if menu == "manage":
            headers = ["    Manage your passwords    "]
            table = [
                ["(1) Add / Update a password"],
                ["(2) Remove a password"],
                ["(3) Delete this file"],
                ["(q) Quit"]
            ]

        print(cls.create_table(headers, table))
