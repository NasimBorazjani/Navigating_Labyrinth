
import heapq
import math


def a_star():
    # Define the list of coins and their tax values
    coins = [22, 25, 37, 5, 46, 10, 23, 23, 3, 6, 34, 32, 34, 2, 3, 8, 4, 28, 32, 24, 15, 38, 17, 35, 9, 12, 12, 22, 34, 48, 39, 30, 7, 18, 10, 46, 30, 36, 49, 27, 22, 19, 9, 24, 43, 15]
    tax_values = {18: 11, 17: 7, 7: 6, 43: 2, 22: 3, 24: 11, 9: 3, 36: 10, 46: 4, 10: 3, 39: 5, 5: 5, 35: 15, 28: 8, 15: 2, 34: 6, 27: 3, 38: 11, 30: 20, 23: 18, 25: 10, 12: 1, 4: 1, 49: 16, 37: 6, 48: 17, 2: 2, 8: 4, 3: 1, 6: 3, 19: 10, 32: 19}
    
    # Encoding other variables given in the problem statement
    target_sum = 463
    coins.sort()
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize the priority queue with the initial state, where the total sum and total tax are 0, and the index of the current coin is 0
    queue = [(0, 0, 0, [])]
    
    while queue:
        _, g, total_sum, current_index, selected_coins = heapq.heappop(queue)
        
        # If the total sum equals the target sum, return the selected coins
        if total_sum == target_sum:
            return selected_coins
        
        # Generate all possible actions from the current state, which includes selecting the next coin or skipping it
        for i in range(current_index, num_coins):
            new_sum = total_sum + coins[i]
            new_tax = tax_values[coins[i]]
            # Check if the new sum does not exceed the target sum
            if new_sum <= target_sum:
                # Check if the coin chosen follows the given rules
                if (not selected_coins or 
                    (coins[i] < selected_coins[-1] and coins[i] % 2 == 0) or 
                    (coins[i] >= selected_coins[-1] and coins[i] % 2 != 0)):
                    new_state = (g + new_tax, new_sum, i + 1, selected_coins + [coins[i]])
                    # The cost of the new state is the total tax paid so far
                    new_cost = g + new_tax
                    
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Relaxing the constraints on the total sum to calculate the heuristic
                        h = target_sum - new_sum
                        heapq.heappush(queue, (g + h, new_cost, new_sum, i + 1, selected_coins + [coins[i]]))
    
    return None


print(a_star())
