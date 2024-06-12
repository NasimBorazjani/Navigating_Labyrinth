
import heapq

def initialize():
    initial_state = ((1, 2, 17, 12, 7, 17, 2, 20, 4, 4, 17, 19, 15, 16, 18, 21, 18, 10, 3, 9, 12, 13, 8, 16, 9, 14, 13, 5, 13, 6, 20, 6, 13, 12, 8, 14, 15, 7, 10, 3, 16, 16, 9, 3, 2, 6, 9, 14, 16, 20, 11, 4, 17), 0, 0, 0)
    goal_sum = 213
    tax_values = {8: 5, 5: 2, 19: 2, 4: 4, 9: 2, 3: 1, 2: 2, 12: 1, 13: 6, 6: 5, 11: 1, 17: 14, 7: 4, 16: 13, 21: 10, 14: 13, 1: 1, 18: 12, 10: 10, 15: 11, 20: 20}
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
