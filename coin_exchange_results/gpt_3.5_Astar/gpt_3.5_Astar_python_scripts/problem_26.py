
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [29, 29, 22, 23, 23, 3, 26, 9, 15, 8, 21, 15, 29, 25, 71, 27, 23, 6, 7, 9, 15, 21, 6, 8, 19, 17, 18, 6, 26, 24, 24, 3, 25, 2]
    tax_values = {24: 14, 2: 1, 25: 2, 26: 14, 18: 12, 27: 15, 29: 19, 19: 3, 15: 7, 9: 1, 8: 1, 21: 18, 6: 1, 71: 3, 23: 4, 17: 7, 7: 2, 22: 11, 3: 1}
    
    # Encoding other variables given in the problem statement
    target_sum = 307
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]
    
    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)
        
        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return coins_chosen
        
        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(num_coins):
            # Check if the coin is valid to choose based on the tax value constraints
            if (coins[i] % 2 == 0 and coins[i] > prev_coin) or (coins[i] % 2 != 0 and coins[i] <= prev_coin):
                new_total_tax = total_tax + tax_values[coins[i]]
                # Generate the new state
                new_coins_chosen = coins_chosen + [coins[i]]
                new_prev_coin = coins[i]
                new_cost = g + tax_values[coins[i]]
                
                if (i, new_total_tax) not in visited_costs or new_cost < visited_costs[(i, new_total_tax)]:
                    visited_costs[(i, new_total_tax)] = new_cost
                    heapq.heappush(queue, (g + new_total_tax, new_cost, new_coins_chosen, new_prev_coin, new_total_tax))
    
    return None


print(a_star())
