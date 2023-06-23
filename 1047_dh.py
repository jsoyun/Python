import sys
sys.stdin = open('1047.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
print("coins:",coins)

count = 0
for coin in coins:
    print("coin",coin)
    count += K // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    print("K",K ,"coin",coin)
    print("count:",count)
    print()
    K %= coin #나머지를 할당

print(count)
