# объявление функции
def is_password_good(password):
    is_len = False
    is_bid = False
    is_little = False
    is_digit = False
    count = 0
    
    if len(password) >= 8:
        is_len = True
    for i in password:
        if 65 <= ord(i) <= 90:
            is_bid = True
        if 97 <= ord(i) <= 122:
            is_little = True
        if i in '1234567890':
            is_digit = True
    
    if is_len == True:
        count += 1
    if is_bid == True:
        count += 1
    if is_little == True:
        count += 1
    if is_digit == True:
        count += 1
    if count == 4:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))