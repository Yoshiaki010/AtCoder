n=int(input())
s=list(input())
t=list(input())
wa=[]
wb=[]
wac=0
wbc=0
ans=0
for i in range(n):
    i+=1
    if s[n-i] != t[n-i]:
        if t[n-i] == "A":
            wa.append(n-i)
            wac+=1
        else:
            wb.append(n-i)
            wbc+=1
    if 1 <= wac and 1 <= wbc:
        if wa[0] < wb[0]:
            s[wa[0]] = "A"
            s[wb[0]] = "B"
            wac-=1
            wbc-=1
            wa.pop(0)
            wb.pop(0)
            ans+=1
else:
    if s != t:
        if 0 < wac and wbc == 0:
            ans+=wac
        else:
            ans=-1
print(ans)