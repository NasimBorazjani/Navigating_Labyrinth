
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [6, 20, 15, 14, 23, 6, 8, 15, 11, 2, 16, 21, 17, 10, 23, 20, 21, 16, 13, 3, 7, 4, 9, 21, 7, 13, 10, 18, 11, 9, 13, 12, 15, 17, 2, 8, 18, 3, 16, 9, 3, 14, 23, 16]
    tax_values = {21: 11, 18: 16, 16: 6, 12: 5, 14: 11, 11: 8, 15: 11, 4: 3, 9: 2, 23: 14, 7: 5, 20: 12, 6: 2, 8: 3, 17: 6, 13: 3, 3: 3, 2: 1, 10: 5}
    target_sum = 236

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
        if sum(coins[i] for i in coins_chosen) == target_sum:
            return [coins[i] for i in coins_chosen]

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for i, coin in enumerate(coins):
            # Check if the coin has not been chosen yet and the tax conditions are satisfied
            if i not in coins_chosen and ((coin < prev_coin and coin % 2 == 0) or (coin >= prev_coin and coin % 2 != 0)):
                # Calculate the new total tax with the addition of the tax value of the current coin
                new_total_tax = total_tax + tax_values[coin]
                # Generate the new state
                new_state = (coins_chosen + [i], coin, new_total_tax)
                # The cost of the new state is the total tax paid so far
                new_cost = new_total_tax

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the remaining tax to be paid, as we aim to minimize the total tax
                    h = sum(tax_values[coins[i]] for i in range(len(coins)) if i not in coins_chosen)
                    heapq.heappush(queue, (g + h, new_cost, actions + [coin], new_state))
    return None


print(a_star())
