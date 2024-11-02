#lv1
"""
a = list(map(int,input().split()))
n = len(a)
color = []
ans = 0
for i in range(n):
    if a[i] not in color:
        color.append(a[i])
    else:
        ans += 1
        color.remove(a[i])
print(ans)
"""

#lv2
"""
n = int(input())
correctday = dict()
for i in range(n):
    q,r = map(int,input().split())
    correctday[i + 1] = [q,r]

query = int(input())
for i in range(query):
    t,d = map(int,input().split())
    q,r = correctday[t]
    ans = d
    if (d % q) < r + 1:
        ans += r - (d % q)
    else:
        ans += q - ((d % q) - r)
    print(ans)
"""

#lv3
"""
n = int(input())
a = list(map(int,input().split()))
seta = list(set(a))
kinds = len(seta)
number = dict()
for i in range(kinds):
    number[seta[i]] = [0,[]]

for i in range(n):
    number[a[i]][1].append(i)

b = []
for i in range(n):
    fastpos = number[a[i]][1][number[a[i]][0]]
    if fastpos == i:
        b.append(-1)
    else:
        b.append(fastpos + 1)
        number[a[i]][0] += 1
print(*b)
"""
#lv4
"""
"""
