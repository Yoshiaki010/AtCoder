#lv1
"""
ans = 0
X = float(input())
if X < 37.5:
    ans = 3
elif X < 38.0:
    ans = 2
else:
    ans = 1
print(ans)
"""
#lv2
"""
s = input()
n = len(s)
ans = 0
for i in range(n):
    if (i + ans + 1) % 2 != 0:
        if s[i] == "i":
            continue
        else:
            ans += 1
    else:
        if s[i] == "o":
            continue
        else:
            ans += 1
else:
    if s[-1] == "i":
        ans += 1
print(ans)
"""
#lv3
"""
n = int(input())
a = list(map(int,input().split()))

left = 0
right = 0
left_numberdict = dict()
right_numberdict = dict()
for i in range(n):
    left_numberdict[a[i]] = 0
    right_numberdict[a[i]] = 0

for i in range(n):
    if right_numberdict[a[i]] < 1:
        right += 1
    right_numberdict[a[i]] += 1

ans = left + right
for i in range(n-1):
    if left_numberdict[a[i]] < 1:
        left += 1
    left_numberdict[a[i]] += 1
    right_numberdict[a[i]] -= 1
    if right_numberdict[a[i]] < 1:
        right -= 1
    if ans < left + right:        
        ans = left + right
print(ans)
"""
#lv4
"""
"""
