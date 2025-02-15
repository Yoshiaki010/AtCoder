#lv1
"""
a1,a2,a3 = map(int,input().split())

ans= "Unknow"

if a1 * a2 == a3:
  ans = "Yes"
elif a2 * a3 == a1:
  ans = "Yes"
elif a1 * a3 == a2:
  ans = "Yes"
else:
  ans = "No"

print(ans)
"""

#lv2
"""
n,m = map(int,input().split())
a = list(map(int,input().split()))
a = set(a)

c = 0
ans = []

for i in range(n):
  i += 1
  if i not in a:
    c += 1
    ans.append(i)
  else:
    continue

print(c)
print(*ans)
"""
#lv3
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

ans = []
for i in range(n):
    ans += [(q[i],q[p[i]-1])]

ans = sorted(ans, key=lambda x: x[0])

for i in range(n):
    print(ans[i][1], end = " ")
