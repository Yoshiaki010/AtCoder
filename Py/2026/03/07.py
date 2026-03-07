#lvA
"""
N,X = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N):
    if A[i] < X:
        X = A[i]
        print(1)
    else:
        print(0)
"""

#lvB
"""
N,M = map(int,input().split())
C = list(map(int,input().split()))

ans = 0
for _ in range(N):
    a,b = map(int,input().split())
    if C[a - 1] <= b:
        ans += C[a - 1]
        C[a - 1] = 0
    else:
        ans += b
        C[a - 1] -= b

print(ans)
"""

#lvC
"""
N,Q = map(int,input().split())
A = list(map(int,input().split()))

A_inBag = [1 for _ in range(N)]
A_sort_lis = soted([(A[i],i) for i in range(N)])

for _ in range(Q):
    k = int(input())
    b = list(map(int,input().split()))

    for i in range(k):
        A_inBag[b[i] - 1] = 0

    for i in range(k + 1):
        if A_inBag[A_sort_lis[i][1]] == 1:
            print(A_sort_lis[i][0])
            break
        else:
            continue

    for i in range(k):
        A_inBag[b[i] - 1] = 1
"""

#lvD
"""
"""
N = int(input())
A = list(map(int,input().split()))

tree = dict()
for i in range(N):
    tree[i + 1] = []

for _ in range(N - 1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

print(tree)

ans = [[] for _ in range(N)]
ans[0] = [A[0]]

now = 1
next = tree[now]
walked = {1}
while len(next) != 0:
    next_next = []

    for next_i in next:
        ans[next_i - 1] = [A[next_i - 1]] + ans[now - 1]

    now = next[0]
    next = next[1:]
    walked.add(now)

    for next_next_i in tree[now]:
        if next_next_i not in walked:
            next_next.append(next_next_i)
        else:
            continue

print(ans)
for i in range(N):
    set_lis = set(ans[i])
    print(set_lis, ans[i])
    if  len(set_lis) < len(ans[i]):
        print("Yes")
    else:
        print("No")