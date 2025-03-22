#lv1
"""
n = int(input())
mid = 0
if n % 2 == 0:
    mid = 2
else:
    mid = 1
both_ends = "-"*((n-1)//2)

print(both_ends + "="*mid + both_ends)
"""
#lv2
"""
a = list(map(int,input().split()))
cards = [0 for _ in range(13)] 
x = 0
y = 0
for Ai in a:
    cards[Ai - 1] += 1
    if cards[Ai - 1] == 2:
        y += 1
    elif cards[Ai - 1] == 3:
        y -= 1
        x += 1

ans = "Unknow"
if x > 0 and y > 0 or x > 1:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""
#lv3
"""
n = int(input())
a = list(map(int,input().split()))
numbers = dict()
for i in range(n):
    if a[i] not in numbers:
        numbers[a[i]] = 1
    else:
        numbers[a[i]] += 1

peple = []
peple_num = 0
for i in range(n):
    if numbers[a[i]] == 1:
        peple.append([a[i],i + 1])
        peple_num += 1

if peple_num > 0:
    ans = sorted(peple, key=lambda x: x[0])[-1][1]
else:
    ans = -1
print(ans)
"""
#lv4
"""
"""
n,r,c = map(int,input().split())
s = input()
x = 0
y = 0

smoke = []
for i in range(n):
    if s[i] == "N":
        x -= 1
    elif s[i] == "W":
        y -= 1
    elif s[i] == "S":
        x += 1
    else:
        y += 1
    smoke.append([x,y])
print(x,y)
print(smoke)