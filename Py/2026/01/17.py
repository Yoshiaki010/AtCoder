#lv1
"""
P,Q = map(int,input().split())
X,Y = map(int,input().split())
ans = "Uknow"
if P <= X and X <= P + 99:
    if Q <= Y and Y <= Q + 99:
        ans = "Yes"
    else:
        ans = "No"
else:
    ans = "No"
print(ans)
"""

#lv2
"""
N,M = map(int,input().split())
S = input()
T = input()
s_dict = {}
t_dict = {}

Q = int(input())
for _ in range(Q):
    w = list(set(input()))
    w_N = len(w)

    for i in range(N):
        s_dict[S[i]] = 0
    for i in range(M):
        t_dict[T[i]] = 0

    s_check = 0
    t_check = 0
    for i in range(w_N):
        if w[i] in S and -1 < s_check:
            if s_dict[w[i]] == 0:
                s_dict[w[i]] += 1
                s_check += 1
            else:
                continue
        else:
            s_check = -1            
        
        if w[i] in T and -1 < t_check:
            if t_dict[w[i]] == 0:
                t_dict[w[i]] += 1
                t_check += 1
        else:
            t_check = -1

    ans = "?"
    #print(s_check,t_check)
    #print(s_dict)
    #print(t_dict)

    if -1 < s_check and s_check < N + 1:
        if -1 < t_check and t_check < M + 1:
            ans = "Unknown"
        else:
            ans = "Takahashi"
    else:
        if -1 < t_check and t_check < M + 1:
            ans = "Aoki"
        else:
            ans = "Unknown"
    print(ans)
"""

#lv3
"""
"""
