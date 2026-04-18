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
changer = list(F_dict[1])
changer_N = len(changer)
changedMan = {1}
print(changer,changer_N)
for _ in range(M):
    new_changer = set()
    new_changer_N = 0
    for m_i in changer:
        if ans < m_i:
            ans = m_i
        if m_i in changedMan:
            continue
        else:
            changedMan.add(m_i)
            new_changer.add(m_i)
            new_changer_N += 1
    changer = list(new_changer)
    changer_N = new_changer_N

    if changer_N == 0:
        break
    else:
        next_changer = set()
        next_changer_N = 0
        for m_i in changer:
            next_changer.update(F_dict[m_i])
            next_changer_N += F_dict_N[m_i - 1]

        changer = list(next_changer)
        changer_N = next_changer_N

print(ans)