
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [7, 2, 20, 24, 9, 24, 29, 6, 32, 26, 17, 61, 33, 14, 12, 20, 15, 34, 60, 18, 18, 37, 25, 9, 9, 21, 24, 30, 28, 3, 21, 32, 13, 10, 4, 2, 33, 36, 13, 24, 27, 7, 21, 4, 8, 17, 22, 3, 21, 12]
    tax_values = {28: 10, 36: 13, 18: 13, 17: 8, 24: 3, 37: 19, 60: 16, 13: 5, 14: 8, 30: 18, 20: 5, 27: 16, 26: 11, 2: 2, 21: 3, 7: 7, 8: 6, 3: 3, 25: 20, 22: 8, 15: 12, 12: 4, 32: 11, 9: 5, 34: 15, 4: 2, 29: 5, 33: 6, 6: 6, 10: 3, 61: 10}
    
    # Encoding other variables given in the problem statement
    target_sum = 389
    coins_set = set(coins)
    even_numbers = set([num for num in coins_set if num % 2 == 0])
    odd_numbers = coins_set - even_numbers

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], (0, 0, 0))]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        total_sum, prev_coin, prev_tax = state

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_sum == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins_set:
            # Check if the coin is valid based on the rules provided
            if (coin not in actions and
                ((coin < prev_coin and coin in even_numbers) or
                 (coin >= prev_coin and coin in odd_numbers))):
                
                # Calculate the new total sum and tax paid
                new_total_sum = total_sum + coin
                new_tax = prev_tax + tax_values[coin]
                # Generate the new state
                new_state = (new_total_sum, coin, new_tax)
                # The cost of the new state is the tax paid for the new coin
                new_cost = g + tax_values[coin]

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + new_tax, new_cost, actions + [coin], new_state))
    return None


print(a_star())
