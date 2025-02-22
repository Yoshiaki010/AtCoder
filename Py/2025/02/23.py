#lv1
"""
s = input()
ans = ""
for i in range(len(s)):
    if s[i] == "2":
        ans += "2"
    else:
        continue
print(ans)
"""
#lv2
"""
n = int(input())
s_dict = {}
s_list = []
for i in range(n):
    s = input()
    s_dict[len(s)] = s
    s_list.append(len(s))

s_list.sort()

for i in s_list:
    print(s_dict[i],end="")
"""
#lv3
"""
s = input()
ans = ""
w = 0
for i in range(len(s)):
    if s[i] == "W":
        w += 1
    else:
        if s[i] == "A":
            ans += "A"+"C"*w
        else:
            ans += "W"*w+s[i]
        w = 0
else:
    ans += "W"*w
print(ans)
"""
"""
#lv4
s = input()
t = "?"
ans = "No"

for i in range(len(s)):
    if s[i] == "(":
        t += "("
    elif s[i] == ")":
        if t[-1] == "(":
            t = t[:-1]
        else:
            break
    elif s[i] == "[":
        t += "["
    elif s[i] == "]":
        if t[-1] == "[":
            t = t[:-1]
        else:
            break
    elif s[i] == "<":
        t += "<"
    elif s[i] == ">":
        if t[-1] == "<":
            t = t[:-1]
        else:
            break
else:
    if t == "?":
        ans = "Yes"
print(ans)
"""
#lv5