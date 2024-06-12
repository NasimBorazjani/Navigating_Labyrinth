
import heapq

def a_star():
    # Define the list of coins and their tax values
    coins = [23, 10, 22, 30, 5, 16, 2, 28, 25, 26, 30, 25, 35, 32, 10, 4, 24, 32, 34, 12, 11, 5, 5, 18, 16, 24, 3, 12, 11, 5, 2, 7, 19, 34, 7, 30, 17, 11, 16, 10, 31, 31, 34, 27, 3, 24]
    tax_values = {24: 9, 26: 11, 17: 7, 7: 4, 12: 4, 35: 18, 5: 5, 31: 8, 2: 2, 3: 1, 27: 14, 34: 3, 30: 1, 23: 6, 4: 2, 10: 8, 18: 18, 25: 15, 28: 4, 32: 19, 11: 7, 16: 6, 19: 11, 22: 5}
    
    # Encoding other variables given in the problem statement
    target_sum = 359
    coins_set = set(coins)
    even_numbers = set([num for num in coins_set if num % 2 == 0])
    odd_numbers = coins_set - even_numbers

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, actions, total_tax, prev_coin = heapq.heappop(queue)

        # If the total tax paid is equal to the target sum, return the list of coins chosen
        if total_tax == target_sum:
            return actions

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins_set:
            # Check if the coin is valid based on the given constraints
            if (coin not in actions and
                ((coin < prev_coin and coin in even_numbers) or
                 (coin >= prev_coin and coin in odd_numbers))):
                
                # Calculate the new total tax paid and the new cost of the state
                new_total_tax = total_tax + tax_values[coin]
                new_cost = g + tax_values[coin]

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_total_tax <= target_sum and (new_cost, new_total_tax) not in visited_costs:
                    visited_costs[(new_cost, new_total_tax)] = new_cost
                    heapq.heappush(queue, (g + new_total_tax, new_cost, actions + [coin], new_total_tax, coin))

    return None

print(a_star())
