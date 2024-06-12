
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [14, 2, 5, 8, 65, 5, 16, 2, 5, 2, 12, 17, 16, 15, 20, 4, 19, 9, 10, 64, 2, 10, 14, 2, 17]
    tax_values = {20: 13, 4: 2, 17: 16, 19: 8, 64: 4, 5: 3, 14: 10, 10: 9, 65: 11, 16: 2, 12: 7, 8: 5, 2: 2, 15: 14, 9: 8}
    target_sum = 208

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize the priority queue with the initial state, where the total value, total tax, and index of the last coin chosen are all 0
    queue = [(0, 0, 0, [])]

    while queue:
        _, total_value, total_tax, last_coin_index, chosen_coins = heapq.heappop(queue)

        # If the total value of the chosen coins equals the target sum, return the list of chosen coins
        if total_value == target_sum:
            return chosen_coins

        for i in range(last_coin_index, len(coins)):
            # Check if the coin chosen is valid based on the given conditions
            if (i == 0 or (coins[i] < coins[i-1] and coins[i] % 2 == 0) or (coins[i] >= coins[i-1] and coins[i] % 2 != 0)):
                new_total_value = total_value + coins[i]
                new_total_tax = total_tax + tax_values[coins[i]]
                new_state = (new_total_value, new_total_tax, i+1)
                new_chosen_coins = chosen_coins + [coins[i]]

                # If the new state is valid and has not been visited before, add it to the priority queue
                if new_state not in visited_costs or new_total_tax < visited_costs[new_state]:
                    visited_costs[new_state] = new_total_tax
                    heapq.heappush(queue, (new_total_tax, new_total_value, new_total_tax, i+1, new_chosen_coins))

    return None


print(a_star())
