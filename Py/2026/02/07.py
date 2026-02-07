#lvA
"""
N = input()
ans = "Uknow"
for i in range(len(N) - 1):
    if N[i] == N[i + 1]:
        continue
    else:
        ans = "No"
        break
else:
    ans = "Yes"
print(ans)
"""

#lvB
"""
"""
N,K = input().split()

def make(n, keta, s, c):
    for i in range(10):
        new = n * 10 + i
        if new <= int(N):
            if keta + 1 < len(N) and s + i < int(K):
               print("|call", new, keta + 1, s + i, c)
               re = make(new, keta + 1, s + i, c)
               c += re
               print("-", new, c, re)
               print()
            else:
                if s + i == int(K):
                    c += 1
                    print(new, s + i, "+1")
                else:
#                    print(new, s + i, "+0")
                    pass
    return c

ans = 0
for i in range(10):
    if i == int(K):
        ans += 1
    if i <= int(N[0]):
        if i != 0:
            print("call", i)
            re = make(i, 1, i, 0)
            ans += re
            print(re)

print(ans)
"""
if len(N) * 9 < int(K):
    ans = 0
else:
"""


#lvC
"""
"""

#lvD
"""
"""
