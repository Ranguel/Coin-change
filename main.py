coins = [2, 5, 10, 20, 50, 100]
change = 93


def get_coin_change(coins, amount):
    coins = filter(lambda x: x <= amount, coins)
    max_val = amount + 1
    dp = [max_val] * (amount + 1)
    last_coin = [-1] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                last_coin[x] = coin

    if dp[amount] == max_val:
        return "no solution was found :("

    result = []
    current = amount
    while current > 0:
        coin = last_coin[current]
        result.append(coin)
        current -= coin
    return len(result), result


result = get_coin_change(coins, change)
print("result: ", result)
