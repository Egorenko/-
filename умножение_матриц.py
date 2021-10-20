def plus():
    s = input().split()
    A = []
    for _ in range(int(s[0])):
        A.append([int(i) for i in input().split()])
    #print(A)
    input()
    c = input().split()
    B = []
    for _ in range(int(c[0])):
        B.append([int(i) for i in input().split()])
    #print(B)
    C = [[0 for _ in range(int(c[1]))] for _ in range(int(s[0]))]
    #print(C)
    for i in range(int(s[0])):
        for j in range(int(c[1])):
            for r in range(int(s[1])):
                C[i][j] += A[i][r] * B[r][j]
        #print(C)
    for i in range(int(s[0])):
        for j in range(int(c[1])):
            C[i][j] = str(C[i][j])
    return C

print(*(' '.join(c) for c in plus()), sep='\n')