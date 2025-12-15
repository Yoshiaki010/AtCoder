#DP1
"""
N = int(input())
h = list(map(int,input().split()))

cost = [0, abs(h[0] - h[1])]
nc1 = 0
nc2 = 0

for i in range(N - 2):
    now = i + 2
    nc1 = cost[now - 2] + abs(h[now] - h[now - 2])
    nc2 = cost[now - 1] + abs(h[now] - h[now - 1])
    if nc1 < nc2:
        cost.append(nc1)
    else:
        cost.append(nc2)

print(cost[-1])
"""

#DP2

"""
"""
N,K = map(int,input().split())
h = list(map(int,input().split()))

cost = [0]

print(h)
print(cost)

for i in range(N):
    minc = 10 ** 4 + 1
    for j in range(K):
        if i - j - 1 < 0:
            break
        else:
            print(h[i], h[i - j - 1])
            nc = cost[i - j - 1] + abs(h[i] - h[i - j - 1])
            if nc < minc:
                minc = nc
            else:
                continue
    cost.append(minc)

print(cost)
print(cost[-1])