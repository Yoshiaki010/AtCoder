#lv2
"""
a,b,c,d,e,f=map(int,input().split())
ans=a*b*c-d*e*f
ans%=998244353
print(ans)
"""
#lv2
"""
a=input()
for _ in range(100):
    new=""
    try:
        b=input()
        new+=b+"\n"+a
        a=new
    except :
        break
print(a)
"""
#lv3
"""
"""
n=int(input())
tates=[]
yokos=[]
nanas=[]
all=""
for _ in range(n):
    s=input()
    all+=s
    tates.append(s)
print(tates,all)
for i in range(n):
    all[i+n*::]

#lv3
"""
n=int(input())
d=dict()
for _ in range(n):
    s=input()
    if s not in d:
        d[s]=0
        print(s)
    else:
        d[s]+=1
        print(s+"("+str(d[s])+")")
"""
#lv4
"""
"""
