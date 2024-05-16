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

#入力と縦
for _ in range(n):
    s=input()
    all+=s
    tates.append(s)

#横
for i in range(n):
    print(all[i::n])
    yokos.append(all[i::n])
print()

#斜め
for i in range(n-5):
    print(all[i::n+1])
    print(i,n+1)
    nanas.append(all[i::n+1])


print(tates)
print(yokos)
print(nanas)
print(all)
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
