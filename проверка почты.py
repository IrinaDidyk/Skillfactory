import time

# Функция для проверки почты
def is_valid_email(email):
    # Фиктивно замедляем функцию
    time.sleep(2)

    if email.count("@") != 1:
        return False
    local_part, domain_part = email.split("@")
    if not local_part or not domain_part:
        return False
    if domain_part.count(".") != 1:
        return False

    return True