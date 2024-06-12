
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [33, 4, 5, 9, 31, 26, 25, 19, 31, 33, 24, 6, 13, 17, 15, 37, 7, 21, 3, 23, 22, 7, 3, 11, 19, 28, 24, 32, 27, 31, 24, 12, 23, 22, 16, 6, 33, 8, 19, 13, 5, 11, 10, 4, 8, 16, 14, 17, 13, 9, 25, 17]
    tax_values = {3: 3, 19: 1, 5: 2, 9: 4, 17: 4, 24: 11, 8: 5, 22: 10, 4: 2, 32: 10, 16: 1, 37: 5, 23: 12, 26: 18, 12: 1, 27: 9, 14: 5, 25: 13, 15: 8, 6: 6, 21: 13, 10: 3, 31: 17, 7: 3, 33: 10, 11: 2, 28: 10, 13: 10}
    
    # Encoding other variables given in the problem statement
    target_sum = 389
    coins.sort(reverse=True)  # Sort the coins in descending order to prioritize larger coins first
    num_coins = len(coins)

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize the priority queue with the initial state, which includes the index of the current coin, the sum of the coins chosen so far, and the total tax paid so far
    queue = [(0, 0, 0, [])]

    while queue:
        _, g, total_tax, chosen_coins = heapq.heappop(queue)

        # If the total sum of the chosen coins equals the target sum, return the chosen coins
        if sum(chosen_coins) == target_sum:
            return chosen_coins

        # Generate all possible actions from the current state, which includes choosing the next coin in the list
        for i in range(num_coins):
            new_sum = total_tax + tax_values[coins[i]]
            # Check if the new coin can be chosen based on the rules provided
            if (not chosen_coins or 
                (coins[i] < chosen_coins[-1] and coins[i] % 2 == 0) or
                (coins[i] >= chosen_coins[-1] and coins[i] % 2 != 0)):
                new_chosen_coins = chosen_coins + [coins[i]]
                new_state = (i, new_sum, new_chosen_coins)
                new_cost = g + tax_values[coins[i]]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_cost, new_cost, new_sum, new_chosen_coins))

    return None


print(a_star())
