import heapq


def a_star(coins, tax, goal_sum):
    """# Define the coins and their tax values
    coins = [11, 24, 3, 37, 32, 31, 23, 1, 29, 25, 5, 25, 3, 1, 32, 26, 9, 31, 18, 16, 33, 12, 27, 24, 9, 6, 27, 8, 15, 8, 11, 35, 3, 11, 27]
    tax = {9: 3, 27: 7, 18: 5, 26: 17, 33: 20, 6: 6, 12: 4, 35: 1, 1: 1, 37: 12, 11: 9, 16: 15, 25: 13, 23: 8, 32: 2, 31: 5, 29: 3, 8: 4, 3: 3, 24: 17, 5: 2, 15: 14}
    goal_sum = 267
    coins = [3, 6, 9, 10, 13, 15, 18, 5, 21, 19, 12, 15, 5, 9, 4, 16, 8, 4, 7, 7, 7, 2, 16, 14, 18, 3, 89, 21, 12, 10, 7, 14, 4, 11, 6, 20]
    tax ={14: 1, 89: 13, 2: 2, 5: 2, 4: 4, 6: 6, 8: 2, 16: 5, 21: 4, 20: 2, 18: 9, 11: 10, 10: 3, 12: 12, 15: 5, 13: 1, 3: 1, 19: 19, 7: 7, 9: 3}
    goal_sum = 229"""


    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[0] = 0


    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the coins chosen to get to each state in a list; no coins chosen to reach the initial state
    queue = [(0, 0, [], 0, coins)]


    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, chosen_coins, state, eligible_coins = heapq.heappop(queue)


        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_sum:
            return chosen_coins


        # Generate all valid actions from the current state, which includes choosing any of the coins based on the rules
        if chosen_coins:
            last_coin_chosen = chosen_coins[-1]
        for coin in eligible_coins:
            if not chosen_coins or (coin < last_coin_chosen and coin % 2 == 0) or (coin >= last_coin_chosen and coin % 2 == 1):
                # The new state is the sum of the current state and the value of the chosen coin
                new_state = state + coin
                # The new state is valid if the sum of the chosen coins does not exceed the goal sum
                if new_state <= goal_sum:
                    # The cost so far is the sum of the tax values of the chosen coins, as our objective is to minimize the total tax paid
                    new_cost = g + tax[coin]
                    eligible_coins_new = eligible_coins[:]
                    eligible_coins_new.remove(coin)
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, eligible_coins_new, tax, goal_sum), new_cost, chosen_coins + [coin], new_state, eligible_coins_new))
    return None

import math
def heuristic(state, eligible_coins_main, tax, goal_sum):
    """if state == goal_sum:
        return 0
    else:
        return 0"""
    eligible_coins = eligible_coins_main[:]
    sorted_eligible_coins = sorted(eligible_coins, key = lambda coin:(tax[coin]/coin, coin))
    return math.floor((goal_sum - state)* tax[sorted_eligible_coins[0]]/sorted_eligible_coins[0])
    """h = 0
    while state < goal_sum and sorted_eligible_coins:
        best_value_coin = sorted_eligible_coins.pop(0)
        if state + best_value_coin < goal_sum:
            state += best_value_coin
            h += tax[best_value_coin]"""
            
    print(h, state, goal_sum, sorted(eligible_coins, key = lambda coin:(tax[coin]/coin, coin)))
    return h

import sys
def main():
    """coins = [11, 24, 3, 37, 32, 31, 23, 1, 29, 25, 5, 25, 3, 1, 32, 26, 9, 31, 18, 16, 33, 12, 27, 24, 9, 6, 27, 8, 15, 8, 11, 35, 3, 11, 27]
    tax = {9: 3, 27: 7, 18: 5, 26: 17, 33: 20, 6: 6, 12: 4, 35: 1, 1: 1, 37: 12, 11: 9, 16: 15, 25: 13, 23: 8, 32: 2, 31: 5, 29: 3, 8: 4, 3: 3, 24: 17, 5: 2, 15: 14}
    goal_sum = 267
    coins = [3, 6, 9, 10, 13, 15, 18, 5, 21, 19, 12, 15, 5, 9, 4, 16, 8, 4, 7, 7, 7, 2, 16, 14, 18, 3, 89, 21, 12, 10, 7, 14, 4, 11, 6, 20]
    tax ={14: 1, 89: 13, 2: 2, 5: 2, 4: 4, 6: 6, 8: 2, 16: 5, 21: 4, 20: 2, 18: 9, 11: 10, 10: 3, 12: 12, 15: 5, 13: 1, 3: 1, 19: 19, 7: 7, 9: 3}
    goal_sum = 229"""
    # Read the initial state from the command line
    coins = eval(sys.argv[1])
    tax = eval(sys.argv[2])
    goal_sum = eval(sys.argv[3])
    print(a_star(coins, tax, goal_sum))

if __name__ == "__main__":
    main()