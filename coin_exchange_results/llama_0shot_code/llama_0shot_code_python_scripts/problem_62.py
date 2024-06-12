
def taxed_coin_exchange(coins, taxes, target_sum):
    # Create a list of tuples, where each tuple contains a coin and its tax
    coins_with_taxes = sorted([(coin, taxes[coin]) for coin in coins], key=lambda x: x[0]-x[1], reverse=True)
    
    # Initialize a list to keep track of the total tax paid for each subset of coins
    dp = [0] * (target_sum + 1)
    
    # Use a dynamic programming algorithm to find the subset of coins that minimizes the total tax paid
    for coin, tax in coins_with_taxes:
        for i in range(target_sum, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + tax)
    
    # Find the subset of coins
    coins_chosen = []
    total_tax_paid = dp[target_sum]
    for coin, tax in reversed(coins_with_taxes):
        if total_tax_paid < dp[target_sum - coin]:
            break
        else:
            coins_chosen.append(coin)
            total_tax_paid -= tax
    
    # Return the subset of coins in Python syntax
    return '[' + ', '.join(map(str, coins_chosen[::-1])) + ']'

coins = [35, 14, 9, 23, 25, 24, 21, 20, 12, 17, 12, 5, 2, 17, 25, 25, 26, 31, 7, 21, 10, 2, 27, 19, 32, 29, 11, 33, 3, 27, 17, 3, 18, 14, 2, 32, 14, 21, 12, 8, 3, 34, 13, 12, 2, 23, 13, 3, 3, 31, 23, 23, 6, 30, 30, 11, 21]
taxes = {3: 1, 32: 16, 6: 5, 20: 13, 13: 5, 31: 9, 23: 10, 35: 14, 24: 17, 11: 11, 9: 1, 12: 10, 5: 3, 8: 5, 34: 11, 17: 16, 25: 9, 26: 6, 30: 17, 27: 17, 7: 2, 18: 17, 33: 5, 14: 2, 29: 14, 10: 3, 2: 2, 21: 12, 19: 9}
target_sum = 356

print(taxed_coin_exchange(coins, taxes, target_sum))
