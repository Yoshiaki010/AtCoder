"""
#lv1
s,t=input().split()
print(s,end=" ")
print("san")
"""
#lv2
n=int(input())
kyoten=[]

for _ in range(n):
    kyoten=map(int,input().split())


if 18 <= kyoten[0][1]:
    mtgtime=9-(24-kyoten[0][1])
else:
    mtgtime=9-kyoten[0][1]
limit=18-mtgtime
