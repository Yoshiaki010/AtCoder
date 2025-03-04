#lv3
"""
"""
n = int(input())
x = list(map(int,input().split()))

p = sum(x) // n
if 0 < sum(x) % n:
    p += 1

ans = 0
for i in range(n):
    ans += (x[i] - p) ** 2
print(ans)