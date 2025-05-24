#lv1
"""
A,B = map(int,input().split())

ans = 0
if (A / B) - (A // B) < (A // B + 1) - (A / B) :
    ans = A // B
else:
    ans = A // B + 1
print(ans)
"""
#lv2
"""
X,Y = map(int,input().split())
ans = 0
for i in range(6):
    i += 1
    for j in range(6):
        j += 1
        if X <= i + j or Y <= abs(i - j):
            ans += 1
        else:
            continue
print(ans / 36)
"""

#lv3
"""
#Memo 制限を解除する方法もある
import sys
sys.set_int_max_str_digits(0)

S = input()
N = len(S)
ans = 0
for i in range(N):
    one_place = int(S[N - i - 1])
    if ans % 10 == one_place:
        pass
    elif ans % 10 < one_place:
        ans += one_place - ans % 10
    else:
        ans += (10 - ans % 10) + one_place
ans += N
print(ans)
"""
#lv4

"""
"""