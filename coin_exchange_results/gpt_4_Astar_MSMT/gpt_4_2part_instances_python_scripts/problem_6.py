
import heapq

def initialize():
    initial_state = ((20, 25, 10, 4, 13, 3, 10, 17, 5, 25, 17, 2, 19, 24, 25, 10, 19, 8, 2, 20, 15, 84, 23, 87, 19, 8, 12, 17, 23, 6), 0, 0, 0)
    goal_sum = 250
    tax_values = {12: 12, 19: 8, 84: 20, 24: 1, 5: 1, 3: 1, 4: 2, 87: 7, 10: 5, 25: 7, 6: 5, 20: 5, 15: 7, 23: 17, 13: 4, 17: 16, 2: 1, 8: 5}
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
