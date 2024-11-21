#lv1
"""
n = list(map(int,(input())))
n.sort()
num = [0,0,0]
for i in range(6):
    if 0 < n[i] and n[i] < 4:
        num[n[i]-1] += 1
    else:
        continue
if num == [1,2,3]:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""
#lv2
"""
s = input().split("|")
s = s[1:-1]

a = []
for i in range(len(s)):
    a.append(len(s[i]))
print(*a)
"""
#lv3
"""
"""
n,k = map(int,input().split())
s = input()
fast = list(s[0])
mid = []
target = []
last = []
onenum = 0
front = s[0]

for i in range(n-1):
    i += 1
    if s[i] == "0" and front == "1":
        onenum += 1
    if onenum < k-1:
        fast.append(s[i])
    elif onenum < k and s[i] != "1":
        mid.append(s[i])
    elif s[i] == "1" and onenum == k-1:
        target.append(s[i])
    else:
        last.append(s[i])
    front = s[i]

ans = fast + target + mid + last
ans = "".join(ans)
print(ans)
