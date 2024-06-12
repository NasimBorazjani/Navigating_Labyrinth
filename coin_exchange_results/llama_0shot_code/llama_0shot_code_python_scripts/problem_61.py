
def taxed_coin_exchange(coins, taxes):
    # Create a list of tuples, where each tuple contains a coin and its tax
    coins_with_taxes = sorted([(coin, taxes[coin]) for coin in coins], key=lambda x: x[0]-x[1], reverse=True)
    
    # Initialize a list to keep track of the total tax paid for each subset of coins
    total_taxes = [0] * (len(coins_with_taxes) + 1)
    
    # Use a dynamic programming algorithm to find the subset of coins that minimizes the total tax paid
    for i in range(1, len(coins_with_taxes) + 1):
        coin, tax = coins_with_taxes[i-1]
        total_taxes[i] = min(total_taxes[i], total_taxes[i-1] + tax)
        for j in range(i-1):
            if coin >= coins_with_taxes[j][0]:
                total_taxes[i] = min(total_taxes[i], total_taxes[j] + tax)
            else:
                break
    
    # Find the subset of coins
    result = []
    i = len(coins_with_taxes)
    while i > 0:
        coin, tax = coins_with_taxes[i-1]
        if total_taxes[i-1] < total_taxes[i] - tax:
            i -= 1
        else:
            result.insert(0, coin)
            total_taxes[i-1] = total_taxes[i] - tax
            coins_with_taxes.pop(i-1)
    
    # Return the result list
    return result

coins = [30, 4, 10, 25, 2, 20, 23, 22, 29, 13, 21, 23, 23, 24, 3, 26, 29, 27, 15, 18, 28, 10, 22, 24, 2, 22, 13, 32, 8, 28, 31, 13, 27, 6, 35, 2, 20, 25, 24, 2, 16, 31, 3, 5, 23, 32, 24, 20, 13, 7, 11, 12]
taxes = {10: 8, 32: 8, 25: 5, 7: 2, 30: 9, 18: 3, 5: 2, 35: 14, 2: 1, 15: 10, 12: 6, 29: 14, 23: 12, 31: 14, 11: 3, 8: 7, 21: 5, 13: 3, 28: 3, 6: 1, 3: 2, 4: 2, 22: 5, 16: 9, 24: 4, 27: 16, 26: 6, 20: 20}
print(taxed_coin_exchange(coins, taxes))
