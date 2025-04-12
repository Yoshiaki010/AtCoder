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
"""
n,k = map(int,input().split())
ans = 0
front_k = []
front_num = 0
front_all = 0

for i in range(n + 1):
    front_num += 1
    if i < k:
        front_k.append(1)
        front_all += 1
    else:
        front_k.append(front_all)
        front_all += front_all - front_k[0]
        front_k = front_k[1:]
#    print(front_k)

print(front_k[-1])
#lv4
"""
"""
