
import heapq

def initialize():
    initial_state = ((28, 5, 25, 22, 26, 13, 20, 20, 18, 28, 7, 20, 18, 19, 18, 5, 15, 23, 28, 27, 22, 10, 8, 17, 3, 8, 5, 11, 21, 17, 65, 23, 11, 3, 12), 0, 0, 0)
    goal_sum = 284
    tax_values = {20: 12, 21: 3, 5: 2, 3: 2, 7: 1, 15: 8, 8: 7, 27: 6, 17: 8, 18: 14, 28: 5, 13: 1, 23: 4, 65: 8, 26: 8, 22: 5, 25: 3, 11: 11, 12: 8, 19: 19, 10: 7}
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
