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
        line.append( int(q[1]) )
    else:
        print(line[head])
        head += 1
"""
#lv3
"""
n,m = map(int,input().split())
cook_list = []
for i in range(m):
    cook = list(map(int,input().split()))
<<<<<<< HEAD
    print(tuple(cook[1:]))
#    cook_dict[] = i + 1
print(cook_dict)
"""

print("helo")
=======
    k = cook[0]
    a = cook[1:]
    cook_list.append([k,a])

b = list(map(int,input().split()))
veg_dict = dict()
for i in range(n):
    veg_dict[b[i]] = i

eat_days = [0] * n
for i in range(m):
    k,a = cook_list[i]
    eat_day = -1
    for j in range(k):
        if veg_dict[a[j]] != -1:
            if eat_day < veg_dict[a[j]]:
                eat_day = veg_dict[a[j]]
            else:
                continue
        else:
            break
    eat_days[eat_day] += 1

ans = 0
for i in range(n):
    ans += eat_days[i]
    print(ans)
"""
>>>>>>> 1c1851acea25f2f6fca1bcc90be345c9e6ca68b1
