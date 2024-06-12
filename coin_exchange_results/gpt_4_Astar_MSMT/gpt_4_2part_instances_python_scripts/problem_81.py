
import heapq

def initialize():
    initial_state = ((13, 30, 19, 13, 34, 12, 16, 21, 24, 39, 37, 32, 3, 5, 30, 37, 29, 20, 15, 23, 30, 24, 12, 21, 19, 10, 26, 29, 3, 23, 20, 40, 22, 13, 2, 36, 8, 40, 6, 24, 24, 11, 26, 37, 16, 57, 39, 21, 17), 0, 0, 0)
    goal_sum = 412
    tax_values = {2: 2, 21: 6, 24: 9, 26: 2, 5: 3, 29: 10, 10: 7, 13: 13, 30: 17, 36: 15, 3: 1, 32: 7, 8: 5, 20: 2, 22: 3, 57: 19, 40: 8, 6: 4, 23: 8, 39: 3, 16: 5, 37: 6, 12: 9, 11: 11, 34: 6, 17: 2, 15: 10, 19: 17}
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
