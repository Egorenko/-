def is_base():
    while True:
        n = input('Введите основание системы счисления.\n')
        if n.isdigit() == True:
            return int(n)
        else:
            print('Что-то пошло не так, повторите ввод.')

def is_num():
    s = input('Введите число для перевода.\n')
    n = list()
    for i in s:
        n.append(i)
    return n

def is_calculator(base, num):
    num = num[::-1]
    count = 0
    for i in range(len(num)):
        if num[i] in '1234567890':
            count += int(num[i]) * base ** i
        else:
            num[i] = ord(num[i]) - 55
            count += int(num[i]) * base ** i
    return count

def ten(base, num):
    num = ''.join(num)
    s = ''
    while int(num) >= base:
        count = (int(num) % base)
        if count > 9:
            if count == 10:
                s += 'A'
            elif count == 11:
                s += 'B'
            elif count == 12:
                s += 'C'
            elif count == 13:
                s += 'D'
            elif count == 14:
                s += 'E'
            else:
                s += 'F'
        else:
            s += str(count)
        num = int(num) // base
    s += str(num)
    return s[::-1]

print('Это калькулятор для перевода из любой системы счисления в десятичную и наоборот.')
while True:
    flag = input('Вам нужно перевести число?\n')
    if flag == 'да':
        base = is_base()
        num = is_num()
        key = input('Необходим перевод в десятичную или из нее? 1 - десятичная, 0 - из нее?\n')
        if key == 1:
            print(is_calculator(base, num))
        else:
            print(ten(base, num))
    else:
        print('До встречи!')
        break