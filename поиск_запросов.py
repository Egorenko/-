n = int(input())
list1 = list()
for _ in range(n):
    word = input()
    list1.append(word)
k = int(input())
list2 = list()
for _ in range(k):
    key = input()
    list2.append(key)
list3 = list()
for i in list1:
    count = 0
    for j in list2:
        if j.lower() in i.lower():
            count += 1
    if count == k:
        list3.append(i)
print(*list3, sep='\n')
