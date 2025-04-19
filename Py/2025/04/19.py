#lv1
"""
s = input()
n = len(s)

ans = []
for i in range(n):
    if ord(s[i]) < 97:
        ans.append(s[i])
    else:
        continue
print("".join(ans))
"""
#lv2
"""
Q = int(input())
line = []
head = 0
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        line.append(int(q[1]))
    else:
        print(line[head])
        head += 1
"""
#lv3
"""
"""
n,m = map(int,input().split())
cook_dict = {}
for i in range(m):
    cook = tuple(map(int,input().split()))
    print(cook[1:])
    if cook[1:] in cook_dict:
        cook_dict[cook[1:]].append(i + 1)
    else:
        cook_dict[cook[1:]] = [i + 1]
print(cook_dict)

ans = []
can_eat = []
b = list(map(int,input().split()))
for i in range(n):
    if b[i] in can_eat:
        pass
    else:
        can_eat.append(b[i])
    q = tuple(can_eat)
    print(q)
    if q in cook_dict:
        ans.append(cook_dict[q])
    else:
        ans.append([])
print(ans)