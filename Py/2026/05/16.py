#lvA
"""
S = input()
sLenght = len(S)
N = int(input())

ans = S[N:sLenght - N]
print(ans)
"""

#lvB
"""
H,W = map(int,input().split())

ans = []
for i in range(H):
    row = []
    for j in range(W):
        aroundWall = 0
        aroundPos = [[i - 1, j],[i + 1, j],[i, j - 1],[i, j + 1]]
#        print(aroundPos)
        for y,x in aroundPos:
#            print(x,y)
            isXInGrid = -1 < x and x < W
            isYInGrid = -1 < y and y < H
#            print(-1 < x , x < W)
#            print(-1 < y , y < W)
            if  isXInGrid and isYInGrid:
#                print("+")
                aroundWall += 1
            else:
                continue
        row.append(aroundWall)
    ans.append(row)

#print(ans)

for i in range(H):
    print(*ans[i])
"""
#lvC
"""
S = input()
N = len(S)

ans = 0
for i in range(N):
    longestLenght = min(i + 1,N - i)
#    print(longestLenght,S[i])
    if S[i] == "C":
        ans += longestLenght
#        print("+")
print(ans)
"""

#lvD
"""
"""
def myLog2(x):
    if x < 2:
        return 0
    return 1 + myLog2(x/2)

print(myLog2(5))
print(myLog2(6))

def sortAdd(x, lis, lisLenght):
    print(x,lis,lisLenght, myLog2(lisLenght))

    mid = lisLenght // 2 + 1
    seeListMin = 0
    seeListMax = lisLenght
    bsN = myLog2(lisLenght)
    for _ in range(bsN):
        targetArea //= 2
        if lis[mid] < x:
            seeListMin = mid
            mid += (seeListMax - seeListMin) // 2
        else:
            seeListMax = mid
            mid -= (seeListMax - seeListMin) // 2
    else:
        if lis[mid] < x:
            lis.append(mid + 1, x)
        else:
            lis.append(mid,x)

X = int(input())
Q = int(input())
n = 1

borad = [X]
for i in range(Q):
    A,B = map(int,input().split())

    sortAdd(A,borad,n)
    print(borad)
    sortAdd(B,borad,n + 1)
    print(borad)
    n += 2

    ans = borad[(n // 2) + 1]
    print(ans)
