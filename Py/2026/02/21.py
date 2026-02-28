#lvA
"""
S = input()
ans = "Of" + S[0].lower() + S[1:]
print(ans)
"""
#lvB
"""
N,M = map(int,input().split())
D = [1 for _ in range(M)]

ans = []
for _ in range(N):
    L = int(input())
    X = list(map(int,input().split()))
    for i in range(L):
        if D[X[i] - 1] == 1:
            D[X[i] - 1] = 0
            print(X[i])
            break
        else:
            continue
    else:
        print(0)
"""

#lvC
"""
"""