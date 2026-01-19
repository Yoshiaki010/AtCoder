#lv1
"""
N = int(input())
ans = 2 ** N - 2 * N
print(ans)
"""

#lv2
"""
def cal(x):
    lis_x = list(map(int,list(str(x))))
    next = 0
    for i in range(len(lis_x)):
        next += lis_x[i] * lis_x[i]
    return next

N = int(input())

next_int = 0
for _ in range(2):
    next_int = cal(N)

ans = "Unknow"
for _ in range(243):
    next_int = cal(next_int)

    if next_int == 1:
        ans = "Yes"
        break
    else:
        continue
else:
    ans = "No"

print(ans)
"""

#lv3
"""
"""


#lv4
"""
"""
