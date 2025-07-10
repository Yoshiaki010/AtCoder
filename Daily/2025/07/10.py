#lv2
"""
N = int(input())
a = set(list(map(int,input().split())))

ans = len(a)
print(ans)
"""
#lv2
"""
S = input()
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
start_pos = 0
fin_pos = 0
ans = 0
for i in range(25):
    for j in range(26):
        if S[j] == ABC[i]:
            start_pos = j
        elif S[j] == ABC[i + 1]:
            fin_pos = j
        else:
            continue
    ans += abs(start_pos - fin_pos)

print(ans)
"""

#lv3
"""
"""

#lv3
"""
"""
N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def cook_max(item):
    max_dish = 10 ** 6 + 1
    for i in range(N):
        if item[i] == 0:
            continue
        else:
            if Q[i] // item[i] < max_dish:
                max_dish = Q[i] // item[i]

    for i in range(N):
        Q[i] -= item[i] * max_dish

    return (max_dish)

A_max_dish = cook_max(A)
B_max_dish = cook_max(B)

ans = A_max_dish + B_max_dish
now_dish = ans
#print(now_dish,A_max_dish,B_max_dish)
for _ in range(A_max_dish):
    now_dish -= 1
    for i in range(N):
        Q[i] += A[i]
    
    B_max_dish = cook_max(B)
    now_dish += B_max_dish

    if ans < now_dish:
        ans = now_dish
    else:
        continue
    
print(ans)
#lv4
"""
"""
