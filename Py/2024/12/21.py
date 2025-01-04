#lv1
"""
a,b,c = map(int,input().split())
ans = "Unknow"
if a + b == c:
    ans = "Yes"
elif a + c == b:
    ans = "Yes"
elif b + c == a:
    ans = "Yes"
elif a == b and b == c:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""
#lv2
"""
h,w,y,x = map(int,input().split())
s = []
for _ in range(h):
    s.append(list(input()))
t = input()

now = (y,x,0)
for i in range(len(t)):
    y,x,c = now
    x -= 1
    y -= 1
    if t[i] == "U":
        y -= 1
    elif t[i] == "D":
        y += 1
    elif t[i] == "L":
        x -= 1
    else:
        x += 1
    if s[y][x] != "#":
        if s[y][x] == "@":
            s[y][x] = "."
            c += 1
        else:
            pass
        now = (y+1,x+1,c)
    else:
        pass

print(*now)
"""
#lv3
"""
"""
