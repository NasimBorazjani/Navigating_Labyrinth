
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [13, 3, 34, 36, 19, 31, 6, 7, 10, 24, 92, 3, 24, 33, 33, 22, 93, 13, 17, 28, 25, 16, 21, 16, 20, 26, 24, 16, 11, 18, 2, 30, 25, 23, 28, 21]
    tax_values = {3: 1, 23: 1, 34: 8, 17: 14, 20: 16, 11: 5, 28: 7, 13: 3, 22: 19, 16: 4, 26: 20, 93: 7, 31: 11, 6: 2, 36: 12, 33: 15, 18: 1, 19: 2, 7: 7, 21: 7, 10: 9, 24: 11, 30: 4, 25: 7, 2: 2, 92: 19}
    target_sum = 384

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0, 0)]

    while queue:
        _, g, coins_chosen, prev_coin, prev_tax, sum_coins = heapq.heappop(queue)

        # If the sum of the chosen coins equals the target sum, return the list of coins chosen
        if sum_coins == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is not already chosen and the sum of the coins chosen so far plus the new coin does not exceed the target sum
            if coin not in coins_chosen and sum_coins + coin <= target_sum:
                # Check if the tax value of the new coin satisfies the conditions based on the previous coin chosen
                if (coin < prev_coin and tax_values[coin] % 2 == 0) or (coin >= prev_coin and tax_values[coin] % 2 != 0):
                    # Calculate the tax paid for the new coin
                    tax_paid = prev_tax + tax_values[coin]
                    # Generate the new state
                    new_state = (coin, tax_values[coin], sum_coins + coin)
                    # The cost of the new state is the tax paid for the new coin
                    new_cost = g + tax_paid

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + tax_paid, new_cost, coins_chosen + [coin], coin, tax_values[coin], sum_coins + coin))

    return None


print(a_star())
