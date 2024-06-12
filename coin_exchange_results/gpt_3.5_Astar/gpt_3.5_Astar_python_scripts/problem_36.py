
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [26, 7, 24, 27, 19, 15, 12, 13, 19, 5, 17, 26, 20, 7, 3, 21, 22, 7, 17, 13, 28, 11, 19, 18, 9, 10, 25, 2, 4, 18, 14, 17, 22, 27, 14, 7, 9, 2, 11, 8, 14, 10, 18, 1, 4, 24, 2, 24, 11, 14, 27]
    tax_values = {13: 8, 27: 5, 21: 13, 25: 11, 22: 6, 20: 14, 12: 1, 14: 12, 2: 2, 8: 5, 3: 2, 18: 4, 1: 1, 9: 9, 10: 1, 19: 10, 11: 5, 28: 10, 5: 3, 26: 7, 7: 1, 24: 9, 4: 3, 15: 2, 17: 13}
    
    # Encoding other variables given in the problem statement
    target_sum = 281
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
        
        # Generate all possible actions from the current state, which includes choosing the next coin in the list
        for i in range(last_coin_index, num_coins):
            new_total = total_tax + tax_values[coins[i]]
            # Check if the new state is valid, ie the tax value of the chosen coin satisfies the conditions
            if (i == 0 and coins[i] % 2 == 0) or (i > 0 and ((coins[i] >= coins[i-1] and coins[i] % 2 == 1) or (coins[i] < coins[i-1] and coins[i] % 2 == 0))):
                new_state = (sum(chosen_coins) + coins[i], new_total, i+1)
                new_cost = g + tax_values[coins[i]]
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_total, new_total, i+1, chosen_coins + [coins[i]]))
    
    return None


print(a_star())
