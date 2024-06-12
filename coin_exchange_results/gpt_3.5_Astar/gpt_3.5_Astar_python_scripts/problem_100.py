
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [19, 11, 3, 37, 9, 29, 42, 12, 2, 13, 15, 11, 25, 14, 31, 17, 24, 45, 5, 18, 42, 21, 28, 23, 26, 40, 27, 42, 12, 13, 16, 14, 31, 38, 9, 24, 27, 36, 13, 27, 15, 43, 9, 14, 34, 7, 15, 12, 31, 44]
    tax_values = {37: 7, 45: 7, 29: 6, 27: 2, 2: 2, 40: 6, 13: 9, 17: 2, 9: 2, 15: 12, 36: 2, 26: 18, 44: 5, 42: 4, 38: 8, 43: 2, 12: 4, 24: 20, 28: 15, 16: 7, 21: 13, 23: 5, 19: 4, 25: 16, 3: 2, 18: 13, 34: 16, 31: 2, 5: 4, 14: 2, 7: 1, 11: 8}
    target_sum = 449

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0, 0)]

    while queue:
        _, g, actions, prev_coin, prev_tax, prev_odd = heapq.heappop(queue)

        # Calculate the total value of coins chosen so far
        total_value = sum(coins[coin] for coin in actions)

        # If the total value equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return actions

        for i, coin in enumerate(coins):
            # Check if the coin is valid based on the tax rules
            if (coin not in actions and
                ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0)) and
                (coin + total_value <= target_sum)):
                
                # Calculate the tax for the current coin
                tax = tax_values[coin]

                # Calculate the new total tax
                new_tax = prev_tax + tax

                # Calculate the new odd/even status for the current coin
                new_odd = coin % 2

                # Calculate the new cost
                new_cost = g + new_tax

                # Update the visited costs dictionary
                if (i, new_tax, new_odd) not in visited_costs or new_cost < visited_costs[(i, new_tax, new_odd)]:
                    visited_costs[(i, new_tax, new_odd)] = new_cost
                    heapq.heappush(queue, (g + new_tax, new_cost, actions + [i], coin, new_tax, new_odd))

    return None


print(a_star())
