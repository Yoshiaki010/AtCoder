#lv1
"""
A,B,C,D = map(int,input().split())
ans = "Uknow"
if A <= C:
    if B <= D:
        ans = "No"
    else:
        ans = "Yes"
else:
    ans = "No"
print(ans)
"""

#lv2
"""
N,M = map(int,input().split())
S = []

for i in range(N):
    S.append(input())

all = set()
for i in range(N - M + 1):
    for j in range(N - M + 1):
        now = ""
        for k in range(M):
            now += S[i + k][j:j + M]
        all.add(now)

ans = len(list(all))
print(ans)
"""

#lv3
"""
"""
N,A,B = map(int,input().split())
S = input()

a_sigm = [0]
a_point = []
b_sigm = [0]
b_point = []

a_max = 0
b_max = 0
for i in range(N):
    if S[i] == "a":
        a_max += 1
        a_point.append(i)            

    else:
        b_max += 1
        b_point.append(i)

    a_sigm.append(a_max)
    b_sigm.append(b_max)

print(A,B)
print(a_sigm)
print(a_point)
print(b_sigm)
print(b_point)

a_dict = dict()
for i in range(N):
    