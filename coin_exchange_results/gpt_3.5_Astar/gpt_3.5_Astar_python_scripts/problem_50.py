
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [19, 14, 29, 19, 29, 9, 17, 16, 25, 7, 8, 2, 23, 11, 28, 6, 29, 16, 19, 31, 30, 15, 7, 16, 23, 23, 10, 32, 8, 14, 7, 9, 6, 23, 77, 24, 22, 24, 22]
    tax_values = {15: 6, 29: 12, 19: 3, 30: 18, 14: 2, 77: 3, 6: 5, 17: 1, 32: 16, 9: 8, 22: 15, 31: 17, 25: 10, 24: 1, 28: 11, 2: 2, 7: 4, 8: 7, 11: 7, 23: 19, 10: 2, 16: 2}
    target_sum = 351

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
        for coin in coins:
            # Check if the coin is not already chosen and the total sum plus the coin value does not exceed the target sum
            if coin not in coins_chosen and total_sum + coin <= target_sum:
                # Check if the coin follows the rules of being even if smaller than the previous coin, and odd if larger or equal
                if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                    # Calculate the tax for the current coin
                    tax = tax_values[coin]
                    # Generate the new state
                    new_state = (total_sum + coin, coin, tax)
                    # The cost of the new state is the tax of the current coin plus the total tax paid so far
                    new_cost = g + tax_values[coin]
                    
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + new_cost, new_cost, coins_chosen + [coin], new_state))
    return None


print(a_star())
