H,W,N,Q = map(int,input().split())

row = dict()
row[1] = 0
row[H] = N
col = dict()
col[1] = 0
col[W] = N

for i in range(N):
    R,C = map(int,input().split())

    if(R in row):
        row[R] += 1
    else:
        row[R] = 1

    if(C in col):
        col[C] += 1
    else:
        col[C] = 1

# 累積和
for i in range(1,H):
    row[i] += row[i - 1]
for j in range(1,W):
    col[j] += col[j - 1]

for _ in range(Q):
    q = input()
    if q[0] == "1":
        q,u,d = map(int,q)
        for i in range(N):
            if(row[N - i] <= d):
    else:
        q,l,f = map(int,q)