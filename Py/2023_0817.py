n,x = map(int, input().split())
bcount = []
bags = []
for _ in range(n):
    data = list(map(int, input().split()))
    bcount.append(data[0])
    bags.append(sorted(data[1:]))

print(bags)

# 0 番目以降のバッグから取り出して４０を作る
# 1 をとりだして、1 番目以降から 40 を作る
# 4 をとりだして、1 番目以降から 10 を作る
# 8 を取りだして、1 番目以降から 5 を作る

def findCombination(b, target):
  print("開始番号",b,"目標",target)
  ans = 0
  if b==n-1:
    print("下請けがいないので、数えます")
    return bags[b].count(target)
  else:
    for x in bags[b]:
      if target % x == 0:
         print(b,"番です。自分のところから",x,"を取り出しました")
         # 再帰呼出し
         print(b+1,"番目以降に下請けに出します")
         ans += findCombination(b+1, target // x)
  return ans

print( findCombination(0,x) )


