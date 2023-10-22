"""
#lv1
n=int(input())
a=set(map(int,input().split()))
ans="Unknow"
if len(a) == 1:
    ans="Yes"
else:
    ans="No"
print(ans)
"""
"""
#lv2
n=int(input())
ans="Unknow"
amari=n
while amari != 1:
    if amari%2 == 0:
        amari/=2
    elif amari%3 == 0:
        amari/=3
    else:
        ans="No"
        break
else:
    ans="Yes"
print(ans)
"""
"""
"""
#lv3
def match(a1,a2):
    if a1 == a2:
        return True
    elif abs(len(a1) - len(a2)) >=2:
        return False
    elif abs(len(a1) - len(a2)) == 0:
        wrong=0
        for i in range(len(a1)):
            if a1[i] != a2[i]:
                if wrong == 0:
                    wrong+=1
                else:
                    return False
        else:
            return True
    else:
        wronga1=0
        wronga2=0
        wrong=0
        for i in range(min(len(a1),len(a2))):
            if a1[i+wronga1] != a2[i+wronga2]:
                if wrong==0:
                    if len(a1) > len(a2):
                        wronga1+=1
                        if a1[i+1] != a2[i]:
                            return False
                    else:
                        wronga2+=1
                        if a1[i] != a2[i+1]:
                            return False
                else:
                    return True
        else:
            return False

n,tdash=input().split()
tdash=list(tdash)
ans=[]
s=[]
for _ in range(int(n)):
    s.append(list(input()))

for i in range(int(n)):
    if match(tdash,s[i]):
        ans.append(i+1)
    else:
        continue

print(len(ans))        
for i in ans:
    print(i,end=" ")
