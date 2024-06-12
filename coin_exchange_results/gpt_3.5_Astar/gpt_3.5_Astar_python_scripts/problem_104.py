
import heapq
import math


def a_star():
    # Define the list of coins and their tax values
    coins = [18, 23, 23, 36, 27, 10, 25, 14, 6, 43, 6, 31, 5, 43, 3, 13, 16, 8, 11, 6, 39, 44, 41, 28, 12, 8, 1, 14, 22, 23, 11, 24, 37, 9, 2, 31, 27, 10, 9, 38, 37, 4, 4, 17, 18, 36, 18, 32, 3, 12, 4, 42, 8, 4, 4, 16, 30, 40, 13, 41]
    tax_values = {6: 4, 18: 3, 38: 1, 23: 2, 16: 8, 12: 2, 4: 2, 24: 13, 28: 17, 30: 17, 1: 1, 9: 9, 27: 8, 11: 4, 37: 16, 41: 19, 13: 3, 31: 8, 44: 8, 22: 7, 43: 13, 10: 3, 17: 8, 36: 7, 39: 3, 25: 17, 40: 10, 8: 6, 32: 16, 14: 4, 2: 1, 42: 3, 3: 2, 5: 2}
    
    # Encoding other variables given in the problem statement
    target_sum = 441
    coins_set = set(coins)
    coins_set.discard(0)  # Remove 0 from the set of coins
    coins_set = sorted(list(coins_set))  # Sort the coins in ascending order
    num_coins = len(coins_set)

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0, 0)]

    while queue:
        _, g, actions, total_tax, prev_coin, num_chosen = heapq.heappop(queue)

        # If the total sum of the chosen coins equals the target sum, return the list of chosen coins
        if total_tax == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(num_coins):
            coin = coins_set[i]
            tax = tax_values[coin]
            # Check if the new state would be valid, ie the tax value of the chosen coin must satisfy the given conditions
            if ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0)):
                new_total_tax = total_tax + tax
                new_num_chosen = num_chosen + 1
                # If the new state is unvisited or we found a new path with a lower total tax, add it to the queue of unvisited states
                if new_total_tax <= target_sum and (new_num_chosen, new_total_tax) not in visited_costs:
                    visited_costs[(new_num_chosen, new_total_tax)] = 1
                    heapq.heappush(queue, (g + new_total_tax, new_total_tax, actions + [coin], new_total_tax, coin, new_num_chosen))

    return None


print(a_star())
