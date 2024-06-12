
import heapq
import math


def a_star():
    # Define the list of coins and their tax values
    coins = [12, 26, 9, 14, 11, 25, 28, 17, 18, 18, 9, 16, 2, 11, 31, 25, 4, 23, 9, 3, 24, 22, 3, 14, 32, 30, 19, 7, 4, 22, 33, 13, 25, 15, 14, 28, 20, 3, 4, 3, 32, 10, 6, 29, 25]
    tax_values = {29: 2, 9: 7, 17: 4, 18: 9, 26: 6, 33: 11, 16: 12, 4: 3, 31: 12, 6: 2, 11: 8, 23: 14, 7: 1, 30: 8, 12: 8, 13: 2, 20: 13, 24: 16, 14: 8, 19: 8, 10: 8, 32: 14, 3: 2, 2: 2, 25: 19, 22: 18, 15: 5, 28: 9}
    
    # Encoding other variables given in the problem statement
    target_sum = 325
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], (0, 0, 0))]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Unpack the information encoded in each state
        coins_chosen, prev_coin, total_tax = state
        
        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return actions
        
        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(num_coins):
            # Check if the coin is not already chosen
            if i not in coins_chosen:
                # Check if the coin chosen is valid based on the tax rules
                if (coins[i] > coins[prev_coin] and tax_values[coins[i]] % 2 != 0) or (coins[i] < coins[prev_coin] and tax_values[coins[i]] % 2 == 0):
                    # Generate the new state
                    new_state = (coins_chosen + [i], i, total_tax + tax_values[coins[i]])
                    # The additional cost of this state is the tax value of the coin chosen
                    new_cost = g + tax_values[coins[i]]
                    
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Relaxing the constraints on the target sum to calculate the heuristic
                        h = target_sum - total_tax
                        heapq.heappush(queue, (g + h, new_cost, actions + [coins[i]], new_state))
    return None


print(a_star())
