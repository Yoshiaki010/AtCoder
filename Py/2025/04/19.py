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
cook_dict = {}
for i in range(m):
    cook = list(map(int,input().split()))
    print(tuple(cook[1:]))
#    cook_dict[] = i + 1
print(cook_dict)
"""

print("helo")