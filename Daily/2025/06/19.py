#lv1
"""
A,B,C,D = map(int,input().split())
if ((A * 60) * 60) + (B * 60) < ((C * 60) * 60) + (D * 60) + 1:
    ans = "Takahashi"
else:
    ans = "Aoki"
print(ans)
"""
#lv1
"""
N = int(input())
ans = "L" + "o" * N + "ng"
print(ans)
"""
#lv2
"""
N,M = map(int,input().split())
eat_dishes = input().split()
dishes_color = input().split()
dishes_monny = list(map(int,input().split()))

ans = 0
for i in range(N):
    for j in range(M):
        if eat_dishes[i] == dishes_color[j]:
            ans += dishes_monny[j + 1]
            break
        else:
            continue
    else:
        ans += dishes_monny[0]
print(ans)
"""
#lv2
"""
X = float(input())

if 0 < X % 1:
    ans = X
else:
    ans = int(X)

print(ans)
"""
#lv3
"""
"""
AH,AW = map(int,input().split())
A = [input() for _ in range(AH)]

BH,BW = map(int,input().split())
B = [input() for _ in range(BH)]

XH,XW = map(int,input().split())
X = [input() for _ in range(XH)]

C = []
for _ in range(XH):
    C.append([False] * XW)

for i in range(XH):
    print(C[i])

def check(sheetx, anysheet, H, W, anssheet):
    for i in range(H):
        for j in range(W):
            if sheetx[i][j] == anysheet[i][j]:
                anssheet[i][j] = True
            else:
                break
    return anssheet

for i in range(XH):
    for j in range(XW):
        if X[i][j] == A[0][0]:
            NH = 0
            NW = 0
            if AH < XH - i:
                NH = AH
            else:
                NH = XH - i
            if AW < XW - j:
                NW = AW
            else:
                NW = XW - j
            C = check(X, A, NH, NW, C)
        if X[i][j] == B[0][0]:
            NH = 0
            NW = 0
            if BH < XH - i:
                NH = BH
            else:
                NH = XH - i
            if BW < XW - j:
                NW = BW
            else:
                NW = XW - j
            C = check(X, B, NH, NW, C)

ans = "Unknow"
for i in range(XH):
    for j in range(XW):
        if C[i][j]:
            continue
        else:
            ans = "No"
            break
if ans == "Unknow":
    ans = "Yes"

print("")
for i in range(XH):
    print(C[i])

print(ans)