
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [15, 2, 37, 38, 21, 30, 19, 28, 3, 35, 16, 32, 3, 28, 24, 27, 10, 1, 14, 3, 33, 6, 18, 37, 20, 19, 4, 31, 34, 39, 7, 13, 29, 38, 34, 14, 29, 13, 5, 33, 31, 24]
    tax_values = {33: 10, 13: 12, 6: 1, 15: 2, 20: 15, 4: 3, 27: 7, 35: 5, 19: 18, 14: 13, 16: 4, 2: 2, 39: 19, 21: 18, 3: 2, 37: 14, 10: 1, 24: 3, 32: 2, 7: 4, 1: 1, 5: 4, 31: 4, 34: 7, 30: 8, 28: 11, 18: 9, 29: 2, 38: 1}
    
    # Encoding other variables given in the problem statement
    target_sum = 397
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
            # Check if the coin is valid to be chosen based on the given conditions
            if (coins[i] % 2 == 0 and coins[i] > prev_coin) or (coins[i] % 2 != 0 and coins[i] <= prev_coin):
                # Calculate the new total tax by adding the tax value of the chosen coin
                new_total_tax = total_tax + tax_values[coins[i]]
                # Generate the new state
                new_coins_chosen = coins_chosen + [coins[i]]
                new_prev_coin = coins[i]
                # The cost of the new state is the total tax paid so far
                new_cost = g + tax_values[coins[i]]
                
                if new_total_tax <= target_sum and (i, new_total_tax) not in visited_costs or new_cost < visited_costs[(i, new_total_tax)]:
                    visited_costs[(i, new_total_tax)] = new_cost
                    heapq.heappush(queue, (g + new_total_tax, new_cost, new_coins_chosen, new_prev_coin, new_total_tax))
    
    return None


print(a_star())
