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
print(6*0.5)
n=int(input())
for i in range(10):
    i+=1
    ans=(10-i)**3
    if ans < n and 10 < ans:
        a=list(str(ans))
        for i in range(len(a)):
            if a[i] != a[len(a)-i-1]:
                break
            else:
                continue
        else:
            break
    else:
        continue
else:
    ans=1
print(ans)