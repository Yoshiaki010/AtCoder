#lv1
"""
N,L,R = map(int,input().split())
S = input()

ans = "Uknow"
for i in range(L,R + 1):
    if S[i - 1] == "o":
        continue
    else:
        ans = "No"
        break
else:
    ans = "Yes"
print(ans)
"""
#lv2
"""
S = input()
N = len(S)

t = []
before_o = False
mid_hash = False
for i in range(N):
    if S[i] == "#":
        t.append("#")
        if 0 < i and i < N - 1 and before_o:
            mid_hash = True
    else:
        if not before_o:
            t.append("o")
            before_o = True
        else:
            if mid_hash:
                t.append("o")
                mid_hash = False
            else:
                t.append(".")
print("".join(t))
"""

#lv3
"""
"""
