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
knightpos = set()
cantputpos = set()

ans = n**2
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    if (a,b) in knightpos:
        continue
    else:
        print("rouk:",a,b)
        knightpos.add((a,b))
        if (a,b) not in cantputpos:
#            print("-1")
            cantputpos.add((a,b))
            ans -= 1
        if -1 < a + 1 and a + 1 < n:
            if 0 < b - 2 and b - 2 < n:
                if (a + 1 , b - 2) not in cantputpos:
#                    print(a + 1 , b - 2)
                    cantputpos.add((a + 1,b - 2))
                    ans -= 1
            if -1 < b + 2 and b + 2 < n:
                if (a + 1 , b + 2) not in cantputpos:
                    print(a + 1 , b + 2)
                    cantputpos.add((a + 1,b + 2))
                    ans -= 1
        if -1 < a + 2 and a + 2 < n:
            if -1 < b + 1 and b + 1 < n:
                if (a + 2 , b + 1) not in cantputpos:
#                    print(a + 2 , b + 1)
                    cantputpos.add((a + 2,b + 1))
                    ans -= 1
            if -1 < b - 1 and b - 1 < n:
                if (a + 2 , b - 1) not in cantputpos:
#                    print(a + 2 , b - 1)
                    cantputpos.add((a + 2,b - 1))
                    ans -= 1
        if -1 < a - 1 and a - 1 < n:
            if -1 < b + 2 and b + 2 < n:
                if (a - 1 , b + 2) not in cantputpos:
                    print(a - 1 , b + 2)
                    cantputpos.add((a - 1,b + 2))
                    ans -= 1
            if -1 < b - 2 and b - 2 < n:
                if (a - 1 , b - 2) not in cantputpos:
                    print(a - 1 , b - 2)
                    cantputpos.add((a - 1,b - 2))
                    ans -= 1
        if -1 < a - 2 and a - 2 < n:
            if -1 < b + 1 and b + 1 < n:
                if (a - 2 , b + 1) not in cantputpos:
                    print(a - 2 , b + 1)
                    cantputpos.add((a - 2,b + 1))
                    ans -= 1
            if -1 < b - 1 and b - 1 < n:
                if (a - 2 , b - 1) not in cantputpos:
                    print(a - 2 , b - 1)
                    cantputpos.add((a - 2,b - 1))
                    ans -= 1

#print(knightpos)
print(ans)
"""


"""
