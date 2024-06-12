
import heapq

def initialize():
    initial_state = ((8, 13, 16, 4, 35, 2, 19, 2, 21, 26, 28, 12, 58, 28, 12, 35, 33, 4, 19, 27, 61, 30, 17, 20, 27, 25, 30, 31, 9, 15, 4, 13, 11, 29), 0, 0, 0)
    goal_sum = 384
    tax_values = {13: 1, 4: 1, 61: 2, 30: 19, 12: 4, 20: 16, 29: 10, 2: 2, 35: 17, 31: 17, 19: 15, 25: 11, 21: 8, 27: 16, 17: 17, 11: 7, 58: 12, 26: 4, 15: 14, 28: 10, 8: 5, 16: 5, 9: 8, 33: 13}
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
