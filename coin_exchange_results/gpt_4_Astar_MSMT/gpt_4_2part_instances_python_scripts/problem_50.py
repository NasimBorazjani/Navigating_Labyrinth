
import heapq

def initialize():
    initial_state = ((19, 14, 29, 19, 29, 9, 17, 16, 25, 7, 8, 2, 23, 11, 28, 6, 29, 16, 19, 31, 30, 15, 7, 16, 23, 23, 10, 32, 8, 14, 7, 9, 6, 23, 77, 24, 22, 24, 22), 0, 0, 0)
    goal_sum = 351
    tax_values = {15: 6, 29: 12, 19: 3, 30: 18, 14: 2, 77: 3, 6: 5, 17: 1, 32: 16, 9: 8, 22: 15, 31: 17, 25: 10, 24: 1, 28: 11, 2: 2, 7: 4, 8: 7, 11: 7, 23: 19, 10: 2, 16: 2}
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
