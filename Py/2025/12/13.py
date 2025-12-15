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

"""
#lv4
H,W = map(int,input().split())
S = [["#"] * (W + 2)]
for _ in range(H):
    S.append(list("#" + input() + "#"))
S.append(["#"] * (W + 2))

TP = dict()
for i in range(26):
    TP[chr(97 + i)] = []

for i in range(H + 2):
    for j in range(W + 2):
        if "a" <= S[i][j] <= "z":
            TP[S[i][j]].append((i,j))

walked = []
for _ in range(H + 2):
    walked.append([-1] * (W + 2))

nexts = [[1, 1, 0]]

walked[1][1] = 0
while 0 < len(nexts):
    next_nexts = []
    for next in nexts:
        i, j, m = next
        if S[i - 1][j] != "#" and walked[i - 1][j] == -1:
            next_nexts.append([i - 1, j, m + 1])
            walked[i - 1][j] = m + 1
        if S[i + 1][j] != "#" and walked[i + 1][j] == -1:
            next_nexts.append([i + 1, j, m + 1])
            walked[i + 1][j] = m + 1
        if S[i][j - 1] != "#" and walked[i][j - 1] == -1:
            next_nexts.append([i, j - 1, m + 1])
            walked[i][j - 1] = m + 1
        if S[i][j + 1] != "#" and walked[i][j + 1] == -1:
            next_nexts.append([i, j + 1, m + 1])
            walked[i][j + 1] = m + 1
        if S[i][j] != ".":
            for go in TP[S[i][j]]:
                if go != (i,j) and walked[go[0]][go[1]] == -1:
                    next_nexts.append([go[0], go[1], m + 1])
                    walked[go[0]][go[1]] = m + 1
            TP[S[i][j]] = []
    nexts = next_nexts

#for i in range(H + 2):
#    print(*walked[i])

ans = 0
if walked[H][W] != -1:
    ans = walked[H][W]
else:
    ans = -1
print(ans)
"""