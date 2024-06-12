
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [5, 21, 4, 18, 17, 13, 27, 10, 27, 21, 25, 22, 27, 29, 28, 15, 16, 12, 7, 19, 8, 19, 9, 21, 29, 15, 15, 23, 8, 13, 20, 9, 13, 16, 3, 14, 11, 15, 2, 23, 18, 4]
    tax_values = {14: 2, 12: 11, 20: 5, 4: 2, 23: 12, 28: 1, 25: 8, 27: 3, 19: 1, 21: 6, 16: 2, 29: 7, 13: 5, 17: 2, 22: 15, 10: 1, 15: 1, 3: 2, 8: 5, 5: 4, 9: 1, 7: 2, 2: 2, 18: 17, 11: 1}
    
    # Encoding other variables given in the problem statement
    target_sum = 295
    coins.sort()
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Unpack the information encoded in each state
        coins_chosen, prev_coin, total_tax = state
        
        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if sum(coins[i] for i in coins_chosen) == target_sum:
            return [coins[i] for i in coins_chosen]
        
        # Generate all possible actions from the current state, which includes choosing the next coin in the list
        for i in range(num_coins):
            # Check if the new state would be valid, ie if the coin chosen satisfies the conditions given in the problem statement
            if i not in coins_chosen and ((coins[i] < coins[prev_coin] and coins[i] % 2 == 0) or (coins[i] >= coins[prev_coin] and coins[i] % 2 != 0)):
                # Calculate the tax for the new coin
                new_tax = total_tax + tax_values[coins[i]]
                # Generate the new state
                new_state = (coins_chosen + [i], i, new_tax)
                # The cost of the new state is the total tax paid so far
                new_cost = g + new_tax
                
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The new coin chosen must be added to the list of actions
                    heapq.heappush(queue, (g + new_tax, new_cost, actions + [coins[i]], new_state))
    
    return None


print(a_star())
