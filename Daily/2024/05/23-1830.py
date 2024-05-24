#lv2
"""
n=int(input())
a=list(map(int,input().split()))
mt=[]
for _ in range(n-1):
    mt.append(list(map(int,input().split())))
for i in range(n-1):
    h=a[i]//mt[i][0]
    a[i]%=mt[i][0]
    a[i+1]+=h*mt[i][1]
print(a[n-1])
""" 
#lv2
"""
n=str(bin(int(input())))
m=len(n)-1
ans=0
for i in range(m-1):
    if n[m-i] == "0":
        ans+=1
    else:
        break
print(ans)
""" 
#lv3
"""
""" 

#lv3
"""
n=int(input())
ans=""
for _ in range(120):
    if n < 1:
        break
    else:
        new=""
        if n%2 == 1:
            n-=1
            new="A"+ans
        else:
            n//=2
            new="B"+ans
        ans=new
print(ans)
""" 

#lv4
"""
""" 
