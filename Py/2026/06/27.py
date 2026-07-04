#lvA
"""
S = input()

e = 0
w = 0
for i in range(len(S)):
    if S[i] == "E":
        e += 1
    else:
        w += 1

ans = "Uknow"
if e < w:
    ans = "West"
else:
    ans = "East"
print(ans)
"""

#lvB
"""
def Delete(lis, h, w):
    result = []
    delete = 0
    isNeed = True

    for i in range(h):
        row = lis[i]
        if isNeed:
            for j in range(w):
                if row[j] == "#":
                    isNeed = False
                    break
            else:
                delete += 1
                continue
            result.append(row)
        else:
            result.append(row)

    h -= delete
    return result, h, w

def Rotation(lis, h, w):
    result = []
    for j in range(w):
        newRow = []
        for i in range(h):
            newRow.append(lis[i][w - 1 - j])
        result.append(newRow)
    return result, w, h

H,W = map(int,input().split())
C = []
for _ in range(H):
    cRow = list(input())
    C.append(cRow)

ans = C
for _ in range(4):
    ans,H,W = Delete(ans, H, W)
    ans,H,W = Rotation(ans, H, W)

for i in range(H):
    print("".join(ans[i]))
"""
#lvC
"""
"""
N,M = map(int,input().split())

chenge = []
colorNum = [0] * N
colorKind = 0
for i in range(N):
    A,D,B = map(int,input().split())
    chenge.append([A, D, B])
    colorNum[A - 1] += 1
    if colorNum[A - 1] == 1:
        colorKind += 1

chengeSortDay = sorted(chenge, key = lambda x: x[1])

ans = [-1] * M
ans[0] = colorKind
for i in range(N):
    A,D,B = chengeSortDay[i]
    colorNum[A - 1] -= 1
    colorNum[B - 1] += 1
    if colorNum[A - 1] == 0:
        colorKind -= 1
    if colorNum[B - 1] == 1:
        colorKind += 1
    ans[D - 1] = colorKind
#     print(D,"colors",colorNum,A,B,)

# print(ans)
before = -1
for i in range(M):
    if ans[i] != before and ans[i] != -1:
        before = ans[i]
    print(before)
    