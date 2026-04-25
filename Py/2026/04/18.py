#LvA
"""
L,R = map(int,input().split())
ans = (R - L) + 1
print(ans)
"""
#LvB
"""
N,M = map(int,input().split())
F = list(map(int,input().split()))

clo = [0]* M
for i in range(N):
    clo[F[i] - 1] += 1

ans1 = "Uknow"
for i in range(M):
    if 1 < clo[i]:
        ans1 = "No"
        break
    else:
        continue
else:
    ans1 = "Yes"

ans2 = "Uknow"
for i in range(M):
    if clo[i] < 1:
        ans2 = "No"
        break
    else:
        continue
else:
    ans2 = "Yes"

print(ans1)
print(ans2)
"""

#LvC
"""
"""
N,M = map(int,input().split())
F = [tuple(map(int,input().split())) for _ in range(M)]

F_dict = dict()
F_dict_N = [0] * N
for i in range(N):
    F_dict[i + 1] = set()

for i in range(M):
    a,b = F[i]
    F_dict[a].add(b)
    F_dict_N[a - 1] += 1
print(F_dict,F_dict_N)

ans = 1

print(ans)