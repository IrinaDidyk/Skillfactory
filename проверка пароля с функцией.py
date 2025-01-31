def is_valid_password(password, min_length=8, require_upper=True, require_lower=True, require_digit=True):
    if len(password) < 8:
        return False
    min_length = len
    upper, lower, digit = False, False, False
    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True

    if not upper:
        return False
    if not lower:
        return False
    if not digit:
        return False
password = input('Введите пароль:')