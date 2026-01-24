#A
"""
S = input()
ans = 0
for i in range(len(S)):
    if S[i] == "i" or S[i] == "j":
        ans += 1
print(ans)
"""

#lvB
"""
Q = int(input())

sound = 0
player = False

for i in range(Q):
    A = int(input())
    if A == 1:
        sound += 1
    elif A == 2:
        if 0 < sound:
            sound -= 1
        else:
            pass
    else:
        player = not player

    ans = "Uknow"
    if 3 <= sound and player:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
"""

#lvC
"""
N, M = map(int,input().split())
t = dict()
t_n = [0] * N
for i in range(N):
    t[i + 1] = set()

for _ in range(M):
    A,B = map(int,input().split())
    if B not in t[A]:
        t[A].add(B)
        t_n[A - 1] += 1
    if A not in t[B]:
        t[B].add(A)
        t_n[B - 1] += 1

for i in range(N):
    ans = 0
    p = (N - 1) - t_n[i]
    if 2 < p:
        ans = p * (p - 1) * (p - 2) // 6
    print(ans,end = " ")
"""

#lvD
"""
N,Q = map(int,input().split())
A = list(map(int,input().split()))
ruiseki = [0]

for i in range(N):
    ruiseki.append(ruiseki[i] + A[i])

for i in range(Q):
    q = input()
    if q[0] == "1":
        q,x = map(int,q.split())
        x -= 1
        a = A[x]
        b = A[x + 1]
        ruiseki[x + 1] += b - a
        A[x] = b
        A[x + 1] = a
    else:
        q,l,r = map(int,q.split())
        print(ruiseki[r] - ruiseki[l - 1])
"""

#lvE
"""
"""
