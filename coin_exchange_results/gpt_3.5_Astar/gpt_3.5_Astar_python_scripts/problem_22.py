
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [10, 2, 5, 22, 15, 3, 4, 66, 3, 11, 21, 16, 69, 2, 19, 20, 9, 24, 24, 20, 12, 13, 21, 7, 7, 23, 25, 10]
    tax_values = {66: 17, 9: 3, 15: 10, 7: 6, 3: 3, 13: 7, 11: 10, 25: 14, 22: 18, 24: 17, 12: 6, 23: 18, 2: 2, 10: 5, 19: 10, 20: 19, 5: 4, 16: 1, 21: 20, 69: 14, 4: 4}
    
    # Encoding other variables given in the problem statement
    target_sum = 268
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
        
        for i in range(num_coins):
            # Check if the coin is valid based on the tax rules provided
            if (coins[i] % 2 == 0 and coins[i] > prev_coin) or (coins[i] % 2 != 0 and coins[i] <= prev_coin):
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
