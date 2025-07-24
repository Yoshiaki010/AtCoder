#lv1
"""
N = int(input())

ans = 0
for _ in range(N):
    A,B = map(int,input().split())
    if A < B:
        ans += 1
    else:
        continue
print(ans)
"""
#lv2
"""
S = input()
T = input()

ans = "Yes"
for i in range(len(S) - 1):
    i += 1
    if S[i] <= "Z":
        if S[i - 1] in T:
            continue
        else:
            ans = "No"
            break
print(ans)
"""
#lv3
"""
T = int(input())

for _ in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    LastMino = S[-1]
    FirstMino = S[0]

    if LastMino <= FirstMino * 2:
        ans = 2
    else:
        S.sort()

        ans = 0
        next = 0
        count = False
        for i in range(N - 1):
            if S[i] == FirstMino and not count:
                count = True
                ans += 1
                next = S[i] * 2
            else:
                pass

            if S[i + 1] == LastMino:
                if LastMino <= next:
                    ans += 1
                else:
                    ans = -1
                break
            else:
                if count:
                    if next < S[i + 1]:
                        ans = -1
                        break
                    else:
                        if next < S[i + 2]:
                            next = S[i + 1] * 2
                            ans += 1
                        else:
                            continue
                else:
                    continue        
    print(ans)
"""