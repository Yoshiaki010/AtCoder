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
n,m = map(int,input().split())
s = []
for i in range(n):
    s.append(input())

t = []
for i in range(m):
    t.append(input())

ans = []
judge = "No"
for i in range(n-m+1):
    for j in range(n-m+1):
        if s[i][j] == t[0][0]:
            for k in range(m):
                for l in range(m):
                    if s[i+k][j+l] == t[k][l]:
                        continue
                    else:
                        judge = "No"
                        break
                else:
                    continue
                break
            else:
                judge = "Yes"
                ans = [i+1,j+1]
        else:
            judge = "No"
        if judge == "Yes":
            break
        else:
            continue
print(*ans)
"""
#lv3
"""
N,Q = map(int,input().split())
nest = [1 for _ in range(N)]
bird = [i+1 for i in range(N)]

ans = 0
for i in range(Q):
    query = input()
    if query[0] == "1":
        n,p,h = map(int,query.split())
        if nest[bird[p-1]-1] == 2:
            ans -= 1
        if nest[h-1] == 1:
            ans += 1
        nest[bird[p-1]-1] -= 1
        bird[p-1] = h
        nest[bird[p-1]-1] += 1
    else:
        print(ans)
"""
