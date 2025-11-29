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
""" 
T = int(input())

for _ in range(2):
    N,H = map(int,input().split())
    obj = []
    for _ in range(N):
        t,l,u = map(int,input().split())
        obj.append([t,l,u])
    print(obj)

    last_t,last_l,last_u = obj[-1]
    now = [last_t,last_l,last_u]
    for i in range(N - 1):
        back_t,back_l,back_u = obj[N - i - 2]
        now_t,now_l,now_u = now
        print()
        diff = now_t - back_t

        if now_u <= back_l:
            if now_u <= back_u:
                if now_l <= back_l:
                    

        else:


"""
        if now_u < back_l:
            #全て下に飛び出てる　under out
            print(f"[{now_l} - {now_u}] < [{back_l} ~ {back_u}]")
            if back_l - now_u <= diff:
                now = [back_t,back_l,(now_u + diff)]
        else:
            if now_u < back_u:
                #内側にいる inside
                print(f"[{back_l} ~ [{now_l} - {now_u}] ~ {back_u}]")
            else:
                if now_l < back_u:
                    if now_l < back_l:
                        #両側(now_l,now_u)が飛び出ている
                        print(f"[{now_l} - [{back_l} ~ {back_u}] - {now_u}]")
                    else:
                        #上側(now_u)が飛び出てる
                        print(f"[{back_l} ~ [{now_l} -~ {back_u}] - {now_u}]")
                else:
                    # 全て上に飛び出ている
                    print(f"[{back_l} ~ {back_u}] < [{now_l} - {now_u}]")
"""