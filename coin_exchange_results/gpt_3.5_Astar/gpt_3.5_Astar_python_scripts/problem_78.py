
import heapq


def a_star():
    # Define the list of coins and the target sum
    coins = [29, 32, 2, 34, 7, 25, 7, 14, 33, 1, 26, 18, 13, 11, 32, 31, 13, 2, 28, 21, 38, 8, 11, 28, 26, 9, 4, 28, 34, 23, 18, 31, 35, 2, 25, 20, 15, 5, 12, 10, 7, 14, 17, 4, 13, 24, 11, 16, 14, 27, 29]
    target_sum = 392
    # Define the tax values for each coin
    tax_values = {10: 1, 25: 18, 1: 1, 15: 7, 12: 1, 23: 16, 9: 7, 27: 15, 29: 16, 28: 2, 32: 12, 24: 6, 5: 1, 8: 1, 11: 8, 17: 13, 13: 6, 38: 6, 31: 19, 4: 2, 34: 12, 21: 3, 2: 2, 33: 12, 20: 13, 18: 1, 14: 13, 16: 8, 7: 5, 35: 16, 26: 10}
    # Encoding other variables of the problem
    num_coins = len(coins)
    coins_set = set(coins)
    coins.sort()

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        coins_chosen, prev_coin, total_tax = state

        # If the total sum of the coins chosen equals the target sum, return the coins chosen
        if total_tax == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is not already chosen and the total tax does not exceed the target sum
            if coin not in coins_set and total_tax + tax_values[coin] <= target_sum:
                # Check if the coin follows the rules of being even if smaller than the previous coin and odd if larger or equal to the previous coin
                if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                    # Generate the new state
                    new_state = (coins_chosen + 1, coin, total_tax + tax_values[coin])
                    # The additional cost of this state is the tax value of the chosen coin
                    new_cost = g + tax_values[coin]

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + new_cost, new_cost, actions + [coin], new_state))
    return None


print(a_star())
