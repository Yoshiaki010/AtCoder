#lvA
"""
N = int(input())
A = list(map(int,input().split()))
X = int(input())

ans = A[X - 1]

print(ans)
"""

#lvB
"""
N = int(input())
A = []
for _ in range(N):
  oneLine = list(map(int,input().split()))
  L = oneLine[0]
  a = oneLine[1:]
  A.append(a)

X,Y = map(int,input().split())
ans = A[X - 1][Y - 1]
print(ans)

"""

#lvC
"""
N,K = map(int,input().split())
A = []
L = []
for _ in range(N):
    oneLine = list(map(int,input().split()))
    l = oneLine[0]
    a = oneLine[1:]
    L.append(l)
    A.append(a)
C = list(map(int,input().split()))

bLength = 0
ans = ""
for i in range(N):
    bLength += L[i] * C[i]
#    print(bLength)
    if K <= bLength:
        overItemes = (bLength - K) % L[i]
#        print(f"/{overItemes} = ({bLength} - {K}) % {L[i]}")
        ans = A[i][L[i] - overItemes - 1]
        break
    else:
        continue

print(ans)
"""

#lvD
"""
N, K = map(int,input().split())
A = list(map(int,input().split()))

aiLis = [(A[i],i) for i in range(N)]
aiLis.sort()

print(A)
print(aiLis)

needPlus = 0
for j in range(N - 1):
    a = aiLis[j][0]
    i = aiLis[j][1]
    nextA = aiLis[j + 1][0]
    nextI = aiLis[j + 1][1]

    overPlus = (nextA - a) % (i + 1)
    if overPlus == 0:
        needPlus += (nextA - a) // (i + 1)
        aiLis[j] = (nextA,i)
    else:
        needPlus += (nextA - a) // (i + 1) + 1
        aiLis[j] = (nextA + overPlus, i)

print(A)
print(overPlus)
"""
