
import heapq

def initialize():
    initial_state = ((39, 3, 38, 10, 3, 5, 6, 14, 32, 7, 30, 28, 17, 9, 8, 13, 17, 41, 25, 6, 19, 36, 5, 36, 8, 38, 6, 19, 25, 3, 22, 18, 3, 21, 57, 37, 42, 30, 54, 13, 36, 6, 13, 17, 10, 4, 36), 0, 0, 0)
    goal_sum = 452
    tax_values = {37: 2, 38: 4, 30: 18, 39: 18, 14: 1, 18: 1, 4: 1, 10: 8, 21: 10, 6: 5, 42: 13, 32: 10, 25: 2, 17: 15, 13: 2, 9: 4, 22: 17, 7: 5, 3: 2, 54: 7, 19: 15, 8: 2, 36: 17, 28: 6, 5: 5, 41: 9, 57: 12}
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
