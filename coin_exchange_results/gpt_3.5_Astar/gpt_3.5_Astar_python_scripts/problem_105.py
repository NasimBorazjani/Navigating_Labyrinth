
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [26, 8, 34, 12, 20, 21, 35, 13, 28, 5, 16, 11, 24, 42, 16, 12, 34, 21, 27, 27, 20, 47, 9, 12, 38, 23, 43, 33, 26, 22, 38, 42, 20, 41, 47, 41, 24, 46, 35, 42, 9, 35, 13, 45, 24, 29, 45, 2, 41, 39, 24, 38, 39, 18, 5, 8, 36]
    tax_values = {12: 8, 18: 6, 42: 8, 11: 9, 38: 13, 9: 9, 24: 15, 34: 1, 20: 5, 2: 2, 23: 2, 33: 12, 27: 8, 39: 11, 16: 1, 28: 12, 26: 11, 21: 7, 35: 7, 22: 19, 47: 9, 29: 12, 46: 3, 45: 9, 5: 1, 13: 13, 43: 8, 36: 11, 41: 4, 8: 8}
    
    # Encoding other variables given in the problem statement
    target_sum = 477
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0  # Initialize the cost to reach the initial state as 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], (0, 0, 0))]  # The initial state is represented as (index of the coin, sum of coins chosen, total tax paid)
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Unpack the information encoded in each state
        coin_index, sum_coins, total_tax = state
        
        # If the sum of coins chosen equals the target sum, return the list of coins chosen
        if sum_coins == target_sum:
            return actions
        
        # Generate all possible actions from the current state, which includes choosing the next coin in the list
        for i in range(coin_index, num_coins):
            new_sum_coins = sum_coins + coins[i]
            new_tax = total_tax + tax_values[coins[i]]
            
            # Check if the new state would be valid, ie the sum of coins chosen does not exceed the target sum and the tax constraints are satisfied
            if new_sum_coins <= target_sum and ((coins[i] < coins[coin_index] and coins[i] % 2 == 0) or (coins[i] >= coins[coin_index] and coins[i] % 2 != 0)):
                new_state = (i + 1, new_sum_coins, new_tax)
                new_cost = g + tax_values[coins[i]]  # The additional cost of this state is the tax value of the coin chosen
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, actions + [coins[i]], new_state))
    
    return None


print(a_star())
