"""
#lv1
n=int(input())
a=set(map(int,input().split()))
ans="Unknow"
if len(a) == 1:
    ans="Yes"
else:
    ans="No"
print(ans)
"""
"""
#lv2
n=int(input())
ans="Unknow"
amari=n
while amari > 3:
    if amari%2 == 0:
        amari/=2
    elif amari%3 == 0:
        amari/=3
    else:
        ans="No"
        break
else:
    ans="Yes"
print(ans)
"""
"""
#lv3
n,t=input().split()
tdash=list(t)
print(tdash)
for _ in range(int(n)):
    s=list(input())
    wrong=0
    for i in range(len(s)):
        if len(set(s)) - len(set(tdash)) == 1:
            print(set(s)-set(tdash))
        elif len(set(s)) - len(set(tdash)) == 0:
            len(tdash) - len(s)
    print(tdash)
    if tdash == s:
        ans="Yes"
        break
    elif 
"""
