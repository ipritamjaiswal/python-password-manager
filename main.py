from my_module.password_manager import PasswordManager
from my_module.display_screen import DisplayScreen
from sys import exit
import os


def main():
    pm = PasswordManager()
    ds = DisplayScreen()
    login = False

    clear_screen()

    '''
    Keep the program running till Quit or error
    '''
    while True:
        ds.show_options("manage" if login else "home")
        pm.show_password_file() if login else print(end="")
        prompt = get_prompt("Prompt: ")
        if prompt == 'q':
            clear_exit("Thank You!")

        '''
        If user provide correct file and key
        Decrypted: File successfully matched with key
        '''
        if login:

            match prompt:
                # Add or Update a password
                case "1":
                    site = input("Enter site name: ")
                    password = input("Enter your password: ")
                    pm.add_password(site, password)

                # Remove a password
                case "2":
                    site = input("Enter site name: ")
                    clear_screen()
                    try:
                        pm.remove_password(site)
                    except ValueError:
                        print("Site not found!")

                # Delete this password file
                case "3":
                    sure = get_bool("Are you sure (y/n)? ")
                    clear_screen()
                    if sure:
                        pm.delete_file()
                        clear_exit("File deleted successfully.")

        else:

            match prompt:
                # Generate a random password
                case "1":
                    length = get_length("Enter the length of password: ")
                    upper = get_bool("Include uppercase (y/n)? ")
                    lower = get_bool("Include lowercase (y/n)? ")
                    numbs = get_bool("Include numbers (y/n)? ")
                    symbs = get_bool("Include symbols (y/n)? ")

                    if not upper and not lower and not numbs and not symbs:
                        clear_screen()
                        print("You must choose an case to include in password.")
                        continue

                    password = generate_password(length, upper, lower, numbs, symbs)
                    clear_screen()
                    print(f"Your password is: {password}")

                # Create a new password file
                case "2":
                    path = input("Enter filename without extension: ")
                    if file_exists(path):
                        clear_exit("File already exits!")

                    try:
                        key = pm.create_new_file(path + ".txt")
                    except:
                        clear_exit("Something went wrong.")

                    with open(path + "_key.txt", "w") as file:
                        file.write(key)

                    print(f"Your file and key has been saved successfully.\nYour key is: {key}")

                # Authenticate to Open existing password file
                case "3":
                    path = input("Enter filename without extension: ")
                    if not file_exists(path):
                        clear_exit("File does not exits!")

                    key = input("Enter your key: ")
                    if not valid_key(key):
                        clear_exit("Invalid Key!")
                    elif not key_matched(path, key):
                        clear_exit("Entered key was wrong.")

                    pm.set_path_key(path + ".txt", key)
                    login = True
                    clear_screen()
                    print("Success")


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def clear_exit(label=""):
    exit(label)


def get_prompt(label=""):
    while True:
        cmd = input(label).lower()
        if cmd in ['1', '2', '3', 'q']:
            clear_screen()
            return cmd


def get_length(label=""):
    while True:
        try:
            n = int(input(label))
            if n < 1:
                raise ValueError
            return n
        except ValueError:
            pass


def get_bool(label=""):
    while True:
        ans = input(label).lower()
        if ans == 'y':
            return True
        elif ans == 'n':
            return False


def generate_password(length=15, upper=True, lower=True, numbs=True, symbs=True):
    return PasswordManager.generate_random_password(length, upper, lower, numbs, symbs)


def file_exists(path):
    return os.path.exists(path + ".txt")


def valid_key(key):
    return PasswordManager.valid_key(key)


def key_matched(path, key):
    return PasswordManager.key_matched(path + ".txt", key)


if __name__ == "__main__":
    main()
