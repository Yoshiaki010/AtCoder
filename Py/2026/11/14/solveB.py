K = int(input())
A = list(map(int,input().split()))

ans = 10

max = -1
min = 10

for i in range(K):
    if max < A[i]:
        max = A[i]
    if A[i] < min:
        min = A[i]

if max == 9:
    ans = min
else:
    ans = -1
print(ans)