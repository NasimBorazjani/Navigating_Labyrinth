
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [31, 83, 19, 4, 13, 27, 13, 18, 21, 24, 9, 3, 2, 30, 16, 14, 31, 29, 27, 23, 18, 8, 32, 3, 3, 25, 17, 8, 32, 5, 2, 28, 30, 26, 25, 12, 12]
    tax_values = {32: 1, 19: 12, 3: 1, 27: 14, 5: 3, 9: 5, 13: 11, 14: 10, 28: 6, 31: 15, 8: 8, 18: 18, 17: 7, 2: 2, 12: 9, 24: 16, 83: 6, 23: 9, 16: 15, 29: 4, 25: 5, 26: 18, 4: 1, 21: 10, 30: 10}
    target_sum = 335

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize the priority queue with the initial state, where the total value, total tax, and index of the last coin chosen are all 0
    queue = [(0, 0, 0, [])]

    while queue:
        _, g, last_coin_index, chosen_coins = heapq.heappop(queue)

        # If the total value of the chosen coins equals the target sum, return the list of chosen coins
        if sum(chosen_coins) == target_sum:
            return chosen_coins

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(last_coin_index, len(coins)):
            # Check if the coin chosen is valid based on the tax values and the previous coin chosen
            if (not chosen_coins or
                (coins[i] < chosen_coins[-1] and tax_values[coins[i]] % 2 == 0) or
                (coins[i] >= chosen_coins[-1] and tax_values[coins[i]] % 2 != 0)):
                # Generate the new state by adding the chosen coin to the list of chosen coins
                new_chosen_coins = chosen_coins + [coins[i]]
                # Calculate the new total value and total tax
                new_total_value = sum(new_chosen_coins)
                new_total_tax = sum(tax_values[coin] for coin in new_chosen_coins)
                # The cost of the new state is the total tax paid
                new_cost = new_total_tax

                if (new_total_value, new_total_tax, i) not in visited_costs or new_cost < visited_costs[(new_total_value, new_total_tax, i)]:
                    visited_costs[(new_total_value, new_total_tax, i)] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, i, new_chosen_coins))

    return None


print(a_star())
