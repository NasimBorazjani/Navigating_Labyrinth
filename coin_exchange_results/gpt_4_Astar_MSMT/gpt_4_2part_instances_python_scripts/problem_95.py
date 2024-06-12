
import heapq

def initialize():
    initial_state = ((26, 8, 19, 9, 36, 23, 42, 40, 13, 34, 40, 25, 11, 38, 10, 41, 19, 34, 91, 18, 14, 27, 14, 43, 42, 13, 2, 27, 90, 13, 3, 4, 44, 7, 48, 40, 35, 40, 10, 12, 25), 0, 0, 0)
    goal_sum = 488
    tax_values = {44: 20, 11: 4, 19: 3, 4: 4, 10: 3, 14: 9, 90: 18, 48: 12, 91: 5, 8: 4, 7: 5, 9: 5, 12: 2, 42: 18, 36: 6, 35: 10, 34: 12, 25: 7, 27: 1, 3: 2, 26: 15, 40: 8, 43: 1, 18: 8, 23: 1, 13: 3, 41: 8, 38: 13, 2: 2}
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
