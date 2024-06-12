
import heapq


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [9, 11, 7, 9, 12, 19, 29, 21, 11, 10, 26, 22, 18, 29, 19, 11, 18, 23, 26, 16, 18, 4, 22, 25, 17, 18, 12, 23, 3, 17, 17, 15, 22, 25, 27, 2, 26, 22, 21, 28, 10, 23, 15]
    tax_values = {28: 16, 10: 8, 21: 8, 18: 12, 27: 6, 7: 7, 2: 2, 19: 4, 17: 13, 26: 11, 12: 1, 9: 5, 25: 15, 29: 20, 11: 2, 15: 8, 22: 1, 16: 13, 4: 4, 3: 3, 23: 18}
    target_sum = 296

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen yet
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, last_coin = heapq.heappop(queue)

        # If the total value of the coins chosen so far equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is not already chosen and the total value of the coins chosen so far plus the value of the new coin does not exceed the target sum
            if coin not in coins_chosen and total_value + coin <= target_sum:
                # Check if the coin satisfies the tax conditions based on the previous coin chosen
                if (last_coin == 0 or (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 != 0)):
                    # Calculate the tax value of the new coin
                    tax = tax_values[coin]
                    # Calculate the new total tax paid
                    new_total_tax = g + tax
                    # Generate the new state
                    new_state = (g + tax, new_total_tax, coins_chosen + [coin], total_value + coin, coin)
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_total_tax < visited_costs[new_state]:
                        visited_costs[new_state] = new_total_tax
                        heapq.heappush(queue, (new_total_tax, new_total_tax, coins_chosen + [coin], total_value + coin, coin))

    return None


print(a_star())
