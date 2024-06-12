
import heapq


def a_star():
    # Define the list of coins and the target sum
    coins = [27, 17, 6, 5, 20, 3, 4, 29, 25, 27, 20, 18, 18, 25, 2, 13, 15, 4, 12, 4, 26, 12, 26, 24, 17, 23, 2, 6, 2, 29, 3, 20, 12, 7, 9, 12, 26, 11, 2, 5, 10, 25, 3, 13, 7, 25]
    target_sum = 295

    # Define the tax values for each coin
    tax_values = {2: 1, 13: 11, 26: 13, 5: 1, 4: 2, 9: 8, 15: 8, 18: 6, 20: 18, 3: 1, 17: 17, 6: 2, 10: 10, 12: 1, 23: 10, 7: 6, 29: 13, 25: 15, 11: 10, 27: 2, 24: 18}

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_sum, prev_coin = heapq.heappop(queue)

        # If the total sum equals the target sum, return the coins chosen
        if total_sum == target_sum:
            return coins_chosen

        for coin in coins:
            # Check if the coin is valid based on the tax rules
            if (coin % 2 == 0 and coin > prev_coin) or (coin % 2 != 0 and coin <= prev_coin):
                new_sum = total_sum + coin
                new_tax = g + tax_values[coin]
                new_state = (g + new_tax, new_sum, coins_chosen + [coin], coin)

                if new_state not in visited_costs or new_tax < visited_costs[new_state]:
                    visited_costs[new_state] = new_tax
                    heapq.heappush(queue, (g + new_tax, new_sum, coins_chosen + [coin], coin))

    return None


print(a_star())
