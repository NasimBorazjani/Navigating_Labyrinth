
import heapq

def initialize():
    initial_state = ((26, 8, 34, 12, 20, 21, 35, 13, 28, 5, 16, 11, 24, 42, 16, 12, 34, 21, 27, 27, 20, 47, 9, 12, 38, 23, 43, 33, 26, 22, 38, 42, 20, 41, 47, 41, 24, 46, 35, 42, 9, 35, 13, 45, 24, 29, 45, 2, 41, 39, 24, 38, 39, 18, 5, 8, 36), 0, 0, 0)
    goal_sum = 477
    tax_values = {12: 8, 18: 6, 42: 8, 11: 9, 38: 13, 9: 9, 24: 15, 34: 1, 20: 5, 2: 2, 23: 2, 33: 12, 27: 8, 39: 11, 16: 1, 28: 12, 26: 11, 21: 7, 35: 7, 22: 19, 47: 9, 29: 12, 46: 3, 45: 9, 5: 1, 13: 13, 43: 8, 36: 11, 41: 4, 8: 8}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, goal_sum, tax_values, visited_costs, queue)

def a_star():
    (initial_state, goal_sum, tax_values, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        (coins, sum_coins, tax_paid, last_coin) = state
        if (sum_coins == goal_sum):
            return actions
        elif (sum_coins < goal_sum):
            for coin in coins:
                if (((coin < last_coin) and ((coin % 2) == 0)) or ((coin >= last_coin) and ((coin % 2) == 1))):
                    new_state = (tuple((c for c in coins if (c != coin))), (sum_coins + coin), (tax_paid + tax_values[coin]), coin)
                    new_cost = (g + tax_values[coin])
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + heuristic(new_state, goal_sum)), new_cost, (actions + [coin]), new_state))
    return None

def heuristic(state, goal_sum):
    return (goal_sum - state[1])
print(a_star())
