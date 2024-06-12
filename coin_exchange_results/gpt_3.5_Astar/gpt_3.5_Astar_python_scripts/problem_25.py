
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [28, 5, 25, 22, 26, 13, 20, 20, 18, 28, 7, 20, 18, 19, 18, 5, 15, 23, 28, 27, 22, 10, 8, 17, 3, 8, 5, 11, 21, 17, 65, 23, 11, 3, 12]
    tax_values = {20: 12, 21: 3, 5: 2, 3: 2, 7: 1, 15: 8, 8: 7, 27: 6, 17: 8, 18: 14, 28: 5, 13: 1, 23: 4, 65: 8, 26: 8, 22: 5, 25: 3, 11: 11, 12: 8, 19: 19, 10: 7}
    
    # Encoding other variables given in the problem statement
    target_sum = 284
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]
    
    while queue:
        _, g, coins_chosen, state = heapq.heappop(queue)
        
        # Unpack the information encoded in each state
        total_sum, prev_coin, prev_tax = state
        
        # If the total sum of coins chosen equals the target sum, return the coins chosen
        if total_sum == target_sum:
            return coins_chosen
        
        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(num_coins):
            coin = coins[i]
            tax = tax_values[coin]
            
            # Check if the coin can be chosen based on the given conditions
            if (coin % 2 == 0 and coin > prev_coin) or (coin % 2 != 0 and coin <= prev_coin):
                new_total_sum = total_sum + coin
                new_tax = prev_tax + tax
                new_state = (new_total_sum, coin, new_tax)
                
                # The cost of the new state is the total tax paid so far
                new_cost = g + tax
                
                if new_total_sum <= target_sum and (new_state not in visited_costs or new_cost < visited_costs[new_state]):
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_tax, new_cost, coins_chosen + [coin], new_state))
    
    return None


print(a_star())
