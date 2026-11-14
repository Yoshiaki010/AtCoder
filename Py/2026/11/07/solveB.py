N,Q = map(int,input().split())
K = list(map(int,input().split()))
Cards = [i for i in range(1,N + 1)]

for i in range(Q):
    Ki = K[i]
    TopCards = Cards[0:Ki]
    for j in range(Ki):
        Cards[j] = TopCards[Ki - j - 1] * -1

for i in range(N):
    print(Cards[i])