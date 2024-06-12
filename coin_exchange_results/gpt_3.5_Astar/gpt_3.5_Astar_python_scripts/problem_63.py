
import heapq


def a_star():
    # Define the list of coins and the target sum
    coins = [12, 12, 5, 32, 25, 3, 23, 49, 31, 6, 12, 23, 20, 14, 34, 17, 16, 16, 21, 18, 7, 30, 7, 27, 29, 14, 5, 9, 48, 33, 5, 18, 15, 29, 2, 28, 29, 25, 26, 6, 4, 4, 6, 8, 16, 5, 4, 4, 20, 25, 10, 6, 3, 24, 19]
    target_sum = 348

    # Define the tax values for each coin
    tax_values = {20: 18, 16: 6, 19: 2, 27: 12, 25: 2, 6: 2, 26: 16, 23: 9, 28: 12, 49: 16, 33: 13, 30: 12, 8: 6, 21: 18, 31: 16, 48: 5, 15: 5, 10: 2, 3: 1, 29: 14, 32: 15, 5: 3, 4: 4, 34: 3, 17: 14, 12: 11, 7: 3, 9: 9, 14: 7, 24: 14, 18: 15, 2: 1}

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_sum, prev_coin = heapq.heappop(queue)

        # If the total sum of the coins chosen equals the target sum, return the list of coins chosen
        if total_sum == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is valid to choose based on the given conditions
            if (coin not in coins_chosen and
                (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0)):
                # Calculate the new total sum and the tax paid for choosing the coin
                new_total_sum = total_sum + coin
                tax_paid = tax_values[coin]
                new_cost = g + tax_paid

                # If the new total sum does not exceed the target sum, add the new state to the queue
                if new_total_sum <= target_sum:
                    new_coins_chosen = coins_chosen + [coin]
                    if (new_total_sum, coin, tax_paid) not in visited_costs or new_cost < visited_costs[(new_total_sum, coin, tax_paid)]:
                        visited_costs[(new_total_sum, coin, tax_paid)] = new_cost
                        heapq.heappush(queue, (g + tax_paid, new_cost, new_coins_chosen, new_total_sum, coin))

    return None


print(a_star())
