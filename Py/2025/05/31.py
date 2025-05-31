#lv1
"""
N,S = map(int,input().split())
T = list(map(int,input().split()))
wake_up = 0
ans = "Yes"
for i in range(N):
    if T[i] - wake_up < S + 0.5:
        wake_up = T[i]
        continue
    else:
        ans = "No"
        break
print(ans)
"""
#lv2
"""
N = int(input())
A = list(set(map(int,input().split())))

n = len(A)
A.sort()

print(n)
print(*A)
"""
#lv3
"""
N,M = map(int,input().split())
protect_wall = [0] * (N + 1)

for _ in range(M):
    L,R = map(int,input().split())
    protect_wall[L - 1] += 1
    protect_wall[R] -= 1

front = 0
protect_gun = []
for i in range(N):
    front += protect_wall[i]
    protect_gun.append( front )

print(protect_gun)
ans = min(protect_gun[1:])
print(ans)
"""

#lv4
"""
"""
T = int(input())
for _ in range(T):
    N = int(input())
    S = input()

    one_blockes = []
    block_num = 0
    block = 0
    if S[0] == "0":
        front_one = False
    else:
        front_one = True
    for i in range(N):
        if front_one:
            if S[i] == "1":
                block += 1
            else:
                one_blockes.append(block)
                block = 0
                block_num += 1
        else:
            if S[i] == "1":
                block += 1
                front_one = True
            else:
                continue
    else:
        one_blockes.append(block)
        block_num += 1
    print(S)
    print(one_blockes)
    max_block = max(one_blockes)
    ans = 0
    if 1 < block_num:
        for i in range(block_num):
            if one_blockes[i] < max_block:
                ans += one_blockes[i]
            else:
                continue
    else:
        pass
    print(ans)