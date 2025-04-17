#lv1
"""
s = int(input())
if 200 <= s and s <= 299:
    ans = "Success"
else:
    ans = "Failure"
print(ans)
"""
#lv2
"""
n = int(input())

account = False
erro = 0
for _ in range(n):
    s = input()
    if s == "login":
        account = True
    elif s == "logout":
        account = False
    elif s == "public":
        continue
    else:
        if account:
            continue
        else:
            erro += 1
print(erro)
"""
#lv3
"""
n,k = map(int,input().split())
next = 0
a = []

for i in range(n + 1):
    next %= 10 ** 9
    if i < k:
        next += 1
        a.append(1)
    else:
        a.append(next)
        next += next - a[i - k]
    
print(a[n])
"""
#lv4
"""
"""
n,k = map(int,input().split())
s = input()
o_num = 0
for i in range(n):
    if s[i] == "o":
        o_num += 1
front = s[0]
ans = [s[0]]
for i in range(n - 1):
    if front == "o":
        front = "."
    else:
        front = s[i + 1]
        if s[i + 1] == "o":
            ans[i] = "."
    ans.append(front)

print(*ans)