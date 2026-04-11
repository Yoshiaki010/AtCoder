#LvA
"""
target_day = {(1,7),(3,3),(5,5),(7,7),(9,9)}

M,D = map(int,input().split())

ans = "Unknow"
if (M,D) in target_day:
    ans = "Yes"
else:
    ans = "No"

print(ans)
"""

#lvB
"""
H,W = map(int, input().split())

Canvas = ["#" * W]
for _ in range(H - 2):
    Canvas.append("#" + "." * (W - 2) + "#")

Canvas.append("#" * W)

for i in range(H):
    print(Canvas[i])
"""

#lvc
"""

"""
N = int(input())
bone_rule = []

for _ in range(N):
    A,B = map(int,input().split())
    bone_rule.append((A,B))

char_dict = [set() for _ in range(10)]

M = int(input())
S = []
for _ in range(M):
    s = input()
    len_s = len(s)
    S.append(s)
    for i in range(len_s):
        char_dict[len_s].add(s[i])

for i in range(M):
    s = S[i]
    len_s = len(s)
    ans = "Unknow"
    if len_s == N:
        for j in range(len_s):
            A,B = bone_rule[j]
            if s[j] in char_dict[A]:
                continue
            else:
                ans = "No"
                break
        else:
            ans = "Yes"
    else:
        ans = "No"
    print(ans)