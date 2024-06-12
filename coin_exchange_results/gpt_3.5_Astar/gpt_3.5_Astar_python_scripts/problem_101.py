
import heapq


def a_star():
    # Define the list of coins and the target sum
    coins = [29, 25, 15, 12, 40, 23, 36, 22, 16, 24, 51, 34, 46, 29, 20, 14, 21, 27, 15, 31, 15, 17, 9, 42, 30, 45, 14, 14, 30, 16, 44, 32, 6, 15, 5, 41, 18, 43, 36, 31, 27, 26, 6, 44, 33, 23, 7, 19]
    target_sum = 477

    # Define the tax values for each coin
    tax_values = {41: 15, 22: 3, 9: 4, 34: 9, 32: 11, 36: 5, 18: 5, 40: 9, 46: 11, 45: 17, 33: 3, 14: 9, 12: 12, 7: 2, 43: 14, 25: 18, 31: 9, 51: 8, 24: 18, 17: 3, 16: 5, 19: 10, 6: 6, 27: 15, 42: 7, 23: 2, 29: 2, 21: 13, 30: 7, 44: 4, 5: 2, 20: 11, 26: 12, 15: 8}

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, actions, total_sum, total_tax = heapq.heappop(queue)

        # If the total sum of the chosen coins equals the target sum, return the list of coins chosen
        if total_sum == target_sum:
            return actions

        for coin in coins:
            # Check if the coin is not already chosen
            if coin not in actions:
                # Check if the coin satisfies the conditions based on the previous coin chosen
                if not actions or (coin < actions[-1] and coin % 2 == 0) or (coin >= actions[-1] and coin % 2 != 0):
                    # Calculate the new total sum and total tax
                    new_sum = total_sum + coin
                    new_tax = total_tax + tax_values[coin]
                    # If the new total sum does not exceed the target sum, add the coin to the list of chosen coins
                    if new_sum <= target_sum:
                        new_actions = actions + [coin]
                        # The cost of the new state is the total tax paid so far
                        new_cost = g + new_tax

                        if (new_sum, new_tax) not in visited_costs or new_cost < visited_costs[(new_sum, new_tax)]:
                            visited_costs[(new_sum, new_tax)] = new_cost
                            heapq.heappush(queue, (g + new_tax, new_cost, new_actions, new_sum, new_tax))

    return None


print(a_star())
