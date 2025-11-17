#lv1
"""
ABC = list(map(int,input().split()))
ABC.sort(reverse= True)
ans = list(map(str,ABC))
print("".join(ans))
"""

#lv2
"""
X = list(map(int,input()))
X.sort()

first = -1
not_use_x = []
for i in range(len(X)):
    if first != -1:
        not_use_x.append(X[i])
    else:
        if X[i] != 0:
            first = X[i]
        else:
            not_use_x.append(X[i])

not_use_x.sort()

ans = str(first) + "".join(list(map(str,not_use_x)))
print(ans)
"""

#lv3
"""
"""
N,X,Y = map(int,input().split())
A = list(map(int,input().split()))

max_Y = min(A)

diff = Y - X
best_g = max_Y * Y
ans = 0
for i in range(N):
    now_g = ((A[i] - max_Y) * X) + (max_Y * Y)
    if now_g == best_g:
        ans += max_Y
    else:
        best_Y = max_Y - abs(now_g - best_g) // diff
        if best_Y < -1:
            ans = -1
            break
        else:
            ans += best_Y
print(ans)