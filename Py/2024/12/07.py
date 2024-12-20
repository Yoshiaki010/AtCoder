#lv1
"""
n = int(input())
time,water = map(int,input().split())
for _ in range(n-1):
    t,v = map(int,input().split())
    if t - time > water:
        nowwater = 0
    else:
        nowwater = abs(water-(t - time))
    time,water = t,nowwater + v
print(water)
"""
#lv2
"""
h,w,d = map(int,input().split())
places = []
n = 0
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == ".":
            places.append((i,j))
            n +=1

ans = 0
for i in range(n):
    s1 = places[i]
    for j in range(n):
        if i < j:
            s2 = places[j]
            floor = 0
            for k in range(n):
                place = places[k]
                s1manhhatan = abs(place[0] - s1[0]) + abs(place[1] - s1[1])
                s2manhhatan = abs(place[0] - s2[0]) + abs(place[1] - s2[1])
                if s1manhhatan < d+1 or s2manhhatan < d+1:
                    floor += 1
                else:
                    continue
            if ans < floor:
                ans = floor
            else:
                pass
        else:
            continue
print(ans)
"""
#lv3
"""
"""
