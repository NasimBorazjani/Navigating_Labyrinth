
import heapq


def a_star():
    # Define the list of coins and their tax values
    coins = [9, 18, 7, 20, 4, 12, 5, 5, 18, 5, 2, 11, 5, 16, 19, 8, 10, 9, 12, 14, 17, 6, 14, 16, 20, 10, 10, 13, 4, 13, 7, 14, 14, 10, 2, 7, 14, 11, 16, 10, 10, 5, 14, 20, 4, 17]
    tax_values = {17: 16, 8: 8, 6: 6, 16: 12, 5: 4, 14: 12, 18: 9, 12: 1, 19: 12, 4: 2, 7: 3, 10: 7, 11: 7, 13: 6, 2: 1, 9: 1, 20: 10}
    target_sum = 206

    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0

    # Initialize the priority queue with the initial state, which includes the current sum, the previous coin value, and the total tax paid so far
    queue = [(0, 0, 0, [])]

    while queue:
        _, current_sum, prev_coin, total_tax, coins_chosen = heapq.heappop(queue)

        # If the current sum equals the target sum, return the list of coins chosen
        if current_sum == target_sum:
            return coins_chosen

        for coin in coins:
            # Check if the coin is valid based on the tax rules
            if (coin > prev_coin and coin % 2 == 1) or (coin < prev_coin and coin % 2 == 0):
                new_sum = current_sum + coin
                new_tax = total_tax + tax_values[coin]
                # If the new sum is less than or equal to the target sum, add the new state to the queue
                if new_sum <= target_sum:
                    new_state = (new_sum, coin, new_tax, coins_chosen + [coin])
                    if new_state not in visited_costs or new_tax < visited_costs[new_state]:
                        visited_costs[new_state] = new_tax
                        heapq.heappush(queue, (new_tax, new_sum, coin, new_tax, coins_chosen + [coin]))

    return None


print(a_star())
