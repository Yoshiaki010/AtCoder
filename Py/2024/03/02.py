#lv1
"""
a,b=map(int,input().split())
if a != a+b:
    ans=a
elif b != a+b:
    ans=b
else:
    ans=9
print(ans)
"""
#lv2
"""
n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    for i in range(n):
        if a[i] == 1:
            print(i+1,end=" ")
        else:
            continue
    print()
"""
#lv3
n=int(input())
x=int(((n**0.375)//1))
for i in range(x):
    k=(x-i)**3
    if k <= n:
        a=list(str(k))
        for i in range(len(a)):
            if a[i] != a[len(a)-i-1]:
                break
            else:
                continue
        else:
            ans=k
            break
    else:
        continue
else:
    ans=1
print(ans)
