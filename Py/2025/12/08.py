#lv1
"""
N = int(input())
ans = 0
for i in range(N):
    ans += i + 1
print(ans)
"""

#lv2
"""
N = int(input())
A = list(map(int,input().split()))

ruiseki = [0]
for i in range(N):
    ruiseki.append(ruiseki[i] + A[i])

ans = 0
for l in range(N):
    for r in range(N):
        if l <= r:
            now_sum = ruiseki[r + 1] - ruiseki[l]
            for i in range(r - l + 1):
                if now_sum % A[i + l] == 0:
                    break
            else:
                ans += 1
print(ans)
"""

#lv3
"""
N = int(input())
A = list(map(int,input().split()))

max_down_i = 1
ans = 0
for i in range(N):
    if i < max_down_i:
        ans += 1
    else:
        break

    if max_down_i < i + A[i]:
        max_down_i = i + A[i]

print(ans)
"""

#lv4
"""
"""
