#lv1
"""
n = int(input())
s = input()
ans = 0
for i in range(n-2):
    if s[i:i+3] == "#.#":
        ans+=1
    else:
        continue
print(ans)
"""
#lv2
"""
import math
n = int(input())
a,b = [0,0]
ans = 0

for i in range(n):
    c,d = map(int,input().split())
    inside = (((a-c)**2)+((b-d)**2))
    ans += math.sqrt(inside)
    a,b = [c,d]

ans += math.sqrt((((a-0)**2)+((b-0)**2)))
print(ans)
"""
#lv4
"""
n = int(input())
for _ in range(n):
    a = input()
    b = ""
    for i in range(n):
        b += 
    a = b
    print(a)
"""
#lv4
"""
"""
s = input()
n = len(s)
kinds = []
kindn = 0
bothpos=dict()
bothnum=dict()
for i in range(n):
    if s[i] in bothpos:
        bothpos[s[i]] += [i]
        bothnum[s[i]] += 1
    else:
        kinds += [s[i]]
        kindn += 1
        bothpos[s[i]] = [i]
        bothnum[s[i]] = 1

print(bothpos)
print(bothnum)
print(kinds)
print(kindn)

ans = 0
for i in range(kindn):
    print(s[i])
    for j in range(bothnum[s[i]]-1):
        print(((bothpos[s[i]][bothnum[s[i]]-1]) , ((bothpos[s[i]][bothnum[s[i]]-2-j]) + 1)))
        ans += (bothpos[s[i]][bothnum[s[i]]-1]) - (bothpos[s[i]][bothnum[s[i]]-2-j] + 1) - j
    print("Fin")
print(ans)