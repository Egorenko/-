from random import randint

def choice(text):
    input(f'Задай мне свой вопрос, {name}.\n')
    answer = randint(0, 20)
    return text[answer]

answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
print('Привет, мир. Я магический шар, и я знаю ответы на все ваши вопросы. Ну или почти на все.')
name = input('А как зовут тебя?\n')
print(f'Приятно познакомиться, {name}.')
while True:
    print('У тебя есть вопросы ко мне?')
    flag = input()
    if flag == 'да':
        print(choice(answers))
    else:
        print(f'До новый встреч, {name}!')
        break
