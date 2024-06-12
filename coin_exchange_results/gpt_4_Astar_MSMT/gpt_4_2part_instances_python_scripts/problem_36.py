
import heapq

def initialize():
    initial_state = ((26, 7, 24, 27, 19, 15, 12, 13, 19, 5, 17, 26, 20, 7, 3, 21, 22, 7, 17, 13, 28, 11, 19, 18, 9, 10, 25, 2, 4, 18, 14, 17, 22, 27, 14, 7, 9, 2, 11, 8, 14, 10, 18, 1, 4, 24, 2, 24, 11, 14, 27), 0, 0, 0)
    goal_sum = 281
    tax_values = {13: 8, 27: 5, 21: 13, 25: 11, 22: 6, 20: 14, 12: 1, 14: 12, 2: 2, 8: 5, 3: 2, 18: 4, 1: 1, 9: 9, 10: 1, 19: 10, 11: 5, 28: 10, 5: 3, 26: 7, 7: 1, 24: 9, 4: 3, 15: 2, 17: 13}
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
