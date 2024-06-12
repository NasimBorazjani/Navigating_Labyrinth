
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [26, 8, 19, 9, 36, 23, 42, 40, 13, 34, 40, 25, 11, 38, 10, 41, 19, 34, 91, 18, 14, 27, 14, 43, 42, 13, 2, 27, 90, 13, 3, 4, 44, 7, 48, 40, 35, 40, 10, 12, 25]
    tax_values = {44: 20, 11: 4, 19: 3, 4: 4, 10: 3, 14: 9, 90: 18, 48: 12, 91: 5, 8: 4, 7: 5, 9: 5, 12: 2, 42: 18, 36: 6, 35: 10, 34: 12, 25: 7, 27: 1, 3: 2, 26: 15, 40: 8, 43: 1, 18: 8, 23: 1, 13: 3, 41: 8, 38: 13, 2: 2}
    
    # Encoding other variables given in the problem statement
    target_sum = 488
    coins.sort(reverse=True)
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]
    
    while queue:
        _, g, coins_chosen, total_tax, prev_coin = heapq.heappop(queue)
        
        # If the total sum of the coins chosen equals the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return coins_chosen
        
        for i in range(num_coins):
            # Check if the coin is valid based on the tax rules and the target sum
            if (coins[i] % 2 == 0 and coins[i] < prev_coin) or (coins[i] % 2 != 0 and coins[i] >= prev_coin):
                new_total_tax = total_tax + tax_values[coins[i]]
                if new_total_tax <= target_sum:
                    new_state = (g + tax_values[coins[i]], new_total_tax, coins_chosen + [coins[i]], coins[i])
                    if new_state not in visited_costs or g + tax_values[coins[i]] < visited_costs[new_state]:
                        visited_costs[new_state] = g + tax_values[coins[i]]
                        heapq.heappush(queue, (g + tax_values[coins[i]], new_total_tax, coins_chosen + [coins[i]], coins[i]))
    
    return None


print(a_star())
