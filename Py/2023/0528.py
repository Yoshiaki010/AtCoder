'''
#lv3
n=int(input())
a=list(map(int,input().split()))
ans="Yes"
for i in range(n):
    if i%2!=0 and ans=="Yes":
        if a[i-1]<a[i] and a[i]>a[i+1]:
            ans="Yes"
        else:
            ans="No"
if ans=="Yes":
    print(ans)
else:
    rea=sorted(a,reverse=True)
    big=[]
    small=[]
    a=[]
    for i in range((n-1)//2):
        a+=[rea[i+((n-1)//2)]]
        a+=[rea[i]]
    a+=[rea[-1]]
    ans="Yes"
    for i in range(n):
        if i%2!=0 and ans=="Yes":
            if a[i-1]<a[i] and a[i]>a[i+1]:
                ans="Yes"
            else:
                ans="No"
    print(ans)
'''

"""
#lv4
n=int(input())
for _ in range(n):
    t=bin(int(input()))
    print(t)

"""