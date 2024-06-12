
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 474
    coins = [21, 13, 10, 18, 21, 43, 42, 29, 14, 19, 9, 2, 15, 19, 32, 45, 24, 31, 25, 7, 21, 24, 29, 29, 4, 36, 29, 19, 29, 12, 3, 44, 40, 46, 33, 3, 28, 44, 25, 6, 36, 3, 4, 19, 31]
    taxes = {6: 3, 9: 7, 13: 11, 19: 11, 36: 17, 32: 11, 46: 1, 4: 3, 21: 14, 3: 1, 18: 5, 29: 18, 12: 9, 2: 2, 15: 14, 43: 11, 24: 5, 25: 15, 14: 10, 42: 11, 44: 7, 31: 11, 40: 2, 33: 10, 45: 20, 7: 6, 10: 3, 28: 5}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, goal_state, coins, taxes, visited_costs, queue)

def a_star():
    (initial_state, goal_sum, coins, taxes, num_coins, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (state[1] == goal_sum):
            return actions
        for i in range(state[0], num_coins):
            if ((state[1] + coins[i]) <= goal_sum):
                if (((coins[i] < state[2]) and ((coins[i] % 2) == 0)) or ((coins[i] >= state[2]) and ((coins[i] % 2) == 1))):
                    new_state = ((i + 1), (state[1] + coins[i]), coins[i], (state[3] + taxes[coins[i]]))
                    new_cost = (g + taxes[coins[i]])
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_sum, coins, taxes)
                        heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [coins[i]]), new_state))
    return None

def heuristic(state, goal_sum, coins, taxes):
    h = 0
    remaining_coins = sorted(coins[state[0]:], key=(lambda x: taxes[x]))
    for coin in remaining_coins:
        if ((state[1] + coin) <= goal_sum):
            h += taxes[coin]
    return h
print(a_star())
