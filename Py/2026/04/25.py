#LvA
"""
A,B,C = map(int,input().split())
ans = "Uknow"
if A != B and B == C:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""
#LvB
"""
H,W = map(int,input().split())

s = [["-"] * (W + 2)]
for _ in range(H):
    s.append(list("-" + input() + "-"))
s.append(["-"] * (W + 2))
#print(s)

ans = []
for h1 in range(1,H + 1):
    for h2 in range(1,H + 1):
        if h1 <= h2:
            for w1 in range(1,W + 1):
                for w2 in range(1,W + 1):
#                    print(w1, w2, "\\", w1 <= w2)
                    if w1 <= w2:
#                        print(h1,h2,w1,w2)
#                        print(f"1 <= i <= {h2},1 <= j <= {w2}")
                        for i in range(h1,h2 + 1):
                            for j in range(w1,w2 + 1):
#                                print(f"s[{i}][{j}] == s[{h1 + h2 - i}][{w1 + w2 - j}] // {s[i][j] == s[h1 + h2 - i][w1 + w2 - j]}")#, end = " "
                                if s[i][j] == s[h1 + h2 - i][w1 + w2 - j]:
#                                    print("con")
                                    continue
                                else:
#                                    print("bre")
                                    break
                            else:
                                continue
                            break
                        else:
#                            print("+")
                            ans.append((h1,h2,w1,w2))
        else:
            continue
print(len(ans))
#print(ans)
"""
#LvC
"""
N,K = map(int,input().split())

A = list(map(int,input().split()))
numDict = dict()
sum = 0

for i in range(N):
    if A[i] in numDict:
        numDict[A[i]] += 1
    else:
        numDict[A[i]] = 1
    sum += A[i]

numList = list(numDict)
numListN = len(numList)

if numListN - K < 1:
    ans = 0
else:
    Asum = []
    for x in numList:
        Asum.append(x * numDict[x])

    Asum.sort(reverse= True)

    ans = 0
    for i in range(numListN):
        if i < K :
            continue
        else:
            ans += Asum[i]
print(ans)
"""
