#lvA
"""
S = input()
print(S + "s")
"""

#lvB
"""
N,K = map(int,input().split())
ans = 0
r = 0

for i in range(10**5):
    r += N + i
    if K <= r:
        break
    else:
        ans += 1
print(ans)
"""

#lvC
"""
N,T = map(int,input().split())
A = list(map(int,input().split()))
A.append(T)

t = 0
ans = 0
for i in range(N + 1):
    if A[i] > t:
        ans += A[i] - t
        t = A[i] + 100

print(ans)
"""

#lvD
"""
"""
