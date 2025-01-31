def check_password(password):
    if len(password) < 8:
        print('Пароль должен быть не менее 8 символов')
    upper, lower, digit = False, False, False
    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True

    if not upper:
        print('Пароль должен содержать хотя бы одну заглавную букву')
    if not lower:
        print('Пароль должен содержать хотя бы одну строчную букву')
    if not digit:
        print('Пароль должен содержать хотя бы одну цифру')
password = input('Введите пароль:')