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
P = []

for i in range(N):
    P.append(list(map(int,input().split())))
print(P)

w_sum = 0
for i in range(N):
    w_sum += P[i][0]
deadline = w_sum // 2
print(deadline)

all = dict()
all[0] = [0,0]

want_h_p = []
want_h = 0
for i in range(N):
    w,h,b = P[i]
    if h <= b:
        all[0][1] += b
    else:
        want_h_p.append(P[i])
        want_h += 1

print(all,list(all),want_h_p,want_h)


for i in range(want_h):
    now_all = list(all)
    for one_patern in now_all:
        w,h,b = want_h_p[i]
        nw,nh,nb = one_patern