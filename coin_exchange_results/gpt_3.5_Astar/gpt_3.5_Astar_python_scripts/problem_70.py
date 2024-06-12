
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [30, 28, 81, 26, 24, 20, 5, 18, 33, 19, 30, 27, 6, 10, 22, 10, 33, 10, 15, 26, 9, 6, 22, 31, 36, 16, 4, 11, 24, 7, 17, 30, 3, 7, 8, 8, 34]
    tax_values = {24: 7, 22: 3, 11: 10, 28: 17, 7: 7, 20: 10, 5: 2, 8: 2, 9: 5, 15: 14, 81: 17, 30: 5, 31: 17, 33: 9, 18: 3, 36: 2, 16: 14, 10: 1, 19: 15, 3: 1, 34: 12, 26: 13, 6: 3, 4: 1, 27: 11, 17: 5}
    target_sum = 387

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize the priority queue with the initial state, where the total value, total tax, and index of the last coin chosen are all 0
    queue = [(0, 0, 0, [])]

    while queue:
        _, total_value, total_tax, last_coin_index, chosen_coins = heapq.heappop(queue)

        # If the total value of the chosen coins equals the target sum, return the list of chosen coins
        if total_value == target_sum:
            return chosen_coins

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(last_coin_index, len(coins)):
            coin = coins[i]
            # Check if the coin chosen is valid based on the given conditions
            if (coin % 2 == 0 and coin > coins[last_coin_index]) or (coin % 2 != 0 and coin <= coins[last_coin_index]):
                # Calculate the new total value and total tax after choosing the coin
                new_total_value = total_value + coin
                new_total_tax = total_tax + tax_values[coin]
                # Generate the new state
                new_state = (new_total_value, new_total_tax, i + 1)
                # If the new state is unvisited or we found a new path with a lower total tax, add it to the queue
                if new_state not in visited_costs or new_total_tax < visited_costs[new_state]:
                    visited_costs[new_state] = new_total_tax
                    heapq.heappush(queue, (new_total_tax, new_total_value, i + 1, chosen_coins + [coin]))

    return None


print(a_star())
