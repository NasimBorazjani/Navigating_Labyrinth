
import heapq

def initialize():
    initial_state = ((19, 11, 35, 3, 12, 23, 42, 45, 8, 12, 32, 82, 39, 12, 45, 12, 40, 38, 28, 6, 32, 37, 39, 9, 43, 12, 38, 4, 42, 44, 41, 37, 83, 5, 38), 0, 0, 0)
    goal_sum = 466
    tax_values = {37: 6, 43: 18, 32: 16, 4: 4, 83: 4, 8: 5, 23: 18, 12: 6, 82: 16, 44: 20, 39: 1, 19: 8, 35: 7, 38: 11, 11: 3, 42: 5, 45: 12, 3: 1, 6: 2, 41: 3, 28: 18, 40: 2, 9: 6, 5: 4}
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
