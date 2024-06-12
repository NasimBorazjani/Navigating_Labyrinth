
import heapq

def initialize():
    initial_state = ((14, 29, 39, 40, 16, 35, 17, 37, 43, 30, 28, 26, 13, 13, 42, 30, 10, 7, 44, 5, 34, 7, 32, 11, 40, 35, 12, 34, 35, 38, 29, 42, 33, 26, 4, 36, 41, 35, 26, 34, 16, 6, 38, 13, 41, 23, 20), 0, 0, 0)
    goal_sum = 449
    tax_values = {11: 4, 10: 3, 41: 9, 34: 4, 7: 2, 17: 16, 29: 8, 37: 1, 44: 8, 30: 13, 32: 9, 20: 18, 23: 8, 6: 4, 5: 3, 14: 3, 13: 7, 35: 4, 33: 5, 39: 9, 40: 11, 28: 3, 4: 2, 43: 14, 42: 15, 38: 14, 16: 5, 36: 5, 12: 9, 26: 1}
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
