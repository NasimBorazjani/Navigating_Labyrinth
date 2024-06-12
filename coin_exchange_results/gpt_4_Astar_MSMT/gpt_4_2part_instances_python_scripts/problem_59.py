
import heapq

def initialize():
    initial_state = ((23, 27, 20, 21, 8, 2, 2, 3, 21, 26, 16, 33, 22, 3, 25, 17, 5, 31, 3, 9, 12, 30, 11, 10, 7, 13, 2, 21, 8, 16, 5, 18, 32, 27, 7, 32, 7, 10, 11, 33, 18, 30, 7, 24, 21, 4, 25, 4, 23, 21, 23, 15, 26, 10), 0, 0, 0)
    goal_sum = 334
    tax_values = {16: 1, 18: 1, 9: 1, 11: 5, 5: 3, 2: 1, 21: 1, 33: 3, 7: 1, 4: 1, 30: 8, 23: 10, 17: 8, 15: 7, 13: 6, 20: 8, 32: 4, 10: 6, 3: 1, 12: 7, 27: 6, 31: 5, 22: 1, 26: 20, 24: 5, 8: 4, 25: 9}
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
