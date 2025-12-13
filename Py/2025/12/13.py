#lv1
"""
N = int(input())
S = input()
diff = N - len(S)
ans = "o" * diff + S
print(ans)
"""

#lv2
"""
N = int(input())
a = []
for _ in range(N):
    a.append([0] * N)

r = 0
c = (N - 1) // 2
k = 1
a[r][c] = k

for i in range(N * N - 1):
    if a[(r - 1) % N][(c + 1) % N] == 0:
        a[(r - 1) % N][(c + 1) % N] = k + 1
        r = (r - 1) % N
        c = (c + 1) % N
    else:
        a[(r + 1) % N][c] = k + 1
        r = (r + 1) % N
    k += 1

for i in range(N):
    print(*a[i])
"""

#lv3
"""
N, M = map(int,input().split())

block = set()

ans = 0
for _ in range(M):
    r,c = map(int,input().split())
    if (r,c) not in block and (r + 1, c) not in block and (r, c + 1) not in block and (r + 1, c + 1) not in block:
        block.add((r, c))
        block.add((r + 1, c))
        block.add((r, c + 1))
        block.add((r + 1, c + 1))
        ans += 1
print(ans)
"""

#lv4
H,W = map(int,input().split())
S = []
for i in range(H):
    S.append(list(input()))

TP = dict()
for i in range(26):
    TP[chr(97 + i)] = []

for i in range(H):
    for j in range(W):
        if "a" <= S[i][j] <= "z":
            TP[S[i][j]].append((i,j))

print(TP)

def move(i, j, k):
    print(i,j,"=",S[i][j])

    if i == H and j == W:
        return k

    if S[i][j] == ".":
        S[i][j] = "#"
        #up
        if -1 < i - 1:
            k = move(i + 1, j, k + 1)
        #down
        if i + 1 < H:
            k = move(i - 1, j - 1, k + 1)
        #right
        if j + 1 < W:
            k = move(i, j + 1, k + 1)
        #left
        if -1 < j - 1:
            k =  move(i, j - 1, k + 1)
           
    return k

for i in range(H):
    print(*S[i])

ans = move(0,0,0)

for i in range(H):
    print(*S[i])

if ans == 0:
    ans = -1

print(ans)
"""
    elif "a" <= S[i][j] <= "z":
            go = TP[S[i][j]]
            new_TP = []
            for i in range(len(go)):
                if go[i] != (i,j):
                    print("TP!")
                    return 0 + move(*go[i], k + 1)                
"""
