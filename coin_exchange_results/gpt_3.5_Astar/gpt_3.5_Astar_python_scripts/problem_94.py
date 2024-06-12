
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [21, 13, 10, 18, 21, 43, 42, 29, 14, 19, 9, 2, 15, 19, 32, 45, 24, 31, 25, 7, 21, 24, 29, 29, 4, 36, 29, 19, 29, 12, 3, 44, 40, 46, 33, 3, 28, 44, 25, 6, 36, 3, 4, 19, 31]
    tax_values = {6: 3, 9: 7, 13: 11, 19: 11, 36: 17, 32: 11, 46: 1, 4: 3, 21: 14, 3: 1, 18: 5, 29: 18, 12: 9, 2: 2, 15: 14, 43: 11, 24: 5, 25: 15, 14: 10, 42: 11, 44: 7, 31: 11, 40: 2, 33: 10, 45: 20, 7: 6, 10: 3, 28: 5}
    target_sum = 474

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0, 0)]

    while queue:
        _, g, actions, total_tax, prev_coin, index = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return actions

        for i in range(index, len(coins)):
            # Check if the coin chosen is valid based on the given conditions
            if (coins[i] % 2 == 0 and coins[i] > prev_coin) or (coins[i] % 2 != 0 and coins[i] <= prev_coin):
                new_total_tax = total_tax + tax_values[coins[i]]
                # Generate the new state
                new_state = (g + new_total_tax, new_total_tax, actions + [coins[i]], coins[i], i + 1)
                # If the new state is unvisited or we found a new path with a lower total tax, add it to the queue of unvisited states
                if new_state not in visited_costs or g + new_total_tax < visited_costs[new_state]:
                    visited_costs[new_state] = g + new_total_tax
                    heapq.heappush(queue, (g + new_total_tax, new_total_tax, actions + [coins[i]], coins[i], i + 1))

    return None


print(a_star())
