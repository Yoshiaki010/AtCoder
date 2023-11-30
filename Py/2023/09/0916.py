"""
#lv1
a,b=list(map(int,input().split()))
ans=(a**b)+(b**a)
print(ans)
"""
"""
#lv2
s=list(input())
long=len(s)
ans=0
for i in range(len(s)):
    for j in range(len(s)-long+1):
        nowlis=s[j:j+long]
        half=long//2
        firstlis=nowlis[0:half]
        if long % 2 == 0:
            backlis=nowlis[half:half+long]
        else:
            backlis=nowlis[half+1:half+long]
        rbacklis=list(reversed(backlis))
        if firstlis == rbacklis:
            ans=len(s)-i
            break
    long-=1
    if ans != 0:
        break
else:
    ans=1
print(ans)
"""
#lv3
m=int(input())
s=[]
for i in range(3):
    s.append(list(map(int,input())))
one=set(s[0])
two=set(s[1])
three=set(s[2])
ans=0
print(s)
print(one,two,three)
if (one in two and one in three):
    ans=0
else:
    ans=-1
print(ans)