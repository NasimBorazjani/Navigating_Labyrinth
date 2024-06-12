
import heapq

def initialize():
    initial_state = ((31, 83, 19, 4, 13, 27, 13, 18, 21, 24, 9, 3, 2, 30, 16, 14, 31, 29, 27, 23, 18, 8, 32, 3, 3, 25, 17, 8, 32, 5, 2, 28, 30, 26, 25, 12, 12), 0, 0, 0)
    goal_sum = 335
    tax_values = {32: 1, 19: 12, 3: 1, 27: 14, 5: 3, 9: 5, 13: 11, 14: 10, 28: 6, 31: 15, 8: 8, 18: 18, 17: 7, 2: 2, 12: 9, 24: 16, 83: 6, 23: 9, 16: 15, 29: 4, 25: 5, 26: 18, 4: 1, 21: 10, 30: 10}
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
