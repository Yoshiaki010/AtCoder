#lv1
"""
R,X = map(int,input().split())
ans = "Uknow"
if X == 1:
    if 1600 <= R <= 2999:
        ans = "Yes"
    else:
        ans = "No"
else:
    if 1200 <= R <= 2399:
        ans = "Yes"
    else:
        ans = "No"
print(ans)
"""
#lv2
"""
N,M = map(int,input().split())
A = list(map(int,input().split()))

num_dict = dict()
for i in range(M):
    num_dict[i + 1] = False

ans = N
all_num = 0
for i in range(N):
    if 1 <= A[i] <= M:
        if num_dict[A[i]]:
            pass
        else:
            num_dict[A[i]] = True
            all_num += 1
    else:
        pass
    if all_num == M:
        break
    else:
        ans -= 1
print(ans)
"""
#lv3
"""
N = int(input())
A = list(map(int,input().split()))

S = []
A_sum = sum(A)
for i in range(N):
    A_sum -= A[i]
    S.append(A_sum)

ans = 0
for i in range(N):
    ans += S[i] * A[i]
print(ans)
"""
