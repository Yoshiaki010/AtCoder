#lv1
"""
N = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += a[i]
print(ans)
"""
#lv2
"""
t = input()
u = input()
tn = len(t)
un = len(u)

def serch(a,b,n):
    same = False
    for i in range(n):
        if a[i] == "?":
            continue
        elif a[i] == b[i]:
            continue
        else:
            break
    else:
        same = True
    return same

ans = "No"
for i in range(tn - un + 1):
    if serch(t[i:i + un],u,un):
        ans = "Yes"
        break
    else:
        continue
print(ans)
"""
#lv3
"""
N,M,Q = map(int,input().split())

watch_dict = dict()
for i in range(1,N+1):
    watch_dict[i] = [set(), False]

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        num,x,y = q
        watch_dict[x][0].add(y)
    elif q[0] == 2:
        num,x = q
        watch_dict[x][1] = True
    else:
        num,x,y = q
        if y in watch_dict[x][0] or watch_dict[x][1]:
            print("Yes")
        else:
            print("No")
"""