# PYTHON PASSWORD MANAGER
#### Video Demo:  <https://youtu.be/d_TZdy4cHaI?si=36QGxh_jYe96wa44>
#### Description:

This is the basic password manager application, entirely based on python having following features:
   - Generate a random password
   - Save your passwords with encryption
   - Read your passwords with the key


## Implementation

- The main project file keep prompting till user types 'q' or some error occurs
- Once getting a valid prompt it the calls the respective functions
- The match case executes one out of given prompt
- The 'login' specifies wheater or not user has successfully accessed his file
- Once logged in the options gets changed by calling `show_options()` by display_screen module


## Files structure

### 1. project.py
password_manager and display_screen module imported
```python
   pm = PasswordManager()
   dm = DisplayScreen()
```
  - ```dm.show_options()```: Displays options from display_screen module
  - ```pm.show_password_file()```: Only display passwords if user provide valid key

```login``` specifies wheather or not user has successfully opened the password file. It determines what options to display.

#### Functions
This file has 9 functions which describes:

- ```clear_screen()```: For useability purpose, making program interactive in terminal.
- ```clear_exit()```: Exits the program with provided argument
- ```get_prompt()```: Validates the command
- ```get_length()```: To make sure that length of password should not be less than 1
- ```get_bool()```: Converts user yes and no to True and False
- ```generate_password()```: Returns randomly generated password from PasswordManager
- ```file_exists()```: Whether or not file exists
- ```valid_key()```: Checks wheter given key is valid or not. (Prevent Error)
- ```key_matched()```: Compares file with the provided key


### 2. password_manager.py

**PasswordManager** initialzes `path`, `key`, `table`, and `headers`

- `set_path_key()`: It is called by other functions whenever needs to set path and key
- `read_existing_file()`: Restting table (passwords) and adding passwords again, everytime password file updated
- `write_existing_file()`: Writes the content of table to the file
- `create_new_file()`: Generate a key and writes encrpted site,password, which then gets validated if key decrpts it successfully.
- `show_password_file()`: Prints the password table from tabulate module
- `add_password()`: Adds or update password
- `remove_password()`: Removes password
- `delete_file()`: Deletes password file
- `site_exists()`: Return index of site if exists else -1

#### classmethod and staticmethod
To make it acceceble without initilizing PasswordManager

- `valid_key()`: Test for valid key
- `key_matched()`: Checks if key matched with the file
- `generate_random_password()`: Generate random password with specification


#### generate_random_password()
**syntax**

`PasswordManager.generate_random_password(length=n, uppercase=True, lowercase=True, numbers=True, symbols=True)`

- It make sures that all specified conditons are meet

```python
if uppercase:
    chars += upper
    password.append(random.choice(upper))
if lowercase:
   ...
```
`remain` defines the remaining length of password and effectively handles if user specifies all 4 conditions (uppercase, lowercase, numbers and symbols) but aspect only 3 or less length password


### 3. display_screen.py
It uses tabulate module to diplay options based on menu parameter (either "home" or "manage")
```
# If "home"

headers = ["    The Password Manager    "]
table = [
    ["(1) Generate a random password"],
    ["(2) Create a new password file"],
    ["(3) Open existing password file"],
    ["(q) Quit"]
]

# If "manage"

headers = ["    Manage your passwords    "]
table = [
    ["(1) Add / Update a password"],
    ["(2) Remove a password"],
    ["(3) Delete this file"],
    ["(q) Quit"]
]
```
