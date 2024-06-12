
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [1, 2, 17, 12, 7, 17, 2, 20, 4, 4, 17, 19, 15, 16, 18, 21, 18, 10, 3, 9, 12, 13, 8, 16, 9, 14, 13, 5, 13, 6, 20, 6, 13, 12, 8, 14, 15, 7, 10, 3, 16, 16, 9, 3, 2, 6, 9, 14, 16, 20, 11, 4, 17]
    tax_values = {8: 5, 5: 2, 19: 2, 4: 4, 9: 2, 3: 1, 2: 2, 12: 1, 13: 6, 6: 5, 11: 1, 17: 14, 7: 4, 16: 13, 21: 10, 14: 13, 1: 1, 18: 12, 10: 10, 15: 11, 20: 20}
    
    # Encoding other variables given in the problem statement
    target_sum = 213
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0  # Initialize the cost to reach the initial state as 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, prev_coin = heapq.heappop(queue)

        # If the total value of the coins chosen so far equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return coins_chosen

        for coin in coins:
            # Check if the coin is valid to be chosen based on the given conditions
            if (coin not in coins_chosen and
                ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0))):
                new_total_value = total_value + coin
                new_tax = tax_values[coin]
                new_cost = g + new_tax

                if new_total_value <= target_sum and (new_total_value, new_tax, coin) not in visited_costs:
                    visited_costs[(new_total_value, new_tax, coin)] = new_cost
                    heapq.heappush(queue, (g + new_tax, new_cost, coins_chosen + [coin], new_total_value, coin))

    return None


print(a_star())
