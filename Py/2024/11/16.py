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
import time
n,k = map(int,input().split())
s = list(input())

ans = 0

now = s[0]
start = time.perf_counter()
for i in range(5 * (10**5)):
    ans += 1
end = time.perf_counter()
print('{:.2f}'.format((end-start)/60))
print(ans)