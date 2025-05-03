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

m_dict = dict()
for i in range(M):
    m_dict[i + 1] = set()
m_num = [0 for i in range(M)]

ans = "No"
for _ in range(M):
    a,b = map(int,input().split())
    if b not in m_dict[a]:
        m_dict[a].add(b)
        m_dict[b].add(a)
        m_num[a - 1] += 1    
        m_num[b - 1] += 1
    if 2 < m_num[a - 1] or 2 < m_num[b - 1]:
        ans = "No"
        break
    else:
        continue
else:
    ans = "Yes"

print(ans)