#lv1
"""
s = input()
a = 0
b = 0
c = 0
for i in range(3):
    if s[i] == "A":
        a += 1
    elif  s[i] == "B":
        b += 1
    elif  s[i] == "C":
        c += 1
    else:
        continue

ans = "Unknow"
if a > 0 and b > 0 and c > 0:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""

#lv2
"""
s = []
sans = [list("."*8) for _ in range(8)]

for i in range(8):
    s += list(input())

for i in range(8):
    if "#" in s[i*8:(i*8)+8]:
        for j in range(8):
            sans[i][j] = "#"
    else:
        pass
    if "#" in s[i::8]:
        for j in range(8):
            sans[j][i] = "#"
    else:
        continue

ans = 0
for i in range(8):
    for j in range(8):
        if sans[i][j] == ".":
            ans += 1
        else:
            continue
print(ans)
"""

#lv3
n,m = map(int,input().split())
sans = []
for i in range(n):
    sans.append(["."]*n)

ans = n**2
for i in range(8):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    if sans[a][b] != "n":
        if sans[a][b] == ".":
            ans -= 1
        sans[a][b] = "n"
        if -1 < a + 2 and a + 2 < n and -1 < b + 1 and b + 1 < n:
            if sans[a + 2][b + 1] == ".":
                sans[a + 2][b + 1] = "#"
                ans -= 1
        if -1 < a + 1 and a + 1 < n and -1 < b + 2 and b + 2 < n:
            if sans[a + 1][b + 2] == ".":
                sans[a + 1][b + 2] = "#"
                ans -= 1
        if -1 < a - 1 and a - 1 < n and -1 < b + 2 and b + 2 < n:
            if sans[a - 1][b + 2] == ".":
                sans[a - 1][b + 2] = "#"
                ans -= 1
        if -1 < a - 2 and a - 2 < n and -1 < b + 1 and b + 1 < n:
            if sans[a - 2][b + 1] == ".":
                sans[a - 2][b + 1] = "#"
                ans -= 1            
        if -1 < a - 2 and a - 2 < n and -1 < b - 1 and b - 1 < n:
            if sans[a - 2][b - 1] == ".":
                sans[a - 2][b - 1] = "#"
                ans -= 1
        if -1 < a - 1 and a - 1 < n and -1 < b - 2 and b - 2 < n:
            if sans[a - 1][b - 2] == ".":
                sans[a - 1][b - 2] = "#"
                ans -= 1
        if -1 < a + 1 and a + 1 < n and 0 < b - 2 and b - 2 < n:
            if sans[a + 1][b - 2] == ".":
                sans[a + 1][b - 2] = "#"
                ans -= 1
        if -1 < a + 2 and a + 2 < n and -1 < b - 1 and b - 1 < n:
            if sans[a + 2][b - 1] == ".":
                sans[a + 2][b - 1] = "#"
                ans -= 1
    else:
        continue
aans = 0
for i in range(n):
    for j in range(n):
        if sans[i][j] == ".":
            aans += 1
    print(sans[i])
print(aans)
print(ans)
"""
"""
