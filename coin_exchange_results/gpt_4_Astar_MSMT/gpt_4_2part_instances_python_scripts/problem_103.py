
import heapq

def initialize():
    initial_state = ((40, 28, 46, 16, 13, 15, 38, 39, 3, 8, 40, 41, 18, 48, 16, 25, 39, 14, 47, 46, 31, 16, 41, 45, 9, 26, 33, 46, 17, 23, 6, 46, 7, 43, 10, 28, 47, 15, 35, 20, 32, 4, 32, 9, 48, 7, 34, 46, 10, 39, 44), 0, 0, 0)
    goal_sum = 485
    tax_values = {44: 6, 39: 15, 4: 2, 23: 11, 7: 2, 40: 10, 13: 10, 34: 8, 45: 9, 10: 3, 35: 18, 14: 2, 28: 5, 46: 12, 25: 3, 26: 18, 15: 11, 31: 2, 20: 15, 9: 7, 41: 13, 18: 16, 32: 11, 3: 3, 48: 20, 38: 4, 43: 6, 33: 9, 16: 13, 8: 4, 17: 1, 47: 17, 6: 5}
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
