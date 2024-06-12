
import heapq

def initialize():
    initial_state = ((43, 41, 23, 24, 40, 11, 12, 9, 32, 32, 6, 15, 16, 20, 6, 39, 9, 12, 4, 251, 43, 24, 27, 20, 39, 37, 7, 43, 9, 13, 45, 27, 9, 15, 41, 25), 0, 0, 0)
    goal_sum = 471
    tax_values = {9: 7, 32: 17, 24: 17, 15: 11, 4: 3, 39: 18, 41: 9, 25: 14, 27: 5, 40: 5, 43: 8, 11: 9, 20: 1, 45: 2, 16: 15, 251: 12, 37: 10, 13: 1, 23: 1, 7: 1, 12: 1, 6: 5}
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
