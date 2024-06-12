
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [25, 22, 28, 23, 5, 14, 28, 14, 20, 6, 22, 1, 25, 18, 30, 10, 19, 12, 17, 17, 6, 28, 21, 28, 21, 2, 20, 2, 19, 14, 31, 31, 14, 7, 20, 13, 7, 18, 22, 15, 6, 6, 21, 9, 18, 11, 20, 26, 15]
    tax_values = {11: 1, 14: 4, 7: 2, 25: 4, 12: 5, 20: 19, 13: 6, 15: 11, 30: 18, 1: 1, 2: 2, 31: 6, 10: 2, 23: 1, 6: 2, 21: 18, 18: 8, 28: 15, 17: 5, 26: 6, 22: 6, 9: 1, 19: 2, 5: 4}
    target_sum = 322

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, actions, prev_coin, prev_tax = heapq.heappop(queue)

        # Calculate the sum of the coins chosen so far
        current_sum = sum(coins[i] for i in actions)

        # If the sum of the chosen coins equals the target sum, return the list of coins chosen
        if current_sum == target_sum:
            return actions

        for i, coin in enumerate(coins):
            # Check if the coin is valid based on the tax value and the previous coin chosen
            if (coin not in actions and
                ((coin < prev_coin and tax_values[coin] % 2 == 0) or
                 (coin >= prev_coin and tax_values[coin] % 2 != 0))):
                
                # Calculate the new tax value based on the previous tax value and the tax value of the current coin
                new_tax = prev_tax + tax_values[coin]
                # Calculate the new cost based on the tax value of the current coin
                new_cost = g + tax_values[coin]

                # If the new state is not visited or the new cost is lower than the cost of the previous visit, add it to the queue
                if (i not in visited_costs or new_cost < visited_costs[i]):
                    visited_costs[i] = new_cost
                    heapq.heappush(queue, (g + new_tax, new_cost, actions + [i], coin, new_tax))

    return None


print(a_star())