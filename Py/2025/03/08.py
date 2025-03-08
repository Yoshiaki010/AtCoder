#lv1
"""
N = int(input())
A = list(map(int,input().split()))

ans = "Unknow"
for i in range(N-2):
  if A[i] == A[i + 1] and A[i + 1] == A[i + 2]:
    ans = "Yes"
    break
  else:
    ans = "No"
print(ans)
"""
#lv2
"""
Cardes = [0]*100
Q = int(input())

for _ in range(Q):
    query = input()
    if query[0] == "1":
        type,x = map(int,query.split())
        Cardes.append(x)
    else:
        print(Cardes[-1])
        Cardes = Cardes[0:-1]
"""
#lv3
"""
N,M = map(int,input().split())
B = list(map(int,input().split()))
W = list(map(int,input().split()))

B.sort()
W.sort()

num_M = M
pointer = 0
for _ in range(M):
    if W[pointer] < 0 or N < num_M:
        pointer += 1
        num_M -= 1
    else:
        break
W = W[pointer:]

ans = 0
for i in range(N):
    ans += B[i]
for i in range(num_M):
    ans += W[i]

num_N = N
B_pointer = 0
for _ in range(num_N - num_M):
    if B[B_pointer] < 0:
        ans += -B[B_pointer]
        B_pointer += 1
        num_N -= 1
    else:
        break
else:
    W_pointer = 0
    for _ in range(num_N):
        if 0 < -B[B_pointer] + -W[W_pointer]:
            ans = ans + -B[B_pointer] + -W[W_pointer]
            B_pointer += 1
            W_pointer += 1
        else:
            break

print(ans)
"""
#lv4 ?