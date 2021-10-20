from random import *

digits = [int(i) for i in '0.1.2.3.4.5.6.7.8.9'.split('.')]
lowercase_letters = [i for i in 'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z'.split('.')]
uppercase_letters = [i for i in 'A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z'.split('.')]
punctuation = [i for i in '! # $ % & * + - = ? @ ^ _'.split(' ')]


def chars(dig, low, upper, punct, slo):
    chars = []
    if dig == 'да':
        chars += digits
    if low == 'да':
        chars += lowercase_letters
    if upper == 'да':
        chars += uppercase_letters
    if punct == 'да':
        chars += punctuation
    if slo == 'нет':
        for i in 'il1Lo0O':
            if i in chars:
                chars.remove(i)
    return chars

def password(lenght, chars):
    password = ''
    for _ in range(lenght):
        password += str(choice(chars))
    return password


n = input('Сколько паролей необходимо сгенерировать?\n')
for _ in range(int(n)):
    l = input('Длина пароля?\n')
    dig = input('Включать ли цифры?\n')
    low = input('Включать ли маленькие буквы?\n')
    upper = input('Включать ли большие буквы?\n')
    punct = input('Включать ли специальные знаки?\n')
    slo = input('Включать ли сложные символы: il1Lo0O?\n')
    chars = chars(dig, low, upper, punct, slo)
    print(password(int(l), chars))