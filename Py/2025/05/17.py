# lv1
"""
A,B,C,D = map(int,input().split())

Outtime = A * 60 + B
Acttime = C * 60 + D
ans = "Unknow"
if Acttime < Outtime:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""
# lv2
"""
N,K = map(int,input().split())
A = list(map(int,input().split()))

ans = 1
for i in range(N):
    ans *= A[i]
    if K < len(str(ans)):
        ans = 1
    else:
        continue
print(ans)
"""
# lv3
"""
"""
N = int(input())
p = list(map(int,input().split()))

start_pos = [0,[]]
big_pos = [0,[]]
small_pos = [0,[]]

tf_pos = [0]

for i in range(N - 2):
    i += 1
    if p[i - 1] < p[i]:
        start_pos[1].append(i)
        start_pos[0] += 1
        if p[i] < p[i + 1]:
            tf_pos.append(0)
            continue
        else:
            big_pos[1].append(i)
            big_pos[0] += 1
            tf_pos.append(1)
    else:
        if p[i] < p[i + 1]:
            small_pos[1].append(i)
            small_pos[0] += 1
            tf_pos.append(2)
        else:
            tf_pos.append(-1)
            continue
tf_pos.append(0)
print(p)
print(start_pos,big_pos,small_pos,tf_pos)
"""
"""
