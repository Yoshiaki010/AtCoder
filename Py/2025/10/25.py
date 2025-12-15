#lv1
"""
N,M = map(int,input().split())
for i in range(1,N  + 1):
  if i < M + 1:
    ans = "OK"
  else:
    ans = "Too Many Requests"
  print(ans)
"""
#oneline
"""
ans = [print("OK") if i <= x[1] else print("Too Many Requests") for x in [list(map(int,input().split()))] for i in range(1, x[0] + 1) ]
"""

#lv2
"""
"""
for i in range(input()):
    if i == 2:
        break
else:
    print("")

#lv3
"""
"""