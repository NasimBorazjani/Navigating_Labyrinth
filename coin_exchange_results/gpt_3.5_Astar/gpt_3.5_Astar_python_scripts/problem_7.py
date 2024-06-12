
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [41, 4, 22, 8, 5, 5, 20, 4, 3, 19, 4, 13, 3, 18, 20, 9, 15, 3, 3, 14, 3, 14, 9, 4, 15, 19, 6, 15, 22, 19, 3, 3, 20, 9, 20, 11, 22, 15, 20]
    tax_values = {20: 11, 15: 13, 9: 7, 8: 3, 3: 1, 6: 3, 5: 2, 13: 11, 4: 4, 22: 11, 19: 19, 11: 1, 14: 2, 41: 16, 18: 18}
    target_sum = 220

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize the priority queue with the initial state, where the total value, total tax, and index of the last coin chosen are all 0
    queue = [(0, 0, 0, [])]

    while queue:
        _, g, last_coin, chosen_coins = heapq.heappop(queue)

        # If the total value of the chosen coins equals the target sum, return the chosen coins
        if sum(chosen_coins) == target_sum:
            return chosen_coins

        for coin in coins:
            # Check if the coin can be chosen based on the given conditions
            if (coin > chosen_coins[-1] and coin % 2 == 1) or (coin < chosen_coins[-1] and coin % 2 == 0):
                # Calculate the new total value, total tax, and index of the last coin chosen
                new_value = sum(chosen_coins) + coin
                new_tax = sum(tax_values[c] for c in chosen_coins) + tax_values[coin]
                new_last_coin = coin
                # Generate the new state
                new_state = (new_value, new_tax, new_last_coin)
                # Calculate the cost of the new state as the total tax paid
                new_cost = new_tax

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, new_last_coin, chosen_coins + [coin]))

    return None


print(a_star())
