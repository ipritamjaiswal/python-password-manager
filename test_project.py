from project import generate_password, file_exists, valid_key, key_matched


def main():
    test_generate_password()
    test_file_exists()
    test_valid_key()
    test_key_matched()


def test_generate_password():
    password1 = generate_password(10)
    password2 = generate_password(upper=False, lower=False, numbs=True, symbs=False)
    password3 = generate_password(upper=True, lower=True, numbs=True, symbs=False)
    assert len(password1) == 10
    assert password2.isdigit() == True
    assert password3.isalnum() == True


def test_file_exists():
    assert file_exists("secret") == True
    assert file_exists("new_name") == False


def test_valid_key():
    assert valid_key("24E-1WvrDRQ2V217HULxzpWoIAtKgZIRXzhpeEFC5os=") == True
    assert valid_key("6883h-jeihd833=") == False


def test_key_matched():
    assert key_matched("secret", "FWteckj3ilKqIrA08pBJknKQNajvp_aWIFFh8edA9OI=") == True
    assert key_matched("secret", "14E-1WvrDRQ2V217HULxzpWoIAtKgZIRXzhpeEFC5os=") == False


if __name__ == "__main__":
    main()
