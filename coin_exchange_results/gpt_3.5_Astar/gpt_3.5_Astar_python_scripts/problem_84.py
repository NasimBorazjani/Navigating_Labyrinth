
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [17, 4, 35, 10, 42, 11, 10, 11, 2, 14, 29, 31, 33, 3, 38, 4, 32, 9, 19, 14, 4, 39, 6, 36, 31, 25, 40, 8, 33, 31, 11, 34, 18, 2, 32, 40, 4, 16, 1, 36, 37, 3, 33, 20, 10, 8, 9, 20, 14, 35, 36, 22, 35, 4]
    tax_values = {37: 11, 10: 3, 36: 8, 32: 3, 3: 1, 18: 16, 14: 5, 35: 5, 16: 15, 8: 5, 42: 20, 29: 4, 6: 1, 25: 9, 11: 4, 20: 15, 39: 6, 38: 14, 34: 6, 40: 11, 9: 2, 17: 6, 19: 8, 4: 4, 22: 20, 31: 3, 1: 1, 33: 18, 2: 2}
    
    # Encoding other variables given in the problem statement
    target_sum = 426
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first
    num_coins = len(coins)

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        total_sum, prev_coin, prev_tax = state

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_sum == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i in range(num_coins):
            coin = coins[i]
            tax = tax_values[coin]

            # Check if the new state would be valid, ie the total sum of coins chosen does not exceed the target sum
            if total_sum + coin <= target_sum:
                # Check if the coin chosen follows the rules of the problem
                if (coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0):
                    # Generate the new state
                    new_state = (total_sum + coin, coin, tax)
                    # The cost of the new state is the tax value of the coin chosen
                    new_cost = g + tax

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + tax, new_cost, actions + [coin], new_state))
    return None


print(a_star())
