
import heapq

def initialize():
    initial_state = ((28, 2, 4, 7, 11, 26, 14, 8, 23, 29, 18, 13, 26, 21, 10, 26, 8, 33, 9, 15, 4, 21, 19, 3, 7, 10, 4, 7, 16, 16, 11, 33, 12, 23, 5, 3, 26, 7, 17, 30, 22, 22, 6, 16, 18, 25, 26, 11, 13, 23, 17, 11, 20, 12), 0, 0, 0)
    goal_sum = 339
    tax_values = {10: 6, 18: 17, 33: 15, 16: 16, 3: 2, 30: 18, 13: 3, 21: 17, 23: 4, 12: 1, 7: 6, 17: 7, 4: 2, 6: 5, 2: 2, 11: 5, 14: 14, 29: 1, 20: 7, 8: 3, 15: 7, 28: 3, 26: 8, 19: 11, 9: 9, 22: 4, 5: 5, 25: 5}
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
