#lvA
"""
N,M = map(int,input().split())

if N % 2 == 0:
    s = N // 2
else:
    s = N // 2 + 1

if M <= s:
    ans = "Yes"
else:
    ans = "No"

print(ans)
"""
#lvB
"""
S = input()

s_dic = dict()
max = 0
for i in range(len(S)):
    if S[i] not in s_dic:
        s_dic[S[i]] = 1
    else:
        s_dic[S[i]] += 1
    if max < s_dic[S[i]]:
        max = s_dic[S[i]]
    else:
        pass

not_use = []
s_lis = list(s_dic)
for i in range(len(s_lis)):
    if s_dic[s_lis[i]] == max:
        not_use.append(s_lis[i])
    else:
        continue

ans = []
for i in range(len(S)):
    if S[i] not in not_use:
        ans.append(S[i])
    else:
        pass
print("".join(ans))
"""

#lvC
"""
"""

