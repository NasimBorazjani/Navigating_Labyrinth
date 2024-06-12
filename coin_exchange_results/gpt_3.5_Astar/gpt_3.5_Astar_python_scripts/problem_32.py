
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [19, 2, 25, 9, 6, 24, 4, 26, 17, 11, 11, 2, 17, 2, 5, 6, 3, 3, 3, 18, 26, 18, 21, 3, 5, 8, 12, 15, 8, 18, 24, 5, 19, 7, 18, 25, 12, 13, 12, 2, 25, 16, 17, 16, 3, 3]
    tax_values = {26: 12, 25: 20, 17: 13, 13: 4, 16: 13, 11: 10, 24: 5, 5: 4, 8: 6, 7: 5, 4: 4, 12: 9, 18: 12, 3: 2, 21: 17, 19: 7, 2: 2, 9: 9, 6: 2, 15: 4}

    # Encoding other variables given in the problem statement
    target_sum = 264
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0  # Initialize the cost to reach each visited state

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    # The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, prev_coin = heapq.heappop(queue)

        # If the total value of the coins chosen so far equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the new state would be valid, ie the total value of the coins chosen so far plus the new coin value does not exceed the target sum
            if total_value + coin <= target_sum:
                # Check if the new coin follows the rules of the problem
                if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                    # Calculate the tax for the new coin
                    tax = tax_values[coin]
                    # Generate the new state
                    new_state = (g + tax, total_value + coin, coins_chosen + [coin], coin)
                    # The cost of the new state is the tax paid for the new coin
                    new_cost = g + tax

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Estimate the remaining cost to reach the goal state by calculating the tax for the remaining coins
                        remaining_tax = sum(tax_values[remaining_coin] for remaining_coin in coins if remaining_coin not in coins_chosen)
                        heapq.heappush(queue, (g + tax + remaining_tax, g + tax, coins_chosen + [coin], total_value + coin, coin))
    return None


print(a_star())
