
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [19, 21, 16, 6, 34, 23, 8, 10, 14, 10, 59, 15, 17, 32, 11, 15, 8, 29, 58, 12, 3, 5, 11, 34, 2, 12, 20, 6, 29, 23, 10, 34, 33, 18]
    tax_values = {6: 5, 17: 7, 12: 10, 34: 9, 5: 1, 11: 7, 10: 8, 21: 19, 15: 3, 33: 6, 3: 2, 16: 12, 58: 19, 8: 7, 14: 5, 20: 8, 2: 2, 19: 19, 59: 14, 18: 15, 29: 8, 23: 6, 32: 5}
    
    # Encoding other variables given in the problem statement
    target_sum = 355
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]
    
    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)
        
        # If the total sum of coins chosen equals the target sum, return the coins chosen
        if total_tax == target_sum:
            return coins_chosen
        
        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(num_coins):
            # Check if the coin is valid to be chosen based on the given conditions
            if (coins[i] % 2 == 0 and coins[i] > prev_coin) or (coins[i] % 2 != 0 and coins[i] <= prev_coin):
                new_total_tax = total_tax + tax_values[coins[i]]
                # Generate the new state
                new_coins_chosen = coins_chosen + [coins[i]]
                new_prev_coin = coins[i]
                # The cost of the new state is the total tax paid so far
                new_cost = new_total_tax
                
                if (i, new_total_tax, new_coins_chosen) not in visited_costs or new_cost < visited_costs[(i, new_total_tax, new_coins_chosen)]:
                    visited_costs[(i, new_total_tax, new_coins_chosen)] = new_cost
                    heapq.heappush(queue, (g + new_total_tax, new_cost, new_coins_chosen, new_prev_coin, new_total_tax))
    
    return None


print(a_star())
