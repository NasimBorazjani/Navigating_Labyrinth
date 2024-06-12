
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [14, 29, 39, 40, 16, 35, 17, 37, 43, 30, 28, 26, 13, 13, 42, 30, 10, 7, 44, 5, 34, 7, 32, 11, 40, 35, 12, 34, 35, 38, 29, 42, 33, 26, 4, 36, 41, 35, 26, 34, 16, 6, 38, 13, 41, 23, 20]
    tax_values = {11: 4, 10: 3, 41: 9, 34: 4, 7: 2, 17: 16, 29: 8, 37: 1, 44: 8, 30: 13, 32: 9, 20: 18, 23: 8, 6: 4, 5: 3, 14: 3, 13: 7, 35: 4, 33: 5, 39: 9, 40: 11, 28: 3, 4: 2, 43: 14, 42: 15, 38: 14, 16: 5, 36: 5, 12: 9, 26: 1}
    
    # Encoding other variables given in the problem statement
    target_sum = 449
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
            # Check if the coin chosen follows the rules of the problem
            if (i == 0 or (coins[i] < coins[i-1] and coins[i] % 2 == 0) or (coins[i] >= coins[i-1] and coins[i] % 2 != 0)):
                # Calculate the new total value, total tax, and index of the last coin chosen
                new_total = sum(chosen_coins) + coins[i]
                new_tax = total_tax + tax_values[coins[i]]
                new_last_coin_index = i
                # Generate the new state
                new_state = (new_total, new_tax, new_last_coin_index)
                # The cost of the new state is the total tax paid so far
                new_cost = g + tax_values[coins[i]]
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_tax, new_cost, new_last_coin_index, chosen_coins + [coins[i]]))
    
    return None


print(a_star())
