#A
"""
A,B = map(int,input().split())
ans = A * 12 + B
print(ans)
"""

#B
"""
H,W,N = map(int,input().split())
A = []
for _ in range(H):
    A.append(list(map(int,input().split())))

B = set()
for _ in range(N):
    B.add(int(input()))

max_same = 0
for i in range(H):
    same = 0
    for j in range(W):
        if A[i][j] in B:
            same += 1
        else:
            continue
    if max_same < same:
        max_same = same
    else:
        continue

print(max_same)
"""

#C
"""
"""
T = int(input())

for _ in range(T):
    N = int(input())
    animal = [tuple(map(int,input().split())) for _ in range(N)]
    sort_animal = sorted(animal, key = lambda x: (x[1], x[0]), reverse = True)
#    print(animal)
#    print(sort_animal)

    pull_animal = 0
    take_animal = N - 1
    car_p = 0
    car_w = 0

    ans = 0
    for _ in range(N):
        w,p = sort_animal[take_animal]
        if car_w + w < car_p:
            car_w += w
            ans += 1
            take_animal -= 1
        else:
            w,p = sort_animal[pull_animal]
            car_p += p
            pull_animal += 1
#    print(car_p, car_w)
    print(ans)