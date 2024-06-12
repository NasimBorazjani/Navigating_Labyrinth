
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [10, 16, 2, 18, 10, 16, 17, 32, 18, 33, 23, 20, 21, 25, 32, 24, 10, 27, 13, 27, 30, 13, 19, 20, 4, 5, 15, 8, 8, 34, 21, 14, 3, 20, 10, 18, 3, 14, 28, 6, 4, 8, 15, 4, 30, 30, 12, 20, 14, 10]
    tax_values = {30: 12, 20: 19, 16: 7, 24: 14, 12: 3, 13: 4, 8: 2, 2: 1, 21: 2, 23: 12, 34: 13, 27: 16, 3: 3, 28: 3, 14: 13, 6: 4, 33: 17, 10: 8, 5: 3, 15: 12, 4: 2, 18: 2, 19: 5, 17: 1, 32: 2, 25: 12}
    target_sum = 357

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0, 0)]

    while queue:
        _, g, actions, total_tax, prev_coin, index = heapq.heappop(queue)

        if total_tax == target_sum:
            return actions

        for i in range(index, len(coins)):
            coin = coins[i]
            tax = tax_values[coin]
            new_total_tax = total_tax + tax

            # Check if the coin is valid based on the given conditions
            if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                new_actions = actions + [coin]
                new_state = (g + new_total_tax, new_total_tax, new_actions, coin, i + 1)

                if new_state not in visited_costs or g + new_total_tax < visited_costs[new_state]:
                    visited_costs[new_state] = g + new_total_tax
                    heapq.heappush(queue, (g + new_total_tax, new_total_tax, new_actions, coin, i + 1))

    return None


print(a_star())
