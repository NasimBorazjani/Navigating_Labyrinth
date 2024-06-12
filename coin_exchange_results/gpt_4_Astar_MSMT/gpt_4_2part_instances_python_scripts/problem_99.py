
import heapq

def initialize():
    initial_state = ((37, 4, 1, 15, 2, 7, 8, 33, 35, 14, 47, 36, 41, 44, 13, 31, 3, 7, 27, 25, 26, 38, 10, 19, 7, 18, 32, 45, 29, 35, 44, 17, 40, 13, 14, 40, 28, 15, 23, 11, 7, 16, 7, 35, 31, 45, 14, 22, 7, 36, 31), 0, 0, 0)
    goal_sum = 465
    tax_values = {44: 2, 1: 1, 36: 14, 26: 2, 22: 10, 33: 13, 16: 12, 23: 1, 41: 6, 8: 6, 18: 3, 13: 5, 2: 2, 7: 5, 29: 13, 25: 19, 3: 1, 45: 12, 35: 13, 17: 6, 47: 13, 10: 8, 15: 14, 31: 13, 4: 2, 14: 2, 32: 11, 40: 3, 11: 4, 28: 7, 37: 12, 27: 11, 19: 17, 38: 18}
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
