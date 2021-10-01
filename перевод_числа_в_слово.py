# объявление функции
def is_pangram(text):
    s = text.replace(' ', '').lower()
    alpha = [chr(a) for a in range(ord('a'), ord('z') + 1)]
    s = set(s)
    #print(len(s))
    #print(len(alpha))
    if len(s) == len(alpha):
        return True
    else:
        return False

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))