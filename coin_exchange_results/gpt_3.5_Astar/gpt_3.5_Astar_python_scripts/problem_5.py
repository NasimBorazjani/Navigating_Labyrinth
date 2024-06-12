
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [20, 10, 16, 21, 15, 21, 13, 6, 19, 9, 7, 5, 2, 6, 9, 22, 4, 13, 3, 16, 22, 18, 6, 5, 14, 7, 7, 2, 17, 9, 8, 83, 14]
    tax_values = {22: 18, 21: 1, 14: 12, 10: 8, 8: 6, 17: 9, 6: 4, 7: 6, 9: 3, 20: 13, 19: 12, 5: 3, 13: 8, 4: 3, 83: 14, 3: 2, 18: 1, 2: 1, 16: 2, 15: 3}
    target_sum = 239

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, prev_tax = heapq.heappop(queue)

        # If the sum of the coins chosen so far equals the target sum, return the list of coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is not already chosen and the sum of the coins chosen so far plus the new coin does not exceed the target sum
            if coin not in coins_chosen and sum(coins_chosen) + coin <= target_sum:
                # Check if the tax value of the new coin satisfies the conditions based on the previous coin chosen
                if (coin < prev_coin and tax_values[coin] % 2 == 0) or (coin >= prev_coin and tax_values[coin] % 2 != 0):
                    # Calculate the tax paid for the new coin
                    tax_paid = prev_tax + tax_values[coin]
                    # Generate the new state
                    new_coins_chosen = coins_chosen + [coin]
                    new_state = (g + tax_paid, coin, tax_values[coin])
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or g + tax_paid < visited_costs[new_state]:
                        visited_costs[new_state] = g + tax_paid
                        heapq.heappush(queue, (g + tax_paid, coin, new_coins_chosen, coin, tax_paid))

    return None


print(a_star())
