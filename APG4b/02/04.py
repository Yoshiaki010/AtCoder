#EX17 - GameCompe
N,M = map(int,input().split())
table = [["-"]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int,input().split())
    table[a - 1][b - 1] = "o"
    table[b - 1][a - 1] = "x"

for i in range(N):
    print(*table[i])