
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 445
    coins = [36, 40, 17, 7, 15, 23, 18, 26, 29, 24, 15, 43, 13, 12, 31, 33, 30, 31, 26, 37, 14, 31, 43, 25, 30, 7, 37, 27, 221, 13, 26, 21]
    taxes = {36: 14, 27: 19, 21: 6, 13: 8, 23: 17, 26: 17, 15: 6, 25: 7, 31: 20, 30: 5, 18: 14, 12: 6, 37: 2, 221: 18, 14: 13, 24: 10, 33: 4, 43: 11, 29: 18, 40: 1, 7: 6, 17: 2}
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
