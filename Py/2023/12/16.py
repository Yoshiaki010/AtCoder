"""
#lv1
n=input()
print(n*int(n))
"""
"""
#lv2
s1,s2=map(ord,list(input()))
t1,t2=map(ord,list(input()))
ans="No"
s=min(abs(s1-s2),5-abs(s1-s2))
t=min(abs(t1-t2),5-abs(t1-t2))
if s == t:
    ans="Yes"
print(ans)
"""
#lv3
n=int(input())
ans=[3]
now=0
print(str(n))
a=int(str(n),2)
for i in range(n-1):
    if ans[now] == 3:
        ans.append(1)
        now+=1
    ans[now]+=1
    print(ans)
print(ans,end="")
print(3)