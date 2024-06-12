
import heapq

def initialize():
    initial_state = ((17, 4, 35, 10, 42, 11, 10, 11, 2, 14, 29, 31, 33, 3, 38, 4, 32, 9, 19, 14, 4, 39, 6, 36, 31, 25, 40, 8, 33, 31, 11, 34, 18, 2, 32, 40, 4, 16, 1, 36, 37, 3, 33, 20, 10, 8, 9, 20, 14, 35, 36, 22, 35, 4), 0, 0, 0)
    goal_sum = 426
    tax_values = {37: 11, 10: 3, 36: 8, 32: 3, 3: 1, 18: 16, 14: 5, 35: 5, 16: 15, 8: 5, 42: 20, 29: 4, 6: 1, 25: 9, 11: 4, 20: 15, 39: 6, 38: 14, 34: 6, 40: 11, 9: 2, 17: 6, 19: 8, 4: 4, 22: 20, 31: 3, 1: 1, 33: 18, 2: 2}
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
