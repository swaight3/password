password = input("Введите пароль: ")


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(symboll.isdigit() for symboll in password)


def has_upper_letters(password):
    return any(symboll.isupper() for symboll in password)
   

def has_lower_letters(password):
    return any(symboll.islower() for symboll in password)


def has_symbols(password):
    return any(not symboll.isdigit() and not symboll.isalpha() for symboll in password)
    

all_checks = [is_very_long, has_digit, has_upper_letters, has_lower_letters, has_symbols]

score = 0

for check_function in all_checks:
    if check_function(password):
        score = score + 2

print("Рейтинг пароля:", score)

