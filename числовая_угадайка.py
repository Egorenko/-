def game_random(n):
    print(f'{name}, введи число от 1 до {gran}. ')
    count = 0
    while True:
        user_num = is_valid(input())
        if user_num == False:
            print(f'Кажется, ты ошибся, {name}. Повтори ввод.')
        elif user_num > n:
            count += 1
            print('Слишком много, попробуй еще!')
        elif user_num < n:
            count += 1
            print('Слишком мало, попробуй еще!')
        else:
            count += 1
            return f'В точку, {name}! Поздравляю, ты угадал. Количество попыток: {count}!'

def is_gran():
    while True:
        print(f'Введи правую границу, {name}.')
        n = input()
        if n.isdigit() == True:
            return int(n)
        else:
            print(f'Кажется, ты ошибся, {name}. Повтори ввод.')

def is_valid(text):
    if text.isdigit() == True:
        if 1 <= int(text) <= 100:
            return int(text)
        else: 
            return False
    else:
        return False

from random import randint
print('Игра "Угадай число"!')
name = input('Привет, как тебя зовут?\n')
while True:
    flag = input(f'{name}, хочешь сыграть?\n')
    if flag == 'да':
        gran = is_gran()
        num = randint(1, gran + 1)
        print(game_random(num))
    else:
        print(f'До встречи, {name}!')
        break
