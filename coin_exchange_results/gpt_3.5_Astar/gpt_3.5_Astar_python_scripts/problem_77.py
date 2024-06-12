
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [26, 32, 14, 36, 14, 8, 9, 3, 8, 18, 7, 23, 6, 20, 34, 8, 37, 19, 15, 6, 2, 13, 37, 7, 31, 2, 7, 4, 17, 9, 4, 22, 7, 16, 33, 14, 11, 30, 36, 14, 34, 37, 36, 37, 32, 38, 15, 17, 19, 14]
    tax_values = {17: 16, 4: 2, 15: 2, 8: 1, 19: 5, 9: 4, 23: 7, 3: 2, 16: 13, 2: 1, 38: 13, 11: 2, 31: 6, 7: 6, 36: 8, 14: 8, 37: 17, 32: 5, 6: 1, 13: 11, 22: 9, 20: 8, 18: 4, 30: 6, 34: 2, 33: 1, 26: 3}
    
    # Encoding other variables given in the problem statement
    target_sum = 396
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first
    num_coins = len(coins)

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0  # Initialize the cost to reach the initial state as 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        total_sum, prev_coin, prev_tax = state

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_sum == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin in the list
        for i in range(num_coins):
            coin = coins[i]
            tax = tax_values[coin]

            # Check if the coin chosen is valid based on the given conditions
            if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                new_total_sum = total_sum + coin
                new_tax = prev_tax + tax
                new_state = (new_total_sum, coin, new_tax)
                new_cost = g + tax

                if new_total_sum <= target_sum and (new_state not in visited_costs or new_cost < visited_costs[new_state]):
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_tax, new_cost, actions + [coin], new_state))

    return None


print(a_star())
