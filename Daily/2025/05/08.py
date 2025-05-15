#lv2
"""
N = int(input())
name_dict = {}

def add_to_dict(str):
    if str in name_dict:
        name_dict[str] += 1
    else:
        name_dict[str] = 1

p = []
for _ in range(N):
    s,t = input().split()
    if s == t:
        add_to_dict(s)
    else:
        add_to_dict(s)
        add_to_dict(t)
    p.append([s,t])

ans = "Unknow"
for i in range(N):
    s,t = p[i]
    if 1 < name_dict[s]:
        if 1 < name_dict[t]:
            ans = "No"
            break
        else:
            name_dict[t] += 1
    else:
        name_dict[s] += 1
else:
    ans = "Yes"

print(ans)
"""
#lv2
ans = 0
S,T = map(int,input().split())
for a in range(90):
    for b in range(90):
        for c in range(90):
            if a + b + c <= S and a * b * c <= T:
                ans += 1
            else:
                continue
print(ans)