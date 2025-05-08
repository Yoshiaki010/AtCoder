#lv2
"""
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