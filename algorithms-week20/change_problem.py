def min_num_coins(money, coins):
    min_coins = [0] + [float("inf")] * money
    for m in range(1, money + 1):
        for coin in coins:
            if coin <= m and min_coins[m - coin] + 1 < min_coins[m]:
                min_coins[m] = min_coins[m - coin] + 1
    return min_coins[money]

money = 40
coins = [50, 25, 20, 10, 5, 1]

print(min_num_coins(money, coins))
