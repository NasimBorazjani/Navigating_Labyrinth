
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 397
    coins = [15, 2, 37, 38, 21, 30, 19, 28, 3, 35, 16, 32, 3, 28, 24, 27, 10, 1, 14, 3, 33, 6, 18, 37, 20, 19, 4, 31, 34, 39, 7, 13, 29, 38, 34, 14, 29, 13, 5, 33, 31, 24]
    taxes = {33: 10, 13: 12, 6: 1, 15: 2, 20: 15, 4: 3, 27: 7, 35: 5, 19: 18, 14: 13, 16: 4, 2: 2, 39: 19, 21: 18, 3: 2, 37: 14, 10: 1, 24: 3, 32: 2, 7: 4, 1: 1, 5: 4, 31: 4, 34: 7, 30: 8, 28: 11, 18: 9, 29: 2, 38: 1}
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
