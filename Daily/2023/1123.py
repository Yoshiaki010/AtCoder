"""
#lv2
n=int(input())
a=list(map(int,input().split()))
q=int(input())
for _ in range(q):
    qq=list(map(int,input().split()))
    k=qq[1]-1
    if qq[0] == 1:
        x=qq[2]
        a[k]=x
    else:
        print(a[k])
""" 

"""
#lv2
n,x=map(int,input().split())
a=list(map(int,input().split()))
knowf=set()
knowf.add(x)
for _ in range(n):
    i=x
    if a[i-1] not in knowf and i!=a[i-1]:
        knowf.add(a[i-1])
        x=a[i-1]
    else:
        break
ans=len(knowf)
print(ans)
""" 

"""
""" 
#lv3
n,m=input().split()
s=list(input().split())
t=list(input().split())






"""
""" 
#lv3









"""
""" 
#lv4




