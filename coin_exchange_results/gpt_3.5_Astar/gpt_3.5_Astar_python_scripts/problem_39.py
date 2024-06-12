
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [26, 24, 8, 2, 11, 10, 11, 14, 20, 9, 13, 10, 25, 21, 7, 20, 15, 27, 18, 12, 23, 4, 2, 4, 22, 23, 15, 16, 24, 14, 22, 13, 15, 21, 5, 14, 2, 21, 14, 10, 2, 2, 24, 26, 17, 2, 20, 22, 3, 27, 8, 20, 2, 25, 7]
    tax_values = {24: 18, 14: 4, 15: 10, 23: 15, 26: 12, 22: 4, 17: 8, 5: 2, 18: 2, 16: 3, 11: 3, 2: 1, 27: 9, 3: 3, 10: 5, 20: 4, 4: 2, 21: 4, 12: 1, 8: 6, 13: 2, 7: 2, 9: 6, 25: 15}
    
    # Encoding other variables given in the problem statement
    target_sum = 273
    coins_set = set(coins)
    even_numbers = set([num for num in coins_set if num % 2 == 0])
    odd_numbers = coins_set - even_numbers

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, last_coin, total_tax = heapq.heappop(queue)

        # If the total sum of coins chosen equals the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins_set:
            # Check if the coin is valid based on the rules provided
            if (coin not in coins_chosen and
                ((coin < last_coin and coin in even_numbers) or (coin >= last_coin and coin in odd_numbers))):
                # Calculate the new total tax with the addition of the tax value of the chosen coin
                new_total_tax = total_tax + tax_values[coin]
                # Generate the new state
                new_state = (g + new_total_tax, new_total_tax, coins_chosen + [coin], coin, new_total_tax)
                # The cost of the new state is the total tax paid so far
                new_cost = g + new_total_tax

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic is the difference between the target sum and the current total tax paid
                    h = target_sum - new_total_tax
                    heapq.heappush(queue, (g + h, g + new_total_tax, coins_chosen + [coin], coin, new_total_tax))
    return None


print(a_star())
