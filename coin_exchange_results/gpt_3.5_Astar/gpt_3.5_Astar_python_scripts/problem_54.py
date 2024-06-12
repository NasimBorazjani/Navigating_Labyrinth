
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [4, 17, 14, 12, 1, 3, 12, 10, 14, 9, 30, 20, 11, 17, 11, 16, 22, 17, 30, 5, 10, 16, 19, 27, 6, 18, 20, 19, 32, 25, 30, 15, 30, 21, 19, 25, 31, 33, 19, 10, 8, 16, 8]
    tax_values = {1: 1, 31: 13, 25: 13, 11: 3, 3: 1, 10: 8, 33: 14, 8: 4, 9: 9, 4: 1, 20: 4, 12: 8, 27: 13, 30: 14, 16: 10, 18: 9, 32: 5, 21: 20, 6: 4, 5: 5, 22: 11, 17: 11, 19: 2, 14: 10, 15: 6}
    target_sum = 328

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0, 0)]

    while queue:
        _, g, actions, prev_coin, prev_tax, prev_sum = heapq.heappop(queue)

        # If the sum of the chosen coins equals the target sum, return the list of coins chosen
        if prev_sum == target_sum:
            return actions

        for coin in coins:
            # Check if the coin is valid based on the tax rules
            if (coin > prev_coin and coin % 2 == 1) or (coin < prev_coin and coin % 2 == 0):
                new_sum = prev_sum + coin
                new_tax = prev_tax + tax_values[coin]
                # Generate the new state
                new_state = (coin, new_tax, new_sum)
                # The cost of the new state is the total tax paid so far
                new_cost = g + new_tax

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_tax, new_cost, actions + [coin], coin, new_tax, new_sum))

    return None


print(a_star())
