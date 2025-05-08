#lv1
"""
s = input()
abc = [True for i in range(26)]
for i in range(len(s)):
    if "a" <= s[i] <= "z":
        abc[ord(s[i]) - 97] = False
    else:
        continue

ans = []
for i in range(26):
    if abc[i]:
        ans.append(chr(i + 97))
    else:
        continue
print(ans[0])
"""
#lv2
"""
def rotate(x):
    new = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(x[n - j - 1][i])
        new.append(row)
    return new

def count_diff(x,y):
    diff = 0
    for i in range(n):
        for j in range(n):
            if x[i][j] != y[i][j]:
                diff += 1
            else:
                continue
    return diff

n = int(input())
s = [input() for _ in range(n)]
t = [input() for _ in range(n)]

ans = n * n + 4
diff = 0
rotate_num = 0
for i in range(5):
    diff = count_diff(s,t)
    if diff + rotate_num < ans:
        ans = diff + rotate_num
    s = rotate(s)
    rotate_num += 1
print(ans)
"""

#lv3
"""
"""
N,M = map(int,input().split())

n_num = [0] * N
n_dict = dict()
for i in range(N):
    n_dict[ i + 1 ] = []

def check(s,t):
    if 1 < n_num[s - 1]:
        ans = True
    else:
        n_dict[s].append(t)
        n_num[s - 1] += 1
        ans = False
    return ans

ans = "No"
for _ in range(M):
    a,b = map(int,input().split())
    if check(a,b) or check(b,a):
        break
    else:
        continue
else:
    next = set(n_dict[1])

    ok_n = set()
    ok_n.add(1)
    ok_n_num = 1
    next_num = 1
    p = 0
    while 0 < next_num:
        next_num = 0
        new_next = set()
        for n in next:
            ok_n.add(n)
            ok_n_num += 1
            for a in n_dict[n]:
                if a in ok_n or a in next or a in new_next:
                    p += 1
                    continue
                else:
                    new_next.add(a)
                    next_num += 1
                    p += 1
        next = new_next

    if ok_n_num == N:
        ans = "Yes"
    else:
        ans = "No"
print(ans)
"""
"""
