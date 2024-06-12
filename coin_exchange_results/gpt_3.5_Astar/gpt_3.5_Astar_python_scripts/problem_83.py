
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [12, 5, 22, 10, 4, 26, 26, 31, 13, 30, 37, 14, 14, 38, 9, 30, 7, 16, 21, 37, 4, 24, 10, 41, 13, 16, 3, 40, 24, 117, 34, 7, 11, 14, 28, 37, 21, 32, 2, 15, 5, 13, 3, 28, 31, 22, 30, 32, 38, 25, 10, 4, 30]
    tax_values = {10: 7, 2: 2, 14: 12, 15: 8, 13: 10, 9: 1, 38: 17, 117: 2, 16: 13, 25: 11, 31: 3, 32: 2, 22: 10, 7: 4, 12: 3, 4: 1, 40: 2, 34: 4, 41: 9, 30: 8, 11: 10, 26: 13, 28: 6, 3: 2, 37: 17, 5: 5, 21: 3, 24: 13}
    
    # Encoding other variables given in the problem statement
    target_sum = 411
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
        
        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(num_coins):
            # Check if the coin is valid to be chosen based on the given conditions
            if (coins[i] % 2 == 0 and coins[i] > prev_coin) or (coins[i] % 2 != 0 and coins[i] <= prev_coin):
                new_total_tax = total_tax + tax_values[coins[i]]
                # Generate the new state
                new_coins_chosen = coins_chosen + [coins[i]]
                new_state = (i, coins[i], new_coins_chosen, coins[i], new_total_tax)
                # The cost of the new state is the total tax paid so far
                new_cost = g + new_total_tax
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic as the remaining tax to be paid, assuming the remaining coins are chosen optimally
                    h = sum(tax_values[coin] for coin in coins[i+1:])
                    heapq.heappush(queue, (g + h, new_cost, new_coins_chosen, coins[i], new_total_tax))
    
    return None


print(a_star())
