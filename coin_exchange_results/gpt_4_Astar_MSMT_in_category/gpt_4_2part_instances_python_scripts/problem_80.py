
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 397
    coins = [8, 7, 5, 24, 3, 18, 36, 39, 36, 25, 25, 33, 16, 20, 34, 9, 1, 22, 25, 13, 8, 37, 35, 39, 11, 26, 36, 25, 25, 27, 2, 4, 35, 2, 16, 22, 12, 15, 19, 2, 17, 25, 28, 12, 26, 17, 33, 5, 30, 3, 21, 3]
    taxes = {13: 7, 39: 4, 20: 18, 5: 1, 12: 7, 9: 5, 28: 20, 24: 11, 3: 3, 17: 3, 21: 9, 37: 6, 16: 8, 15: 1, 26: 10, 36: 6, 22: 9, 2: 2, 8: 1, 25: 20, 4: 3, 7: 5, 19: 7, 30: 6, 27: 12, 1: 1, 34: 7, 35: 5, 11: 6, 18: 12, 33: 4}
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
