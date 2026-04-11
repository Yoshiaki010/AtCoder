#lvA
"""
N = int(input())
S = input()

ans = []
head = "Unknow"
if S[0] == "o":
    head = True
else:
    head = False

for i in range(N):
    if S[i] == "o" and head:
        continue
    else:
        head = False
        ans.append(S[i])

print("".join(ans))
"""

#lvB
"""
T,X = map(int,input().split())
A = list(map(int,input().split()))

t = 0
front_A = 0
for i in range(T + 1):
    if X <= abs(front_A - A[i]):
        front_A = A[i]
        print(f"{t} {front_A}")
    t += 1
"""

#lvC
"""
"""

