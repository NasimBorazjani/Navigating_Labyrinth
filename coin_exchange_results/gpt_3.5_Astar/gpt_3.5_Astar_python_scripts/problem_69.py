
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [28, 11, 40, 15, 21, 6, 20, 6, 12, 22, 8, 18, 34, 24, 22, 30, 35, 41, 6, 39, 5, 15, 19, 8, 26, 38, 11, 29, 31, 14, 37, 28, 8, 11, 28, 27, 38]
    tax_values = {40: 1, 41: 13, 8: 5, 28: 2, 21: 18, 15: 7, 5: 4, 14: 13, 37: 12, 22: 12, 29: 3, 30: 15, 35: 4, 26: 19, 39: 7, 31: 14, 11: 7, 20: 3, 6: 2, 12: 8, 27: 13, 19: 19, 34: 5, 18: 9, 38: 16, 24: 17}
    
    # Encoding other variables given in the problem statement
    target_sum = 423
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]
    
    while queue:
        _, g, coins_chosen, state = heapq.heappop(queue)
        
        # Unpack the information encoded in each state
        coin_index, prev_coin, total_tax = state
        
        # If the total sum of coins chosen equals the target sum, return the coins chosen
        if total_tax == target_sum:
            return coins_chosen
        
        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(coin_index, num_coins):
            # Check if the next coin follows the rules of the problem
            if (coins[i] % 2 == 0 and coins[i] > prev_coin) or (coins[i] % 2 != 0 and coins[i] <= prev_coin):
                # Calculate the tax for the current coin
                tax = tax_values[coins[i]]
                # Generate the new state
                new_state = (i + 1, coins[i], total_tax + tax)
                # The cost of the new state is the tax of the current coin
                new_cost = g + tax
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, coins_chosen + [coins[i]], new_state))
    
    return None


print(a_star())
