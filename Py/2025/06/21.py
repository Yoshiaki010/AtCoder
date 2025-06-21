#lv1
"""
P = input()
L = int(input())

if L <= len(P):
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""
#lv2
"""
N = int(input()) - 1
D = list(map(int,input().split()))

stationes = [0]
D_sum = 0
for i in range(N):
    D_sum += D[i]
    stationes.append(D_sum)

for i in range(N):
    for j in range(N - i):
        j += i + 1
        print(stationes[j] - stationes[i], end = " ")
    print()
"""
#lv3
"""
N,Q = map(int,input().split())
A = list(map(int,input().split()))
BWline = ["." for _ in range(N + 2)]

ans = 0
for i in range(Q):
    Ai = A[i] - 1
    mid = BWline[Ai]
    left = BWline[Ai - 1]
    right = BWline[Ai + 1]
    if left == mid and mid == right:
        ans += 1
    elif left != mid and left == right:
        ans -= 1
    else:
        pass
    if mid == "#":
        BWline[Ai] = "."
    else:
        BWline[Ai] = "#"
    print(ans)
"""
#lv4
"""
"""
N,Q = map(int,input().split())
ans = ""
pc = dict()
for i in range(N):
    pc[i + 1] = ""

#多分置き換えと文字列の長さがもんだい
for i in range(Q):
    query = input()
    if query[0] == "1":
        q,p = map(int,query.split())
        pc[p] = ans
    elif query[0] == "2":
        q,p,s = query.split()
        pc[int(p)] = "".join([pc[int(p)],s])
    else:
        q,p = map(int,query.split())
        ans = pc[p]
print(ans)