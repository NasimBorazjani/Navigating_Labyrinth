
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [5, 15, 15, 77, 12, 38, 41, 30, 31, 30, 13, 19, 9, 2, 23, 37, 14, 34, 29, 22, 22, 4, 16, 2, 12, 17, 9, 18, 19, 21, 4, 28, 40, 11, 30, 24, 19, 9, 10, 76, 34]
    tax_values = {13: 8, 29: 10, 4: 4, 2: 2, 77: 17, 16: 10, 11: 2, 22: 18, 17: 10, 18: 18, 38: 7, 9: 6, 5: 2, 41: 14, 31: 3, 12: 10, 19: 5, 24: 16, 40: 6, 14: 4, 34: 13, 15: 3, 23: 20, 76: 16, 37: 2, 21: 2, 28: 3, 10: 2, 30: 16}
    
    # Encoding other variables given in the problem statement
    target_sum = 419
    coins.sort()
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]
    
    while queue:
        _, g, coins_chosen, total_tax, last_coin_index = heapq.heappop(queue)
        
        # If the total sum of coins chosen equals the target sum, return the coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen
        
        # Generate all possible actions from the current state, which includes choosing the next coin in the list
        for i in range(last_coin_index, num_coins):
            new_coin = coins[i]
            # Check if the new coin can be chosen based on the given conditions
            if (new_coin % 2 == 0 and new_coin > coins_chosen[-1]) or (new_coin % 2 != 0 and new_coin <= coins_chosen[-1]):
                # Calculate the tax for the new coin
                new_tax = tax_values[new_coin]
                # Generate the new state
                new_coins_chosen = coins_chosen + [new_coin]
                new_total_tax = total_tax + new_tax
                new_state = (g + new_tax, new_total_tax, new_coins_chosen, i)
                
                # If the new state is unvisited or we found a new path with a lower total tax, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_total_tax < visited_costs[new_state]:
                    visited_costs[new_state] = new_total_tax
                    heapq.heappush(queue, (g + new_tax, new_total_tax, new_coins_chosen, i))
    
    return None


print(a_star())
