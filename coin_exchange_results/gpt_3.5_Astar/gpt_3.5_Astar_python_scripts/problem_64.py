
import heapq

def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [14, 8, 11, 30, 3, 3, 27, 16, 19, 4, 6, 14, 7, 2, 39, 103, 15, 100, 27, 36, 7, 36, 13, 7, 18, 39, 14, 3, 28]
    tax_values = {13: 11, 18: 8, 36: 15, 11: 4, 6: 1, 16: 8, 100: 12, 39: 10, 28: 9, 27: 20, 103: 6, 19: 5, 30: 14, 2: 1, 4: 3, 3: 3, 15: 10, 8: 5, 7: 2, 14: 14}
    target_sum = 410

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen so far in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, 0)]

    while queue:
        _, g, coins_chosen, total_value, last_coin = heapq.heappop(queue)

        # If the total value of the coins chosen so far equals the target sum, return the list of coins chosen
        if total_value == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing the next coin from the list
        for coin in coins:
            # Check if the coin is valid to be chosen based on the given conditions
            if (coin not in coins_chosen and
                ((coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 != 0))):
                # Calculate the new total value and tax paid
                new_total_value = total_value + coin
                new_tax_paid = g + tax_values[coin]
                # If the new total value does not exceed the target sum, add the new state to the queue
                if new_total_value <= target_sum:
                    new_coins_chosen = coins_chosen + [coin]
                    new_state = (new_tax_paid, new_total_value, new_coins_chosen, coin)
                    if new_state not in visited_costs or new_tax_paid < visited_costs[new_state]:
                        visited_costs[new_state] = new_tax_paid
                        heapq.heappush(queue, (g + new_tax_paid, new_tax_paid, new_coins_chosen, new_total_value, coin))

    return None

print(a_star())
