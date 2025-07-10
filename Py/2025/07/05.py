#lv1
"""
N,M = map(int,input().split())
A = list(map(int,input().split()))

all = sum(A)
ans = "Unknow"
if all <= M:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""

#lv2
"""
N = int(input())
S = [input() for _ in range(N)]
all = set()

for i in range(N):
    for j in range(N - i):
        j += i
        if i == j:
            continue
        else:
            all.add(S[i]+S[j])
            all.add(S[j]+S[i])

all = list(all)
all.sort()
print(len(all))
"""
#lv3
"""
Q = int(input())

A = list()
a_Del = 0
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        T,C,X = q
        A.append([X,C])
    else:
        T,K = q
        ans = 0
        i = a_Del
        while 1 <= K:
            if A[i][1] <= K:
                ans += A[i][0] * A[i][1]
                K -= A[i][1]
                a_Del += 1
            else:
                ans += A[i][0] * K
                A[i][1] -= K
                K = 0
            i += 1
        print(ans)
"""
#v4
"""
"""
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    print(a)
    r = a[1] / a[0] 
    print(r)
    ans = "Uknow"
    for i in range(n - 1):
        print(a[i],a[i] * r,a[i + 1],a[i] * r == a[i + 1])
        if a[i] * r == a[i + 1]:
            continue
        else:
            ans = "No"
            break
    else:
        ans = "Yes"
    print(ans)