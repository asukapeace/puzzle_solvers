import random

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]

def main():
    coins = input("Enter the coins (separated by spaces): ")
    coins = [int(coin) for coin in coins.split()]

    total = random.randint(1, 100)
    print(f"Random total: {total}")

    result = coin_change(coins, total)

    if result == -1:
        print("It's not possible to make change for the total.")
    else:
        print(f"Minimum number of coins needed: {result}")

if __name__ == "__main__":
    main()