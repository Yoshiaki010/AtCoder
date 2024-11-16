#lv1
"""
n,k = map(int,input().split())
a = list(map(int,input().split()))
print(*a[-k:],*a[:n-k])
"""

#lv2
"""
"""
n = int(input())
a = list(map(int,input().split()))

ans = 0
while 1 < n:
    ans += 1
    a.sort(reverse=True)
    a[0] -=1
    a[1] -=1
    if a[0] < 1:
        n -= 1
    else:
        pass
    if a[1] < 1:
        n -= 1
    else:
        pass
print(ans)
#lv3
"""
"""
