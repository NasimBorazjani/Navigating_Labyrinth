
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [5, 29, 12, 96, 4, 13, 8, 23, 14, 25, 18, 23, 36, 32, 17, 37, 34, 7, 9, 32, 29, 37, 30, 40, 99, 9, 2, 40, 35, 14]
    tax_values = {14: 4, 4: 2, 18: 12, 23: 12, 36: 15, 5: 1, 12: 3, 13: 13, 9: 7, 32: 8, 99: 16, 8: 7, 96: 17, 35: 13, 29: 19, 30: 19, 7: 1, 34: 16, 37: 15, 2: 2, 17: 3, 40: 18, 25: 9}
    
    # Encoding other variables given in the problem statement
    target_sum = 427
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, prev_coin = heapq.heappop(queue)

        # If the total value of the coins chosen so far equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is valid based on the given conditions
            if (coin not in coins_chosen and
                ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0))):
                # Calculate the tax for the current coin
                tax = tax_values[coin]
                # Generate the new state
                new_state = (g + tax, total_value + coin, coins_chosen + [coin], coin)
                # The cost of the new state is the total tax paid so far
                new_cost = g + tax

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The priority is the total tax paid so far plus the remaining tax to reach the target sum
                    h = sum(tax_values[coin] for coin in coins if coin not in coins_chosen)
                    heapq.heappush(queue, (g + h, new_cost, coins_chosen + [coin], total_value + coin, coin))
    return None


print(a_star())
