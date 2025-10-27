#lv2
"""
cardes = [0 for i in range(13)]
A = list(map(int,input().split()))

for i in range(7):
    cardes[A[i] - 1] += 1
    
x = 0
y = 0
for i in range(13):
    if 2 < cardes[i]:
        x += 1
    elif 1 < cardes[i]:
        y += 1
    else:
        pass

ans = "Unknow"
if 1 < x or 0 < x and 0 < y:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""
#lv2
"""
H,W = map(int,input().split())
S = [input() for _ in range(H)]

pice_A = []
pice_B = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            if pice_A == []:
                pice_A = [i,j]
            else:
                pice_B = [i,j]
                break
        else:
            continue

ans = abs(pice_A[0] - pice_B[0]) + abs(pice_A[1] - pice_B[1])
print(ans)
"""
#lv3
"""
N,K = map(int,input().split())
next = 0
a = []
for i in range(N + 1):
    if 0 <= i and i < K:
        a.append(1)
        next += 1
    else:
        a.append(next)
        next = next * 2 - a[i - K]
        next %= 10 ** 9

print(a[N])
"""
#lv3
"""
"""

#lv4
"""
"""
