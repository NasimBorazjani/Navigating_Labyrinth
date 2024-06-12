
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [12, 23, 57, 18, 6, 5, 21, 15, 14, 23, 5, 16, 9, 8, 19, 8, 19, 6, 8, 3, 12, 2, 14, 3, 3, 4, 26, 6, 6, 25, 9, 13, 20, 24, 6, 26, 14, 25, 5, 26]
    tax_values = {6: 2, 12: 3, 9: 2, 2: 1, 14: 1, 16: 12, 21: 10, 4: 1, 8: 5, 26: 7, 23: 7, 57: 11, 15: 15, 19: 13, 25: 15, 13: 4, 5: 3, 24: 4, 3: 3, 18: 4, 20: 10}
    target_sum = 260

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, prev_tax = heapq.heappop(queue)

        # If the sum of the coins chosen so far equals the target sum, return the coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        for coin in coins:
            # Check if the coin is not chosen yet and the sum of the coins chosen so far plus the current coin does not exceed the target sum
            if coin not in coins_chosen and sum(coins_chosen) + coin <= target_sum:
                # Check if the tax value of the current coin satisfies the conditions based on the previous coin chosen
                if (coin < prev_coin and tax_values[coin] % 2 == 0) or (coin >= prev_coin and tax_values[coin] % 2 != 0):
                    # Calculate the tax paid for the current coin
                    tax_paid = tax_values[coin]
                    # Calculate the total tax paid so far
                    total_tax = prev_tax + tax_paid
                    # Generate the new state
                    new_coins_chosen = coins_chosen + [coin]
                    new_state = (g + total_tax, total_tax, new_coins_chosen, coin, tax_paid)

                    if new_state not in visited_costs or g + total_tax < visited_costs[new_state]:
                        visited_costs[new_state] = g + total_tax
                        heapq.heappush(queue, (g + total_tax, g + total_tax, new_coins_chosen, coin, tax_paid))

    return None


print(a_star())
