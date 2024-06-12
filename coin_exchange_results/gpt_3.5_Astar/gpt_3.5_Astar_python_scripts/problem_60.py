
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [28, 2, 4, 7, 11, 26, 14, 8, 23, 29, 18, 13, 26, 21, 10, 26, 8, 33, 9, 15, 4, 21, 19, 3, 7, 10, 4, 7, 16, 16, 11, 33, 12, 23, 5, 3, 26, 7, 17, 30, 22, 22, 6, 16, 18, 25, 26, 11, 13, 23, 17, 11, 20, 12]
    tax_values = {10: 6, 18: 17, 33: 15, 16: 16, 3: 2, 30: 18, 13: 3, 21: 17, 23: 4, 12: 1, 7: 6, 17: 7, 4: 2, 6: 5, 2: 2, 11: 5, 14: 14, 29: 1, 20: 7, 8: 3, 15: 7, 28: 3, 26: 8, 19: 11, 9: 9, 22: 4, 5: 5, 25: 5}
    
    # Encoding other variables given in the problem statement
    target_sum = 339
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]
    
    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)
        
        # If the total sum of the coins chosen equals the target sum, return the list of coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen
        
        for i in range(num_coins):
            # Check if the coin is valid to be chosen based on the given conditions
            if (coins[i] % 2 == 0 and coins[i] > prev_coin) or (coins[i] % 2 != 0 and coins[i] <= prev_coin):
                new_total_tax = total_tax + tax_values[coins[i]]
                # Generate the new state
                new_coins_chosen = coins_chosen + [coins[i]]
                new_state = (g + new_total_tax, new_total_tax, new_coins_chosen, coins[i], new_total_tax)
                
                if new_state not in visited_costs or g + new_total_tax < visited_costs[new_state]:
                    visited_costs[new_state] = g + new_total_tax
                    heapq.heappush(queue, (g + new_total_tax, new_total_tax, new_coins_chosen, coins[i], new_total_tax))
    
    return None


print(a_star())
