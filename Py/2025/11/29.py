#lv1
"""
W,B = map(int,input().split())
n = (W * 1000 // B) + 1
print(n)
""" 

#lv2
"""
N,M = map(int,input().split())

bird_num = [0]*M
bird_Wsum = [0]*M

for _ in range(N):
    a,b = map(int,input().split())
    bird_num[a - 1] += 1
    bird_Wsum[a - 1] += b

for i in range(M):
    print(bird_Wsum[i] / bird_num[i])
""" 

#lv3
"""
T = int(input())

for _ in range(T):
    N,H = map(int,input().split())
    case = []

    for _ in range(N):
        t,l,u = map(int,input().split())
        case.append([t,l,u])

    now = [0,H,H]

    ans = "Unknow"
    for i in range(N):
        next_t,next_l,next_u = case[i]
        now_t,now_l,now_u = now
 
        move = next_t - now_t
 
        max_u = now_u + move
        min_l = now_l - move

        now = [next_t, max(min_l, next_l), min(max_u, next_u)]
        now_t, now_l, now_u = now

        if next_l <= now_l and now_l <= next_u and next_l <= now_u and  now_u <= next_u:
            continue
        else:
            ans = "No"

        if now_l <= 0:
            ans = "No"

    else:
        if ans == "Unknow":
            ans = "Yes"

    print(ans)
""" 

#lv4
"""
"""

#lv5
"""
"""