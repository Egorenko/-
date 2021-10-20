s = [i for i in input().split(' ')]
count_l = list()
for w in s:
    count = 0
    for c in w:
        if c.lower() in 'abcdefghijklmnopqrstuvwxyz':
            count += 1
    count_l.append(count)

for i in range(len(s)):
    a = ''
    for j in range(len(s[i])):
        if s[i][j].lower() in 'abcdefghijklmnopqrstuvwxyz':
            #маленькая буква
            if s[i][j].lower() == s[i][j]:
                a = s[i][j].replace(s[i][j], chr((ord(s[i][j]) - ord('a') + count_l[i]) % 26 + ord('a')))
                s[i] = s[i][:j] + a + s[i][j + 1:]
                #большая буква
            else:
                a = s[i][j].replace(s[i][j], chr((ord(s[i][j]) - ord('A') + count_l[i]) % 26 + ord('A')))
                s[i] = s[i][:j] + a + s[i][j + 1:]
print(' '.join(s))
