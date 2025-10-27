#DP
#vercation

N = int(input())
day = []
for _ in range(N):
    a,b,c = map(int,input().split())
    day.append((a,b,c))

hA = 0
hB = 0
hC = 0

last = 0
last_max = 0
for i in range(N):
    a,b,c = day[i]
    hA2 = max(hB,hC) + a
    hB2 = max(hA,hC) + b
    hC2 = max(hA,hB) + c
    hA = hA2
    hB = hB2
    hC = hC2
    
print(max(hA,hB,hC))

#Knapsack 1

N, W = map(int(input().split()))
all_WV = []
for _ in range(N):
    w,v = map(int,input().split())
    all_WV.append((w,v))

all_match = dict()
all_match[0] = 0
for i in range(N):
    w, v = all_WV[i]
    for now in all_match:
        new_w = now + w        
        if new_w not in all_match:
            all_match[new_w] = all_match[now] + v
