def game_random(n):
    print(f'{name}, введи число от 1 до 100. ')
    while True:
        user_num = int(input())
        if user_num > n:
            print('Слишком много, попробуй еще!')
        elif user_num < n:
            print('Слишком мало, попробуй еще!')
        else:
            return 'В точку! Поздравляю, ты угадал!'


from random import randint
print('Игра "Угадай число"!')
name = input('Привет, как тебя зовут?\n')
while True:
    flag = input(f'{name}, хочешь сыграть?\n')
    if flag == 'да':
        num = randint(1, 100)
        print(game_random(num))
    else:
        print(f'До встречи, {name}!')
        break
