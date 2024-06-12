
import heapq

def a_star():
    # Define the list of coins and the target sum
    coins = [11, 6, 147, 6, 19, 29, 28, 32, 18, 20, 12, 22, 4, 20, 27, 3, 3, 18, 19, 9, 2, 28, 31, 20, 2, 27, 22, 30, 3]
    target_sum = 324
    # Define the tax values for each coin
    tax_values = {27: 18, 6: 2, 22: 12, 18: 11, 4: 3, 12: 4, 28: 6, 147: 10, 32: 6, 19: 3, 29: 12, 31: 19, 20: 4, 2: 2, 30: 17, 3: 2, 11: 10, 9: 2}
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, prev_coin = heapq.heappop(queue)

        # If the total value of the coins chosen equals the target sum, return the coins chosen
        if total_value == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i, coin in enumerate(coins):
            # Check if the coin is valid to choose based on the tax rules
            if (coin > prev_coin and coin % 2 == 1) or (coin < prev_coin and coin % 2 == 0):
                # Calculate the new total value and tax paid
                new_total_value = total_value + coin
                new_tax_paid = g + tax_values[coin]
                # Generate the new state
                new_coins_chosen = coins_chosen + [coin]
                new_state = (new_tax_paid, new_total_value, new_coins_chosen, coin)
                
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_tax_paid < visited_costs[new_state]:
                    visited_costs[new_state] = new_tax_paid
                    heapq.heappush(queue, (g + new_tax_paid, new_tax_paid, new_coins_chosen, new_total_value, coin))
    
    return None

print(a_star())
