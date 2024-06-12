
import heapq

def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [21, 31, 30, 31, 10, 17, 13, 35, 12, 2, 16, 40, 23, 10, 29, 13, 23, 2, 9, 5, 107, 46, 23, 11, 42, 9, 46, 28, 44, 22, 106, 10]
    tax_values = {13: 9, 106: 19, 28: 20, 44: 14, 9: 6, 35: 6, 22: 19, 46: 17, 11: 7, 40: 12, 17: 15, 10: 4, 12: 6, 30: 20, 2: 2, 23: 11, 42: 10, 16: 1, 107: 11, 21: 12, 5: 3, 31: 13, 29: 20}
    target_sum = 465

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, actions, prev_coin, total_tax = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return actions

        for coin in coins:
            # Check if the coin is valid based on the tax rules
            if (coin > prev_coin and coin % 2 == 1) or (coin < prev_coin and coin % 2 == 0):
                new_total_tax = total_tax + tax_values[coin]
                new_state = (coin, new_total_tax, g + tax_values[coin])
                if new_state not in visited_costs or g + tax_values[coin] < visited_costs[new_state]:
                    visited_costs[new_state] = g + tax_values[coin]
                    heapq.heappush(queue, (g + tax_values[coin], new_total_tax, actions + [coin], coin, new_total_tax))

    return None

print(a_star())
