#lv1
"""
y=int(input())
if (y%4 == 0 and y%100 != 0) or (y%400 == 0):
    ans=366
elif y%4 != 0 or (y%100 == 0 and y%400 != 0):
    ans=365
else:
    ans=0
print(ans)
"""
#lv2
"""
n=int(input())
a=list(map(int,input().split()))       
newa=[[a[i],i+1] for  i in range(n)]
newa.sort()
ans=newa[-2][1]
print(ans)
"""
#lv3
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
all=sum(a)
x=a[0]
if all <= m:
    x="infinite"
else:
    for i in range(n-1):
        if all+i*x <= m:
            maxx=(m-all)//i
            if x < maxx:
                x=maxx
            else:
                pass
            break
        else:
            x=a[i+1]
            all-=a[i]
    else:
        x = a[-1]
        if x*n <= m:
            pass
        else:
            x=m//n
        
print(x)
"""
