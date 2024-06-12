
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [46, 10, 4, 8, 2, 22, 26, 49, 4, 19, 2, 9, 23, 28, 6, 21, 9, 14, 15, 21, 22, 3, 14, 2, 28, 13, 20, 2, 28, 7, 16, 27, 22, 18, 28, 10, 14, 14, 4, 20, 18]
    tax_values = {21: 14, 19: 16, 4: 3, 23: 10, 10: 3, 18: 7, 9: 3, 27: 13, 20: 12, 13: 9, 26: 17, 3: 3, 6: 6, 49: 16, 2: 2, 15: 7, 28: 13, 46: 10, 8: 3, 7: 6, 22: 20, 14: 5, 16: 8}
    target_sum = 294

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, prev_tax = heapq.heappop(queue)

        # If the sum of the coins chosen so far equals the target sum, return the coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is not already chosen and the sum of the coins chosen so far plus the new coin does not exceed the target sum
            if coin not in coins_chosen and sum(coins_chosen) + coin <= target_sum:
                # Check if the tax value of the new coin satisfies the conditions based on the previous coin chosen
                if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                    # Calculate the tax paid for the new coin
                    tax_paid = prev_tax + tax_values[coin]
                    # Generate the new state
                    new_coins_chosen = coins_chosen + [coin]
                    new_state = (g + tax_paid, coin, tax_paid)
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or g + tax_paid < visited_costs[new_state]:
                        visited_costs[new_state] = g + tax_paid
                        heapq.heappush(queue, (g + tax_paid, coin, new_coins_chosen, coin, tax_paid))

    return None


print(a_star())
