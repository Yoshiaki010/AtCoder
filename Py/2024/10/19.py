#lv1
"""
n,c = map(int,input().split())
t = list(map(int,input().split()))
gettime = t[0]
ans = 1
for i in range(n-1):
    if t[i+1] - gettime < c:
        continue
    else:
        gettime = t[i+1]
        ans += 1
print(ans)
"""
"""
#lv2
n,q = map(int,input().split())
left,right = [1,2]
ans = 0
for _ in range(q):
    h,t = input().split()
    t = int(t)
    if h == "R":
        move = right
        block = left
        right = t
    else:
        move = left
        block = right
        left = t
    rote = 0
    wrongrote = False
    for i in range(n):
        rote += 1
        if move == 1:
            move = n
        else:
            move -= 1
        if move == block:
            wrongrote = True
        else:
            if move == t:
                break
            else:
                continue
    if wrongrote:
        ans += n - rote
    else:
        ans += rote
        continue
print(ans)
"""
#lv3
"""
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

ans = 0
big = 0
okbox = 0
for i in range(n):
    if okbox == n-1:
        ans = a[i]
        break
    else:
        if a[i] < b[big] + 1:
            big += 1
            okbox += 1
        else:
            if ans < a[i]:
                ans = a[i]
            else:
                continue

if okbox == n-1:
    print(ans)
else:
    print(-1)
"""
#lv4
"""
"""
