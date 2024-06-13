
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




