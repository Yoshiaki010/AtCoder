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

next = 1
ans = 0
for i in range(m):
    if x[i] > next:
        ans = -1
        break
    else:
        amari = next - x[i]
        next += a[i]
        rock = a[i] + amari
        ans -= ((amari+1) * amari) // 2
        ans += (rock * (rock-1)) // 2
if next - 1 != n:
    ans = -1
else:
    pass
print(ans)
