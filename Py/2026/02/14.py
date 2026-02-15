#lvA
"""
S = input()

ans = "Unknow"
if S[0] == S[-1]:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""

#lvB
"""
N = int(input())
S = []

m = 0
for _ in range(N):
    Si = input()
    if m < len(Si):
        m = len(Si)
    else:
        pass
    S.append(Si)

for i in range(N):
    t = S[i]
    if len(S[i]) < m:
        k = (m - len(S[i])) // 2
        t = "." * k + S[i] + "." * k
    else:
        pass
    print(t)
"""

#lvC
"""
N = int(input())
A = list(map(int,input().split()))

dis_loop = [0 for _ in range(N)]

for i in range(N):
    back_i = N - i - 1

    if A[back_i] == N - i:
        dis_loop[back_i] = N - i
    else:
        dis_loop[back_i] = dis_loop[A[back_i] - 1]

print(*dis_loop)
"""
