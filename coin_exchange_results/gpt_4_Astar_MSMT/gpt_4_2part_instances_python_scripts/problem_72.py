
import heapq

def initialize():
    initial_state = ((13, 3, 34, 36, 19, 31, 6, 7, 10, 24, 92, 3, 24, 33, 33, 22, 93, 13, 17, 28, 25, 16, 21, 16, 20, 26, 24, 16, 11, 18, 2, 30, 25, 23, 28, 21), 0, 0, 0)
    goal_sum = 384
    tax_values = {3: 1, 23: 1, 34: 8, 17: 14, 20: 16, 11: 5, 28: 7, 13: 3, 22: 19, 16: 4, 26: 20, 93: 7, 31: 11, 6: 2, 36: 12, 33: 15, 18: 1, 19: 2, 7: 7, 21: 7, 10: 9, 24: 11, 30: 4, 25: 7, 2: 2, 92: 19}
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
