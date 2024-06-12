
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [25, 22, 26, 12, 18, 12, 5, 6, 6, 21, 28, 26, 6, 26, 9, 11, 27, 24, 16, 1, 12, 5, 10, 23, 11, 10, 28, 2, 3, 7, 23, 28, 27, 12, 3, 3, 27, 21, 13, 8, 18, 25, 6, 7, 9, 25, 18, 18, 23, 12, 11, 15, 2, 16]
    tax_values = {10: 6, 24: 14, 5: 3, 3: 1, 16: 6, 27: 10, 13: 1, 12: 4, 21: 17, 8: 2, 28: 10, 6: 3, 1: 1, 18: 2, 25: 14, 11: 3, 23: 7, 7: 6, 26: 16, 15: 4, 2: 1, 9: 3, 22: 8}
    target_sum = 289

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0, 0)]

    while queue:
        _, g, actions, total_tax, prev_coin, coins_index = heapq.heappop(queue)

        if total_tax == target_sum:
            return actions

        for i in range(coins_index, len(coins)):
            coin = coins[i]
            tax = tax_values[coin]

            if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                new_total_tax = total_tax + tax
                if new_total_tax <= target_sum:
                    new_state = (g + new_total_tax, new_total_tax, actions + [coin], coin, i + 1)
                    if new_state not in visited_costs or g + new_total_tax < visited_costs[new_state]:
                        visited_costs[new_state] = g + new_total_tax
                        heapq.heappush(queue, (g + new_total_tax, new_total_tax, actions + [coin], coin, i + 1))

    return None


print(a_star())
