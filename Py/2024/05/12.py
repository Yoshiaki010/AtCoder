#lv3
"""
a,b,c,d,e,f=map(int,input().split())
n=int(input())
x=list(map(int,input().split()))
w=[a*1+b*5+c*10+d*50+e*100+f*500,a,b,c,d,e,f]
ans="Yes"

#長すぎワロタ
for i in range(n):
    much=x[i]
    w[0]-=much
    for _ in range(6):
        if much == 0:
            break
        else:
            if 0 < much//500 and 0 != w[6]:
                if much//500 <= w[6]:
                    mai=much//500
                else:
                    mai=w[6]
                much-=500*mai
                w[6]-=mai

            elif 0 < much//100 and 0 != w[5]:
                if much//100 <= w[5]:
                    mai=much//100
                else:
                    mai=w[5]
                much-=100*mai
                w[5]-=mai

            elif 0 < much//50 and 0 != w[4]:
                if much//50 <= w[4]:
                    mai=much//50
                else:
                    mai=w[4]
                much-=50*mai
                w[4]-=mai

            elif 0 < much//10 and 0 != w[3]:
                if much//10 <= w[3]:
                    mai=much//10
                else:
                    mai=w[3]
                much-=10*mai
                w[3]-=mai

            elif 0 < much//5 and 0 != w[2]:
                if much//5 <= w[2]:
                    mai=much//5
                else:
                    mai=w[2]
                much-=5*mai
                w[2]-=mai

            elif 0 < much//1 and 0 != w[1]:
                if much//1 <= w[1]:
                    mai=much//1
                else:
                    mai=w[1]
                much-=1*mai
                w[1]-=mai
    else:
        if much != 0:
            ans="No"
            break

print(ans)
"""
#lv4
"""
n=int(input())
s=list(map(int,list(input())))
t=[0]*n
now=n-1
ansc=0
ans=""
for _ in range(10**6):
    if s == t:
        break
    else:
        if s[now] == t[now]:
            now-=1
        else:
            if s[now] == 1:
                t[0:now+1]=[1]*(now+1)
                ans+="A"*(now+1)
            else:
                t[0:now+1]=[0]*(now+1)
                ans+="B"*(now+1)
            ansc+=now+1
            now-=1
print(ansc)
print(ans)
"""
#lv5
"""
"""