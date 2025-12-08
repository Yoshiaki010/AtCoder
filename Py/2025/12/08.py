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
            print(l, r, now_sum)
            for i in range(r - l):
                print(i)
                if now_sum % A[i + l] == 0:
                    break
                else:
                    continue
            else:
                print("+")
                ans += 1
        else:
            continue
print(ans)

#lv3
"""
"""