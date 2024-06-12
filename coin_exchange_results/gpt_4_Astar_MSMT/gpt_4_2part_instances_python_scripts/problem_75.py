
import heapq

def initialize():
    initial_state = ((8, 31, 28, 24, 19, 18, 26, 31, 43, 32, 3, 21, 21, 10, 36, 40, 19, 38, 3, 5, 24, 12, 11, 14, 40, 7, 19, 4, 22, 5, 33, 31, 40, 7, 5, 34, 33, 22, 14, 6, 14, 29), 0, 0, 0)
    goal_sum = 408
    tax_values = {31: 12, 40: 17, 32: 19, 26: 14, 12: 1, 5: 3, 36: 1, 33: 5, 3: 2, 6: 1, 34: 19, 18: 18, 8: 7, 21: 11, 43: 20, 22: 20, 4: 4, 11: 6, 28: 20, 7: 3, 38: 13, 24: 12, 19: 16, 10: 7, 14: 9, 29: 3}
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
