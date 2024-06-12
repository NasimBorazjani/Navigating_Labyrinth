
import heapq

def initialize():
    initial_state = ((5, 15, 15, 77, 12, 38, 41, 30, 31, 30, 13, 19, 9, 2, 23, 37, 14, 34, 29, 22, 22, 4, 16, 2, 12, 17, 9, 18, 19, 21, 4, 28, 40, 11, 30, 24, 19, 9, 10, 76, 34), 0, 0, 0)
    goal_sum = 419
    tax_values = {13: 8, 29: 10, 4: 4, 2: 2, 77: 17, 16: 10, 11: 2, 22: 18, 17: 10, 18: 18, 38: 7, 9: 6, 5: 2, 41: 14, 31: 3, 12: 10, 19: 5, 24: 16, 40: 6, 14: 4, 34: 13, 15: 3, 23: 20, 76: 16, 37: 2, 21: 2, 28: 3, 10: 2, 30: 16}
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
