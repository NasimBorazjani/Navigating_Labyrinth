
import heapq

def initialize():
    initial_state = ((27, 17, 6, 5, 20, 3, 4, 29, 25, 27, 20, 18, 18, 25, 2, 13, 15, 4, 12, 4, 26, 12, 26, 24, 17, 23, 2, 6, 2, 29, 3, 20, 12, 7, 9, 12, 26, 11, 2, 5, 10, 25, 3, 13, 7, 25), 0, 0, 0)
    goal_sum = 295
    tax_values = {2: 1, 13: 11, 26: 13, 5: 1, 4: 2, 9: 8, 15: 8, 18: 6, 20: 18, 3: 1, 17: 17, 6: 2, 10: 10, 12: 1, 23: 10, 7: 6, 29: 13, 25: 15, 11: 10, 27: 2, 24: 18}
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
