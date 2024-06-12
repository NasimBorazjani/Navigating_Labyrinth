
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [38, 36, 40, 31, 39, 29, 36, 31, 16, 14, 16, 45, 40, 45, 257, 8, 39, 16, 2, 41, 9, 26, 22, 24]
    tax_values = {9: 6, 14: 9, 24: 8, 26: 12, 16: 6, 45: 14, 8: 3, 22: 8, 38: 9, 40: 14, 31: 9, 257: 11, 36: 2, 2: 1, 41: 6, 29: 6, 39: 4}
    target_sum = 452

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)

        # If the total tax paid is minimized and the sum of the chosen coins equals the target sum, return the coins chosen
        if total_tax == min_tax and sum(coins_chosen) == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is valid to be chosen based on the given conditions
            if (coin not in coins_chosen and
                ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0))):
                # Calculate the tax for the current coin
                coin_tax = tax_values[coin]
                # Calculate the new total tax paid
                new_total_tax = total_tax + coin_tax
                # Generate the new state
                new_state = (g + coin_tax, g + coin_tax, coins_chosen + [coin], coin, new_total_tax)

                if new_state not in visited_costs or g + coin_tax < visited_costs[new_state]:
                    visited_costs[new_state] = g + coin_tax
                    # The priority is the sum of the cost so far and the estimated remaining cost, which is the difference between the target sum and the current sum of chosen coins
                    heapq.heappush(queue, (g + coin_tax + target_sum - sum(coins_chosen), g + coin_tax, coins_chosen + [coin], coin, new_total_tax))

    return None


# Calculate the minimum total tax that can be paid
min_tax = sum([tax_values[coin] for coin in coins])

print(a_star())
