#lv1
"""
N = int(input())
T = input()
A = input()
ans = "Unknow"
for i in range(N):
    if T[i] == "o" and A[i] == "o":
        ans = "Yes"
        break
    else:
        continue
else:
    ans = "No"
print(ans)
"""
#lv2
"""
N = int(input())
A = list(map(int,input().split()))

A.sort(reverse=True)

A_dict = dict()
all = 0
for i in range(N):
    if A[i] in A_dict:
        A_dict[A[i]] += 1
    else:
        A_dict[A[i]] = 1 + all
    all = A_dict[A[i]]
A_dict[0] = N

A_dict_list = list(A_dict)
A_dict_list_N = len(A_dict_list)
A_dict_list.sort()

ans = 0
for i in range(A_dict_list_N):
    if A_dict_list[i] <= A_dict[A_dict_list[i]]:
        ans = A_dict_list[i]
        continue
    else:
        if ans < A_dict[A_dict_list[i]]:
            ans = A_dict[A_dict_list[i]]
        else:
            pass
        break
print(ans) 
"""
#lv3
"""
N,L = map(int,input().split())
D = list(map(int,input().split()))
pointes = [0]*L
pointes[0] += 1

now = 0
for i in range(N - 1):
    now += D[i]
    now %= L
    pointes[now] += 1

ans = 0
if L % 3 == 0:
    for i in range(L // 3):
        a = pointes[i]
        b = pointes[i + L // 3]
        c = pointes[i + (L // 3) * 2]
        ans += a * b * c
else:
    ans = 0
print(ans)
"""
#lv4
"""
"""