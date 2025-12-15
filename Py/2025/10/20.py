#lv1
"""
"""

#lv2
"""
N, K = map(int,input().split())
S = input()

for i in range(N):
    S[i:K]
"""

#lv3 c
"""
Q = int(input())

open = 0
close = 0
s = []
ans = "Uknow"
for i in range(Q):
    q = input().split()
    if 0 < close:
        if q[0] == "1":
            close += 1
        else:
            close -= 1
    else:
        if q[0] == "1":
            c = q[1]
            if c == "(":
                s.append("(")
                open += 1
            else:
                if 0 < open:
                    s.append(")")
                    open -= 1
                else:
                    close += 1
        else:
            if s[-1] == "(":
                open -= 1
            else:
                open += 1
            s.pop()
    if open == 0 and close == 0:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
"""
#lv4 d
"""
"""
print(2 * (10 ** 8) * 0.5)
T = int(input())
for _ in range(T):
    c,d = map(int,input().split())
    print(c * 0.5)
