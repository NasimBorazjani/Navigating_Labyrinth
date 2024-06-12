
import heapq

def initialize():
    initial_state = ((10, 16, 2, 18, 10, 16, 17, 32, 18, 33, 23, 20, 21, 25, 32, 24, 10, 27, 13, 27, 30, 13, 19, 20, 4, 5, 15, 8, 8, 34, 21, 14, 3, 20, 10, 18, 3, 14, 28, 6, 4, 8, 15, 4, 30, 30, 12, 20, 14, 10), 0, 0, 0)
    goal_sum = 357
    tax_values = {30: 12, 20: 19, 16: 7, 24: 14, 12: 3, 13: 4, 8: 2, 2: 1, 21: 2, 23: 12, 34: 13, 27: 16, 3: 3, 28: 3, 14: 13, 6: 4, 33: 17, 10: 8, 5: 3, 15: 12, 4: 2, 18: 2, 19: 5, 17: 1, 32: 2, 25: 12}
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
