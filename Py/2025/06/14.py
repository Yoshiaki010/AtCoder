#lv1
"""
N = int(input())
A = list(map(int,input().split()))
K = int(input())

ans = 0
for i in range(N):
    if K <= A[i]:
        ans += 1
    else:
        continue
print(ans)
"""
#lv2
"""
N,Q = map(int,input().split())
X = list(map(int,input().split()))
box = []
for i in range(N):
    box.append([i,0])

ans = []
for i in range(Q):
    box = sorted(box, key=lambda x: x[1])
    min_box = box[0][0]
    box.sort()
    if X[i] == 0:
        box[min_box][1] += 1
        ans.append(min_box + 1)
    else:
        box[X[i] - 1][1] += 1
        ans.append(X[i])
print(*ans)
"""
#lv3
"""
def check(i,A,B):
    if i + A < B:
        i = i + A
    else:
        i = (i + A) % B
    return i

N,Q = map(int,input().split())
a = []
for i in range(N):
    a.append(i + 1)

K = 0
for _ in range(Q):
    q = input()
    if q[0] == "1":
        qi,p,x = map(int,q.split())
        p = check(p,K,N)
        a[p - 1] = x
    elif q[0] == "2":
        qi,p = map(int,q.split())
        p = check(p,K,N)
        print(a[p - 1])
    else:
        qi,k = map(int,q.split())
        K += k
"""