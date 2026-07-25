#lvA
"""
N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(N - 2):
    if A[i] < A[i + 1] > A[i + 2]:
        ans += 1

print(ans)
"""

#lvB
"""
M,D = map(int,input().split())
S = list(input())

def GChecker(gPos, nowPos):
    if S[nowPos] == "G":
        gPos = nowPos
        return gPos

    if abs(nowPos - GPos) <= D:
        S[nowPos] = "x"
    return gPos

GPos = - (D + 1)
for i in range(M):
    GPos = GChecker(GPos, i)

GPos = M + D
for i in range(M):
    GPos = GChecker(GPos, M - i - 1)

ans = 0
for i in range(M):
    if S[i] == "G" or S[i] == "x":
        continue
    ans += 1
print(ans)
"""

#lvC
"""
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

def RangeCheker(a, b):
    if a == b:
        return 1
    elif a < b:
        return b - a
    else:
        return 0

ans = 1
for i in range(N):
    print(P[i], Q[i], RangeCheker(P[i], Q[i]))
    ans *= RangeCheker(P[i], Q[i])

print(ans)
"""
