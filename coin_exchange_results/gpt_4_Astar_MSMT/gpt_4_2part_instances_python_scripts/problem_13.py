
import heapq

def initialize():
    initial_state = ((20, 19, 2, 12, 23, 18, 15, 13, 10, 6, 9, 4, 9, 16, 5, 8, 19, 6, 7, 2, 6, 15, 10, 9, 4, 6, 19, 10, 10, 16, 21, 17, 21, 16, 13, 6, 16, 8, 7, 11, 13, 7, 21, 15, 15, 6, 11, 19, 7), 0, 0, 0)
    goal_sum = 216
    tax_values = {6: 6, 8: 6, 16: 4, 15: 11, 12: 3, 10: 5, 20: 14, 9: 3, 17: 8, 7: 5, 5: 5, 2: 1, 11: 4, 23: 18, 19: 3, 13: 13, 18: 6, 4: 3, 21: 20}
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
