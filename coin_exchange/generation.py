import random
import collections


def generate(min_target, max_target, num_coins, seed = 1):
    random.seed(seed)
    max_tax = 20
    
    # Generate random target amount
    target = random.randint(min_target, max_target)
    
    max_coin = target//10
    min_coin = 2
    
    # getting the number of random coin values
    num_random_coins = random.randint(1, num_coins//2)
    
    num_coins_sums_target = num_coins - num_random_coins
    coins_sums_target = []
    
    for _ in range(num_coins_sums_target - 1):
        if sum(coins_sums_target) == target:
            num_random_coins = num_coins - len(coins_sums_target)
            break
        elif target - sum(coins_sums_target) <= min_coin:
            coins_sums_target.append(target - sum(coins_sums_target))
            num_random_coins = num_coins - len(coins_sums_target)
            break
        rand_c = random.randint(min_coin, min(target - sum(coins_sums_target), max_coin))
        coins_sums_target.append(rand_c)
        
    # Append the remaining value to the list so the sum equals the target
    if sum(coins_sums_target) < target:
        coins_sums_target.append(target - sum(coins_sums_target))
    
    #order of coins that sum up to the target can be increasing odd coins then decreasing even coins based on the rules
    #for this to be possible the largest even number must be smaller than or equal to the largest odd number 
    even_numbers = [num for num in coins_sums_target if num % 2 == 0]
    odd_numbers = [num for num in coins_sums_target if num % 2 != 0]
    
    if even_numbers and odd_numbers:
        while max(even_numbers) > max(odd_numbers):
            max_odd_index = coins_sums_target.index(max(odd_numbers))
            coins_sums_target[max_odd_index] += 2
            odd_numbers = [num for num in coins_sums_target if num % 2 != 0]

            max_even_index = coins_sums_target.index(max(even_numbers))
            coins_sums_target[max_even_index] -= 2
            even_numbers = [num for num in coins_sums_target if num % 2 == 0]
        
    random_coins = [random.randint(2, max_coin) for _ in range(num_coins)]
    
    coins = random_coins + coins_sums_target
    
    random.shuffle(coins)
    
    tax_values = {coin:random.randint(1, min(coin, max_tax)) for coin in set(coins)}
    items = list(tax_values.items())
    random.shuffle(items)
    tax_values = dict(collections.OrderedDict(items))
    
    return coins, tax_values, target
        

"""coins,tax ,target = generate(50, 150, 12, 3)
print(f'coins: {coins}, Target amount: {target}', tax)"""