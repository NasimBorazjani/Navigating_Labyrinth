
import heapq

def initialize():
    initial_state = ((29, 25, 15, 12, 40, 23, 36, 22, 16, 24, 51, 34, 46, 29, 20, 14, 21, 27, 15, 31, 15, 17, 9, 42, 30, 45, 14, 14, 30, 16, 44, 32, 6, 15, 5, 41, 18, 43, 36, 31, 27, 26, 6, 44, 33, 23, 7, 19), 0, 0, 0)
    goal_sum = 477
    tax_values = {41: 15, 22: 3, 9: 4, 34: 9, 32: 11, 36: 5, 18: 5, 40: 9, 46: 11, 45: 17, 33: 3, 14: 9, 12: 12, 7: 2, 43: 14, 25: 18, 31: 9, 51: 8, 24: 18, 17: 3, 16: 5, 19: 10, 6: 6, 27: 15, 42: 7, 23: 2, 29: 2, 21: 13, 30: 7, 44: 4, 5: 2, 20: 11, 26: 12, 15: 8}
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
