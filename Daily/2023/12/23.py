"""
#lv1
b,g=map(int,input().split())
pre="?"
if b < g:
  pre="Glove"
else:
  pre="Bat"
print(pre)
"""
"""
"""
#lv2
a,m,x,y=map(int,input().split())
if x == y:
    ans=0
elif a < x:
    now =x+(m-(x-a)%m)
    ans =((y-now)//m)+1
elif x <= a and a <= y:
    ans=1
    ans+=(a-x)//m
    ans+=(y-a)//m
else:
    now =y-(m-(a-y)%m)
    ans =((now-x)//m)+1
print(ans)x