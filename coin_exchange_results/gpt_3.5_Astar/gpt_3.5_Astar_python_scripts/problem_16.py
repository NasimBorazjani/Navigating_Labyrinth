
import heapq
import math


def a_star():
    # Define the list of coins and their corresponding tax values
    coins = [11, 13, 22, 11, 16, 20, 10, 10, 17, 21, 6, 6, 15, 15, 21, 6, 4, 16, 9, 11, 3, 13, 2, 9, 11, 1, 7, 2, 2, 12, 5, 2, 11, 16, 20, 9, 2, 4, 10, 17, 11, 22, 11, 2, 18, 23, 15, 22, 11, 15, 20, 9]
    tax_values = {6: 2, 11: 9, 3: 3, 15: 2, 9: 1, 18: 13, 22: 13, 16: 5, 21: 2, 5: 2, 12: 4, 7: 5, 4: 3, 13: 2, 1: 1, 20: 14, 2: 1, 10: 4, 23: 15, 17: 9}
    
    # Encoding other variables given in the problem statement
    target_sum = 223
    num_coins = len(coins)
    
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    
    # Initialize the priority queue with the initial state, which is the first coin in the list
    queue = [(0, 0, [coins[0]], (0, 0, 0))]
    
    while queue:
        _, g, coins_chosen, state = heapq.heappop(queue)
        
        # Unpack the information encoded in each state
        prev_coin, prev_tax, prev_odd = state
        
        # If the sum of the coins chosen equals the target sum, return the list of coins chosen
        if sum(coins_chosen) == target_sum:
            return coins_chosen
        
        # Generate all possible actions from the current state, which includes choosing the next coin in the list
        for i in range(1, num_coins):
            # Check if the new state would be valid, ie the sum of the coins chosen does not exceed the target sum
            if sum(coins_chosen) + coins[i] <= target_sum:
                # Check if the new coin satisfies the tax conditions
                if (coins[i] < prev_coin and coins[i] % 2 == 0) or (coins[i] >= prev_coin and coins[i] % 2 != 0):
                    # Calculate the tax for the new coin
                    new_tax = tax_values[coins[i]]
                    # Calculate the total tax paid so far
                    total_tax = prev_tax + new_tax
                    # Generate the new state
                    new_state = (coins[i], new_tax, coins[i] % 2)
                    # The additional cost of this state is the total tax paid so far
                    new_cost = g + total_tax
                    
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + total_tax, new_cost, coins_chosen + [coins[i]], new_state))
    
    return None


print(a_star())
