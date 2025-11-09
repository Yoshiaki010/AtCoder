#lv1
"""
H,B = map(int,input().split())
ans = 0
if B < H:
    ans = H - B
else:
    pass
print(ans)
"""

#lv2
"""
x = int(input())
N = int(input())
W = list(map(int,input().split()))
Q = int(input())

x_p = [False]*N
for i in range(Q):
    p = int(input()) - 1
    if x_p[p]:
        x_p[p] = False
        x -= W[p]
    else:
        x_p[p] = True
        x += W[p]
    print(x)
"""

#lv3
"""
N,M,K = map(int,input().split())
H = list(map(int,input().split()))
B = list(map(int,input().split()))

H.sort()
B.sort()

start = 0
x = 0
for i in range(M):
    if N - 1 < start:
        break
    else:
        if H[start] <=  B[i]:
            start += 1
            x += 1
        else:
            continue

ans = "Unkow"
if K <= x:
    ans = "Yes"
else:
    ans = "No"

print(ans)
"""

#lv4
N = int(input())
W = []
H = []
B = []

for i in range(N):
    w,h,b = map(int,input().split())
    W.append(w)
    H.append(h)
    B.append(b)

max_happy = 0
for i in range(N):
    for j in range(N):
        if i != j:
            h = W[i]
            b = W[j]
            if h <= b:
                happy = H[i] + B[j]
                if max_happy < happy:
                    max_happy = happy

print(max_happy)