
import heapq

def initialize():
    initial_state = ((9, 2, 23, 20, 13, 4, 15, 16, 12, 21, 13, 9, 2, 14, 13, 14, 4, 19, 12, 6, 21, 23, 4, 18, 2, 23, 23, 6, 18, 23, 3, 16, 7, 2, 22, 16, 8, 10, 23, 17, 3, 18, 8), 0, 0, 0)
    goal_sum = 230
    tax_values = {9: 1, 17: 6, 2: 2, 22: 9, 13: 13, 16: 8, 12: 4, 4: 1, 21: 14, 14: 10, 19: 9, 10: 7, 7: 6, 8: 7, 6: 2, 23: 16, 18: 3, 20: 2, 3: 1, 15: 2}
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
