
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [12, 15, 3, 24, 10, 18, 10, 20, 21, 17, 9, 8, 2, 11, 5, 5, 3, 8, 6, 12, 20, 22, 4, 5, 17, 5, 14, 10, 15, 8, 9, 22, 4, 7, 15, 16, 4, 2, 5, 9, 24, 23, 3, 7, 20, 9, 12, 10, 4, 4, 8, 24, 11, 20, 2, 15]
    tax_values = {20: 14, 15: 15, 6: 1, 14: 1, 7: 2, 18: 5, 2: 1, 16: 5, 21: 9, 3: 3, 12: 3, 17: 10, 22: 4, 10: 9, 4: 3, 11: 1, 5: 1, 23: 13, 24: 4, 9: 9, 8: 4}
    target_sum = 246

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, total_tax = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        for coin in coins:
            # Check if the coin is not already chosen and the sum of coins chosen so far plus the current coin does not exceed the target sum
            if coin not in coins_chosen and sum(coins_chosen) + coin <= target_sum:
                # Check if the coin follows the rules of being even if smaller than the previous coin, and odd if larger or equal to the previous coin
                if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                    # Calculate the tax for the current coin
                    tax = tax_values[coin]
                    # Calculate the new total tax
                    new_total_tax = total_tax + tax
                    # Generate the new state
                    new_coins_chosen = coins_chosen + [coin]
                    new_state = (g + new_total_tax, g + 1, new_coins_chosen, coin, new_total_tax)

                    if new_state not in visited_costs or g + new_total_tax < visited_costs[new_state]:
                        visited_costs[new_state] = g + new_total_tax
                        heapq.heappush(queue, (g + new_total_tax, g + 1, new_coins_chosen, coin, new_total_tax))

    return None


print(a_star())
