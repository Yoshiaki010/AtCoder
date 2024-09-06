#lv2
"""
b=int(input())
for i in range(15):
    i+=1
    a=i**i
    if a == b:
        ans=i
        break
    else:
        continue
else:
    ans=-1
print(ans)
"""
#lv2
"""
"""
s=list(map(int,list(input())))
top=s[0]
lines=[s[6],s[3],s[1]+s[7],s[0]+s[4],s[2]+s[8],s[5],s[9]]
print(lines)
ans="unknow"
if top == 0:
    for i in range(7):
        for j in range(7-(i+1)):
            j+=i
            print(lines[i],lines[j],lines[i+1:j+1])
            if lines[i] > 0 and lines[j] > 0:
                for k in range(j-i):
                    if lines[i+k] < 1:
                        ans="Yes"
                        print("break1")
                        break
                    else:
                        print("continu1")
                        ans="No"
                        continue
        
print("fin")        
                
print(ans)
#lv3
"""
"""

#lv3
"""
"""

#lv4
"""
"""

