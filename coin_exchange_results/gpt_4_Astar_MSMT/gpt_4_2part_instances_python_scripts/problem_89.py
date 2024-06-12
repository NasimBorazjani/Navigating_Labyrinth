
import heapq

def initialize():
    initial_state = ((27, 23, 11, 23, 6, 197, 7, 21, 2, 22, 12, 38, 15, 32, 5, 19, 6, 28, 31, 31, 10, 10, 28, 24, 41, 6, 39, 16, 11, 37, 23, 7, 2), 0, 0, 0)
    goal_sum = 445
    tax_values = {41: 14, 23: 15, 31: 19, 21: 18, 22: 2, 6: 3, 11: 5, 12: 11, 37: 10, 7: 2, 32: 19, 28: 10, 16: 12, 2: 2, 197: 7, 39: 18, 19: 18, 15: 4, 10: 9, 5: 4, 27: 10, 38: 3, 24: 5}
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
