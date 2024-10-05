#lv1
"""
s = input()
n = len(s)
ans = "Unknow"
if s[n-3:] == "san":
  ans = "Yes"
else:
  ans = "No"
print(ans)
"""

#lv2
"""
s = input()
t = input()

ans = -1
if s == t:
    ans = 0
else:
    if len(s) < len(t):
        n = len(s)
    else:
        n = len(t)
    for i in range(n):
        if s[i] != t[i]:
            ans = i + 1
            break
        else:
            continue
    else:
        ans = n + 1
print(ans)
"""

#lv3
"""
"""
n = int(input())
k = list(map(int,input().split()))

k.sort()

a = 0
b = 0
for i in range(n):
    if a + k[n-i-1] < b + k[n-i-1]:
        a += k[n-i-1]
    else:
        b += k[n-i-1]

ans = 0
if a < b:
    ans = b
else:
    ans = a
print(ans)