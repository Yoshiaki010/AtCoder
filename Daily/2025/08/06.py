#lv1
"""
N,A,B = map(int,input().split())
S = input()
ans = []
for i in range(N - B):
    if i < A:
        continue
    else:
        ans.append(S[i])
print("".join(ans))
"""

#lv2
"""
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

a_dic = dict()
a_dic_num = 0
for i in range(N):
    if A[i] in a_dic:
        a_dic[A[i]] += 1
    else:
        a_dic[A[i]] = 1
        a_dic_num += 1

for i in range(M):
    if B[i] in a_dic:
        a_dic[B[i]] -= 1
    else:
        continue
a_lis = list(a_dic)
ans = []
for i in range(a_dic_num):
    if 0 < a_lis[i]:
        ans += [a_lis[i]] * a_dic[a_lis[i]]
    else:
        continue
print(*ans)
"""

#lv3
"""
"""
N = 10 ** 3
ans = 0
for i in range(N):
    for j in range(N - i - 1):
        j += i + 1
#        print(i,j, "or" , j,i)
        ans += 1
print(ans)

#lv4
"""
"""
