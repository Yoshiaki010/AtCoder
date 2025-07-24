#lv1
"""
N,M = map(int,input().split())
A = list(map(int,input().split()))

all = sum(A)
ans = "Unknow"
if all <= M:
    ans = "Yes"
else:
    ans = "No"
print(ans)
"""

#lv2
"""
N = int(input())
S = [input() for _ in range(N)]
all = set()

for i in range(N):
    for j in range(N - i):
        j += i
        if i == j:
            continue
        else:
            all.add(S[i]+S[j])
            all.add(S[j]+S[i])

all = list(all)
all.sort()
print(len(all))
"""
#lv3
"""
Q = int(input())

A = list()
a_Del = 0
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        T,C,X = q
        A.append([X,C])
    else:
        T,K = q
        ans = 0
        i = a_Del
        while 1 <= K:
            if A[i][1] <= K:
                ans += A[i][0] * A[i][1]
                K -= A[i][1]
                a_Del += 1
            else:
                ans += A[i][0] * K
                A[i][1] -= K
                K = 0
            i += 1
        print(ans)
"""
#v4
"""
"""
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    print(a)
    r = a[1] / a[0] 
    print(r)
    ans = "Uknow"
    for i in range(n - 1):
        print(a[i],a[i] * r,a[i + 1],a[i] * r == a[i + 1])
        if a[i] * r == a[i + 1]:
            continue
        else:
            ans = "No"
            break
    else:
        ans = "Yes"
    print(ans)


    T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))

    a.sort()
    negativ_numbers = []
    positiv_numbers = []
    for i in range(n):
        if a[i] < 0:
            negativ_numbers.append(a[i])
        else:
            positiv_numbers.append(a[i])
    negativ_numbers.sort(reverse = True)

    r_not_positiv = False   
    first = True
    if 0 == len(negativ_numbers) or 0 == len(positiv_numbers):
        r = a[1] / a[0]
    else:
        r_not_positiv = True
        if negativ_numbers[0] * -1 < positiv_numbers[0]:
            r = positiv_numbers[0] / negativ_numbers[0]
            first = True
            print(positiv_numbers[0] ,"/", negativ_numbers[0], "=", r)
        else:
            first = False
            r =  negativ_numbers[0] / positiv_numbers[0]
            print(negativ_numbers[0] , "/", positiv_numbers[0], "=", r)
    print(r)
    print(a)
    print(negativ_numbers,positiv_numbers)
    negativ_point = 0
    positiv_point = 0
    if r_not_positiv:
        for _ in range(n):
            if first:
                if negativ_numbers[negativ_point] * r == positiv_numbers[positiv_point]:
                    print(negativ_numbers[negativ_point], positiv_numbers[positiv_point])
                    first = False
                    negativ_point += 1
                    continue
                else:
                    break
            else:
                if positiv_numbers[positiv_point] * r == negativ_numbers[negativ_point]:
                    print(positiv_numbers[positiv_point],positiv_numbers[positiv_point] * r, negativ_numbers[negativ_point])
                    first = True
                    positiv_point += 1
                    continue
                else:
                    break
    else:
        print("positiv")