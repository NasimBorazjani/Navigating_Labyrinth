
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [2, 27, 9, 80, 20, 81, 13, 24, 16, 6, 26, 12, 3, 26, 20, 8, 16, 8, 20, 22, 9, 34, 23, 8, 12, 34, 4, 6, 22, 19]
    tax_values = {12: 9, 16: 12, 13: 5, 34: 8, 9: 9, 23: 4, 81: 2, 80: 20, 8: 1, 19: 19, 2: 2, 22: 13, 20: 7, 26: 11, 4: 1, 6: 2, 27: 4, 3: 1, 24: 12}
    target_sum = 346

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the coins chosen
        if total_tax == target_sum:
            return coins_chosen

        for coin in coins:
            # Check if the coin is valid based on the given conditions
            if (coin not in coins_chosen and
                ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0))):
                new_total_tax = total_tax + tax_values[coin]
                new_coins_chosen = coins_chosen + [coin]
                new_state = (g + new_total_tax, new_total_tax, new_coins_chosen, coin, new_total_tax)

                if new_state not in visited_costs or g + new_total_tax < visited_costs[new_state]:
                    visited_costs[new_state] = g + new_total_tax
                    heapq.heappush(queue, (g + new_total_tax, new_total_tax, new_coins_chosen, coin, new_total_tax))

    return None


print(a_star())
