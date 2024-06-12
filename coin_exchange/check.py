"""def is_feasible(eligible_coins_main, chosen_coins):
    eligible_coins = eligible_coins_main[:]
    for i in range(1, len(chosen_coins) - 1):
        current_coin = chosen_coins[i]
        previous_coin = chosen_coins[i - 1]
        if not current_coin in eligible_coins:
            return False
        else:
            eligible_coins.remove(current_coin)
            
        if current_coin < previous_coin and current_coin % 2 != 0:
            return False
        elif current_coin >= previous_coin and current_coin % 2 != 1:
            return False
    
    return True

        
def is_correct(eligible_coins, target, chosen_coins):
    feasible = is_feasible(eligible_coins, chosen_coins)
    if feasible and sum(chosen_coins) == target:
        return True, len(chosen_coins)
    
    return False, None"""
   


"""eligible_coins = [31, 39, 52, 6, 44, 28, 38, 10, 5, 3, 33, 26, 28, 3, 33, 24, 14, 2, 41, 24, 3, 11, 18, 35, 24, 47, 29]
target = 107
chosen_coins = [28, 41, 38]
print(is_correct(eligible_coins, target, chosen_coins))"""

        
def is_feasible(eligible_coins_main, chosen_coins):
    eligible_coins = eligible_coins_main[:]
    
    if not chosen_coins[0] in eligible_coins:
        return False
    else:
        eligible_coins.remove(chosen_coins[0])
            
    for i in range(1, len(chosen_coins)):
        current_coin = chosen_coins[i]
        previous_coin = chosen_coins[i - 1]
        if not current_coin in eligible_coins:
            return False
        else:
            eligible_coins.remove(current_coin)
            
        if current_coin < previous_coin and current_coin % 2 != 0:
            return False
        elif current_coin >= previous_coin and current_coin % 2 != 1:
            return False
    
    return True


def is_correct(eligible_coins, tax_values, target, chosen_coins):
    feasible = is_feasible(eligible_coins, chosen_coins)
    if feasible and sum(chosen_coins) == target:
        tax = 0
        for coin in chosen_coins:
            #after laoding the problems in json format keys turn into strings
            if str(coin) in tax_values:
                tax += tax_values[str(coin)]
            else:
                tax += tax_values[coin]
        return True, tax
    
    return False, None


"""coins = [11, 24, 3, 37, 32, 31, 23, 1, 29, 25, 5, 25, 3, 1, 32, 26, 9, 31, 18, 16, 33, 12, 27, 24, 9, 6, 27, 8, 15, 8, 11, 35, 3, 11, 27]
tax = {9: 3, 27: 7, 18: 5, 26: 17, 33: 20, 6: 6, 12: 4, 35: 1, 1: 1, 37: 12, 11: 9, 16: 15, 25: 13, 23: 8, 32: 2, 31: 5, 29: 3, 8: 4, 3: 3, 24: 17, 5: 2, 15: 14}
goal_sum = 267
chosen_coins = [6, 31, 31, 18, 27, 12, 29, 32, 32, 9, 35, 5]
print(is_correct(coins, tax, goal_sum, chosen_coins))"""
print(is_correct([
                3,
                6,
                9,
                10,
                13,
                15,
                18,
                5,
                21,
                19,
                12,
                15,
                5,
                9,
                4,
                16,
                8,
                4,
                7,
                7,
                7,
                2,
                16,
                14,
                18,
                3,
                89,
                21,
                12,
                10,
                7,
                14,
                4,
                11,
                6,
                20
            ],
            {
                "14": 1,
                "89": 13,
                "2": 2,
                "5": 2,
                "4": 4,
                "6": 6,
                "8": 2,
                "16": 5,
                "21": 4,
                "20": 2,
                "18": 9,
                "11": 10,
                "10": 3,
                "12": 12,
                "15": 5,
                "13": 1,
                "3": 1,
                "19": 19,
                "7": 7,
                "9": 3
            },
            229,  [3, 89, 20, 14, 21, 14, 8, 13, 21, 16, 10]))

