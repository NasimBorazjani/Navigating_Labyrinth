
import heapq

def initialize():
    initial_state = ((10, 5, 6, 2, 16, 19, 18, 5, 11, 12, 11, 7, 13, 19, 11, 12, 8, 17, 5, 18, 3, 12, 10, 14, 20, 18, 10, 11, 20, 13, 8, 8, 2, 7, 17, 10, 7, 21, 9, 20, 17, 1, 8, 19, 17, 16, 17, 10, 20, 8, 16, 14, 9), 0, 0, 0)
    goal_sum = 211
    tax_values = {7: 2, 3: 2, 18: 1, 13: 3, 2: 2, 19: 17, 16: 6, 10: 1, 9: 9, 12: 7, 8: 7, 6: 3, 21: 18, 11: 10, 14: 13, 1: 1, 5: 5, 20: 18, 17: 14}
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
