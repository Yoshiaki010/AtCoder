#lv1
"""
N = int(input())

ans = 0
for i in range(N):
    i += 1
    ans += (-1) ** i * (i ** 3)
print(ans)
"""

"""
#lv2
N = int(input())
A = list(map(int,input().split()))

can_change = 0
used_nums = [0] * N
for i in range(N):
    if A[i] == -1:
        can_change += 1
    else:
        used_nums[A[i] - 1] += 1

ans = "No"
can_use = []
for i in range(N):
    if used_nums[i] == 0:
        can_use.append(i + 1)
    elif 1 < used_nums[i]:
        ans = "No"
        break
    else:
        continue
else:
    ans = "Yes"

print(ans)

if ans == "Yes":
    ans_array = []
    point = 0
    for i in range(N):
        if A[i] == -1:
            ans_array.append(can_use[point])
            point += 1
        else:
            ans_array.append(A[i])
    print(*ans_array)
else:
    pass
"""

#lv3
N,Q = map(int,input().split())
A = list(map(int,input().split()))

t = 0
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        q,c = query
        t += c
    else:
        q,l,r = query
        l -= 1
        r -= 1
        print(*A[l + t : r + t + 1] + A[0 : (r + t) - N + 1])
