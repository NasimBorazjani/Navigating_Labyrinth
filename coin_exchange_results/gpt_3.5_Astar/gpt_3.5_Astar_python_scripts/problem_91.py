
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [36, 40, 17, 7, 15, 23, 18, 26, 29, 24, 15, 43, 13, 12, 31, 33, 30, 31, 26, 37, 14, 31, 43, 25, 30, 7, 37, 27, 221, 13, 26, 21]
    tax_values = {36: 14, 27: 19, 21: 6, 13: 8, 23: 17, 26: 17, 15: 6, 25: 7, 31: 20, 30: 5, 18: 14, 12: 6, 37: 2, 221: 18, 14: 13, 24: 10, 33: 4, 43: 11, 29: 18, 40: 1, 7: 6, 17: 2}
    target_sum = 445

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, prev_tax = heapq.heappop(queue)

        # If the sum of the coins chosen so far equals the target sum, return the list of coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        for coin in coins:
            # Check if the coin is valid based on the tax value constraints
            if (coin > prev_coin and coin % 2 == 1) or (coin < prev_coin and coin % 2 == 0):
                new_tax = prev_tax + tax_values[coin]
                new_cost = g + new_tax

                if new_cost <= visited_costs.get((len(coins_chosen) + 1, coin, new_tax), float('inf')):
                    visited_costs[(len(coins_chosen) + 1, coin, new_tax)] = new_cost
                    heapq.heappush(queue, (g + new_tax, new_cost, coins_chosen + [coin], coin, new_tax))

    return None


print(a_star())
