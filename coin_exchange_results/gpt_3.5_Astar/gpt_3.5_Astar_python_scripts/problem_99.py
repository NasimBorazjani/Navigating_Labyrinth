
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [37, 4, 1, 15, 2, 7, 8, 33, 35, 14, 47, 36, 41, 44, 13, 31, 3, 7, 27, 25, 26, 38, 10, 19, 7, 18, 32, 45, 29, 35, 44, 17, 40, 13, 14, 40, 28, 15, 23, 11, 7, 16, 7, 35, 31, 45, 14, 22, 7, 36, 31]
    tax_values = {44: 2, 1: 1, 36: 14, 26: 2, 22: 10, 33: 13, 16: 12, 23: 1, 41: 6, 8: 6, 18: 3, 13: 5, 2: 2, 7: 5, 29: 13, 25: 19, 3: 1, 45: 12, 35: 13, 17: 6, 47: 13, 10: 8, 15: 14, 31: 13, 4: 2, 14: 2, 32: 11, 40: 3, 11: 4, 28: 7, 37: 12, 27: 11, 19: 17, 38: 18}
    target_sum = 465

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0, 0)]

    while queue:
        _, g, actions, total_tax, prev_coin, prev_index = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return actions

        for i, coin in enumerate(coins):
            # Check if the coin is valid based on the tax value and the previous coin chosen
            if (coin % 2 == 0 and coin > prev_coin) or (coin % 2 != 0 and coin <= prev_coin):
                new_total_tax = total_tax + tax_values[coin]
                # If the new total tax is less than the target sum, add the coin to the list of chosen coins
                if new_total_tax <= target_sum:
                    new_actions = actions + [coin]
                    # Update the cost of reaching the new state
                    new_cost = g + tax_values[coin]
                    # Update the previous coin and index for the next state
                    new_prev_coin = coin
                    new_prev_index = i
                    # If the new state is not visited or the new cost is lower than the previous cost, add it to the queue
                    if (new_prev_index, new_prev_coin, new_total_tax) not in visited_costs or new_cost < visited_costs[(new_prev_index, new_prev_coin, new_total_tax)]:
                        visited_costs[(new_prev_index, new_prev_coin, new_total_tax)] = new_cost
                        heapq.heappush(queue, (g + new_total_tax, new_cost, new_actions, new_total_tax, new_prev_coin, new_prev_index))

    return None


print(a_star())
