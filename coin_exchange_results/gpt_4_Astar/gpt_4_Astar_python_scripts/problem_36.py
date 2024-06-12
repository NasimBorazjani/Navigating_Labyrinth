
import heapq

def a_star():
    # Define the initial state of the problem
    coins = [26, 7, 24, 27, 19, 15, 12, 13, 19, 5, 17, 26, 20, 7, 3, 21, 22, 7, 17, 13, 28, 11, 19, 18, 9, 10, 25, 2, 4, 18, 14, 17, 22, 27, 14, 7, 9, 2, 11, 8, 14, 10, 18, 1, 4, 24, 2, 24, 11, 14, 27]
    taxes = {13: 8, 27: 5, 21: 13, 25: 11, 22: 6, 20: 14, 12: 1, 14: 12, 2: 2, 8: 5, 3: 2, 18: 4, 1: 1, 9: 9, 10: 1, 19: 10, 11: 5, 28: 10, 5: 3, 26: 7, 7: 1, 24: 9, 4: 3, 15: 2, 17: 13}
    target_sum = 281
    initial_state = (0, 0, 0, [])  # (sum_so_far, last_coin, total_tax, coins_chosen)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, initial_state)]

    while queue:
        _, state = heapq.heappop(queue)
        sum_so_far, last_coin, total_tax, coins_chosen = state

        # If the current state is the goal state, return the coins chosen
        if sum_so_far == target_sum:
            return coins_chosen

        # Generate all possible actions from the current state, which includes choosing any of the remaining coins
        for coin in coins:
            if coin not in coins_chosen:
                new_sum = sum_so_far + coin
                new_tax = total_tax + taxes[coin]

                # Check if the new state would be valid, i.e., the sum of the coins does not exceed the target sum,
                # and the coin is smaller than the last one and has an even value, or is larger than or equal to the last one and has an odd value
                if new_sum <= target_sum and ((coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1)):
                    new_state = (new_sum, coin, new_tax, coins_chosen + [coin])

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_tax < visited_costs[new_state]:
                        visited_costs[new_state] = new_tax
                        heapq.heappush(queue, (new_tax, new_state))

    return None

print(a_star())
