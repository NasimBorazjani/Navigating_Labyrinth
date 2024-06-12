
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [4, 2, 18, 5, 18, 13, 22, 15, 5, 14, 15, 21, 23, 13, 19, 22, 6, 12, 19, 8, 15, 8, 12, 15, 11, 17, 7, 19, 23, 9, 3, 4, 12, 10, 11, 2, 22, 19, 19, 11, 18, 6, 10, 23, 20, 1, 6, 23, 8, 6]
    tax_values = {21: 18, 1: 1, 13: 3, 20: 2, 19: 7, 5: 4, 18: 4, 4: 1, 15: 5, 12: 7, 17: 5, 22: 10, 8: 3, 7: 5, 23: 11, 9: 7, 10: 8, 3: 2, 14: 4, 6: 1, 2: 2, 11: 10}
    
    # Encoding other variables given in the problem statement
    target_sum = 233
    coins.sort(reverse=True)
    num_coins = len(coins)

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        coins_chosen, prev_coin, total_tax = state

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin in the list
        for i in range(coins_chosen, num_coins):
            # Check if the new state would be valid, ie the tax value of the chosen coin must satisfy the conditions given in the problem statement
            if (coins[i] % 2 == 0 and coins[i] < prev_coin) or (coins[i] % 2 != 0 and coins[i] >= prev_coin):
                new_total_tax = total_tax + tax_values[coins[i]]
                new_state = (i + 1, coins[i], new_total_tax)
                # The cost of the new state is the tax value of the chosen coin
                new_cost = g + tax_values[coins[i]]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_total_tax, new_cost, actions + [coins[i]], new_state))
    return None


print(a_star())
