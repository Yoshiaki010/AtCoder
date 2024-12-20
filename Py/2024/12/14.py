#lv1
"""
n,c1,c2 = input().split()
s = input()

ans = []
for i in range(int(n)):
    if s[i] != c1:
        ans.append(c2)
    else:
        ans.append(s[i])
print("".join(ans))
"""
#lv2
"""
n,r = map(int,input().split())

t = r
for i in range(n):
    d,a = map(int,input().split())
    if d == 1:
        if 1599 < t < 2800:
            t += a
        else:
            continue
    else:
        if 1199 < t < 2400:
            t += a
        else:
            continue
print(t)
"""
#lv3
"""
point = list(map(int,input().split()))

join = set()
total = sum(point)
name = ["A","B","C","D","E"]
join.add(("ABCDE",total))

for i in range(5):
    join.add(("".join(name[0:i]+name[i+1:]),total-point[i]))
    join.add((name[-(i+1)],point[-(i+1)]))
    for j in range(4-i):
        j += i + 1
        join.add(("".join(name[0:i]+name[i+1:j]+name[j+1:]),total-point[i]-point[j]))
        for k in range(3-j+1):
            k += j + 1
            join.add(("".join(name[0:i]+name[i+1:j]+name[j+1:k]+name[k+1:]),total-point[i]-point[j]-point[k]))

join = list(join)

join = sorted(join, key=lambda x : x[1], reverse = True)

judge = join[0][1]
group = []
ans = []
for i in range(len(join)):
    if join[i][1] == judge:
        group.append(join[i][0])
    else:
        group.sort()
        ans += group
        group = [join[i][0]]
        judge = join[i][1]        
group.sort()
ans += group

for i in range(31):
    print(ans[i])
"""
