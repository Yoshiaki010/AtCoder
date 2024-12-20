#lv1
"""
n,d = map(int,input().split())
s = input()
box = 0
ans = 0
for i in range(n):
    if s[i] == ".":
        ans += 1
    else:
        box += 1
if d < box:
    ans += d
else:
    ans += box
print(ans)
"""
#lv2
"""
n,d = map(int,input().split())
s = list(input())
eat = 0
for i in range(n):
    i += 1
    if eat == d:
        break
    else:
        if s[n-i] == "@":
            s[n-i] = "."
            eat += 1
        else:
            continue
print("".join(s))
"""
#lv3
"""
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

max = 10**6
judge = []
judgen = 0
eaters = dict()
for i in range(n):
    if a[i] < max:
        eaters[a[i]] = i + 1
        max = a[i]
        judge.append((a[i],0))
        judgen += 1
    else:
        continue

for i in range(m):
    judge.append((b[i],1,i))

judge.sort()

eater = -1
for i in range(judgen + m):
    if judge[i][1] == 0:
        eater = eaters[judge[i][0]]
        continue
    else:
        b[judge[i][2]] = eater

for i in range(m):
    print(b[i])
"""