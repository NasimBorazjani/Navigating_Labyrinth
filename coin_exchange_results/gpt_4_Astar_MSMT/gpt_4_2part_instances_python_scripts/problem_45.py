
import heapq

def initialize():
    initial_state = ((21, 10, 19, 6, 20, 7, 23, 18, 4, 15, 4, 13, 2, 5, 32, 28, 113, 3, 9, 9, 11, 21, 112, 6, 6, 11, 29), 0, 0, 0)
    goal_sum = 337
    tax_values = {10: 7, 5: 3, 11: 3, 23: 2, 21: 13, 19: 3, 18: 18, 29: 20, 3: 2, 9: 7, 20: 18, 6: 2, 112: 20, 2: 1, 4: 4, 7: 4, 32: 1, 15: 8, 13: 10, 28: 17, 113: 18}
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
