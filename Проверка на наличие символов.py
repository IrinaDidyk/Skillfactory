def is_valid_email(email):
    results = {char: email.count(char)}
    for char in is_valid_email:
        dog_count = input_dog.count('@')
        results['@'] = dog_count
        return results
    if results > 0:
        return True
    else:
        return False
    users_input = input("Введите email: ")
    result = is_valid_email(users_input)
def is_valid_email(email):
    if '@' in email:
        return True
    else:
        return False
def is_valid_email(email):
    if '.' in email:
        return True
    else:
        return False
    if ' ' in email:
        return False
    else:
        return True