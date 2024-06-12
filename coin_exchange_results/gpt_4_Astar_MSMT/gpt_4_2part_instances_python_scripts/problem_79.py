
import heapq

def initialize():
    initial_state = ((33, 4, 5, 9, 31, 26, 25, 19, 31, 33, 24, 6, 13, 17, 15, 37, 7, 21, 3, 23, 22, 7, 3, 11, 19, 28, 24, 32, 27, 31, 24, 12, 23, 22, 16, 6, 33, 8, 19, 13, 5, 11, 10, 4, 8, 16, 14, 17, 13, 9, 25, 17), 0, 0, 0)
    goal_sum = 389
    tax_values = {3: 3, 19: 1, 5: 2, 9: 4, 17: 4, 24: 11, 8: 5, 22: 10, 4: 2, 32: 10, 16: 1, 37: 5, 23: 12, 26: 18, 12: 1, 27: 9, 14: 5, 25: 13, 15: 8, 6: 6, 21: 13, 10: 3, 31: 17, 7: 3, 33: 10, 11: 2, 28: 10, 13: 10}
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
