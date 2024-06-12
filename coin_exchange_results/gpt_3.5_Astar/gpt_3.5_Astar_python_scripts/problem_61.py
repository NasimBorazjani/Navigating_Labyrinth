
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [30, 4, 10, 25, 2, 20, 23, 22, 29, 13, 21, 23, 23, 24, 3, 26, 29, 27, 15, 18, 28, 10, 22, 24, 2, 22, 13, 32, 8, 28, 31, 13, 27, 6, 35, 2, 20, 25, 24, 2, 16, 31, 3, 5, 23, 32, 24, 20, 13, 7, 11, 12]
    tax_values = {10: 8, 32: 8, 25: 5, 7: 2, 30: 9, 18: 3, 5: 2, 35: 14, 2: 1, 15: 10, 12: 6, 29: 14, 23: 12, 31: 14, 11: 3, 8: 7, 21: 5, 13: 3, 28: 3, 6: 1, 3: 2, 4: 2, 22: 5, 16: 9, 24: 4, 27: 16, 26: 6, 20: 20}
    
    # Encoding other variables given in the problem statement
    target_sum = 351
    coins.sort()
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize the priority queue with the initial state, where the total value, total tax, and index of the last coin chosen are all 0
    queue = [(0, 0, 0, [])]
    
    while queue:
        _, g, total_tax, last_coin_index, chosen_coins = heapq.heappop(queue)
        
        # If the total value of the chosen coins equals the target sum, return the chosen coins
        if sum(chosen_coins) == target_sum:
            return chosen_coins
        
        for i in range(last_coin_index, num_coins):
            # Check if the coin chosen is valid based on the given conditions
            if (not chosen_coins or (coins[i] < chosen_coins[-1] and coins[i] % 2 == 0) or (coins[i] >= chosen_coins[-1] and coins[i] % 2 != 0)):
                # Calculate the new total value, total tax, and add the new coin to the chosen coins
                new_total_value = sum(chosen_coins) + coins[i]
                new_total_tax = total_tax + tax_values[coins[i]]
                new_chosen_coins = chosen_coins + [coins[i]]
                
                # If the new state is valid and has not been visited before, add it to the queue
                if new_total_value <= target_sum and (i, new_total_tax, new_total_value) not in visited_costs:
                    visited_costs[(i, new_total_tax, new_total_value)] = 0
                    heapq.heappush(queue, (g + new_total_tax, g + 1, new_total_tax, i, new_chosen_coins))
    
    return None


print(a_star())
