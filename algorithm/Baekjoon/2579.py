# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# graph = [0]
# dp = [0] * (n + 1)
#
# for _ in range(n):
#     graph.append(int(input()))
#
# cnt = 0
# for i in range(1, n + 1):
#
#     if cnt == 0:
#         dp[i] = dp[i - 1] + graph[i]
#         if i == n - 2:
#             cnt = 2
#         else:
#             cnt = 1
#     elif cnt == 1:
#         if i == n:
#             dp[i] = dp[i - 1] + graph[i]
#             break
#         if graph[i] < graph[i + 1]:
#             dp[i] = dp[i - 1]
#             cnt = 0
#         elif graph[i] >= graph[i + 1]:
#             dp[i] = dp[i - 1] + graph[i]
#             cnt = 2
#     elif cnt == 2:
#         dp[i] = dp[i - 1]
#         cnt = 0
# print(dp[-1])

n=int(input()) # 계단 개수
s=[int(input()) for _ in range(n)] # 계단 리스트
dp=[0]*(n) # dp 리스트
if len(s)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(s))
else: # 계단이 3개 이상일 때
    dp[0]=s[0] # 첫째 계단 수동 계산
    dp[1]=s[0]+s[1] # 둘째 계단까지 수동 계산
    for i in range(2,n): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i]=max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
    print(dp[-1])