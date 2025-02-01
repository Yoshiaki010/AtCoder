#lv1
"""
d = input()
ans = ""
for i in range(len(d)):
    if d[i] == "N":
        ans += "S"
    elif d[i] == "S":
        ans += "N"
    elif d[i] == "E":
        ans += "W"
    else:
        ans += "E"
print(ans)
"""
#lv2
"""
"""
n,m = map(int,input().split())
s = []
for i in range(n):
    s.append(input())

t = []
for i in range(m):
    t.append(input())

ans = []
for i in range(n-1):
    for j in range(n-1):
        if s[i][j] == t[0][0]:
            for ti in range(m):
                for tj in range(m):
                    if s[i+ti][j+tj] == t[ti][tj]:
                        continue
                    else:
                        break
                else:
                    continue
                break
            else:
                ans = [i+1,j+1]
                break
print(*ans)
#lv3
"""
"""
