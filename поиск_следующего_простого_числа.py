# объявление функции
def is_prime(num):
    if num > 1:
        delit = [i for i in range(2, num + 1) if num % i == 0]
        if len(delit) == 1:
            return True
        else:
            return False
    else:
        return False
    
def get_next_prime(num):
    for i in range(num + 1, (num + 1) * 2):
        if is_prime(i) == True:
            return i
        

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))