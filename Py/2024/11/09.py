#lv1
"""
a,b,c = map(int,input())
print(b*100+c*10+a,c*100+a*10+b)
"""
#lv2
"""
n,k = map(int,input().split())
s = input()
oks = []
ok = 0
for i in range(n):
    if s[i] == "O":
        ok += 1
    else:
        if ok > k - 1:
            oks.append(ok)
        else:
            pass
        ok = 0
else:
    if ok > k - 1:
        oks.append(ok)
    else:
        pass

ans = 0
okn = len(oks)
for i in range(okn):
    ans += oks[i]//k
print(ans)
"""
#lv3
"""
"""
n,m = map(int,input().split())
x = list(map(int,input().split()))
a = list(map(int,input().split()))

box = [(x[i],a[i]) for i in range(m)]

box.sort()
s = box[1][1] - 1
k = (box[1][0] - box[0][0]) -1
amari = 0

ans = 0
for i in range(m-1):
    s = box[i][1] - 1 + amari
    k = (box[i + 1][0] - box[i][0]) -1
    amari = s - k
    ans += k * (k + 1) // 2
    ans += (s - k) * (k + 1)
amari += box[-1][1] -1
if amari == n - box[-1][0]:
    ans += amari * (amari + 1) // 2
else:
    ans = -1
print(ans)
