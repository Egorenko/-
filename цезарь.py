def language(lan):
    if lan == 'ru':
        alpha_lower = [chr(i) for i in range(ord('а'), ord('я') + 1)]
        alpha_upper = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
        max_key = 32
    else:
        alpha_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        alpha_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        max_key = 26
    return alpha_lower, alpha_upper, max_key

def key(inst):
    key = [int(i) for i in input('Введите сдвиг.\n').split()]
    if inst == 1:
        for i in range(len(key)):
            key[i] *= -1
    return key

def cezar(text, key, l):
    alpha_lower, alpha_upper, max_key = language(l)
    txt = ''
    for j in range(len(key)):
        for i in text:
            if i in alpha_lower:
                txt += chr(ord(alpha_lower[0]) + (ord(i) - ord(alpha_lower[0]) + key[j]) % max_key)
            elif i in alpha_upper:
                txt += chr(ord(alpha_upper[0]) + (ord(i) - ord(alpha_upper[0]) + key[j]) % max_key)
            else:
                txt += i
        txt += '\n'
    return txt


lan = input('Привет. На каком языке будем работать?\nru - русский, en - английский.\n')
ins = int(input('Что нужно сделать: 0 - зашифровать, 1 - дешифровать.\n'))
key = key(ins)
text = input('Введите текст.\n')
print(cezar(text, key, lan))

