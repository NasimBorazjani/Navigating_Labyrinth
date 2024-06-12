
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 392
    coins = [29, 32, 2, 34, 7, 25, 7, 14, 33, 1, 26, 18, 13, 11, 32, 31, 13, 2, 28, 21, 38, 8, 11, 28, 26, 9, 4, 28, 34, 23, 18, 31, 35, 2, 25, 20, 15, 5, 12, 10, 7, 14, 17, 4, 13, 24, 11, 16, 14, 27, 29]
    taxes = {10: 1, 25: 18, 1: 1, 15: 7, 12: 1, 23: 16, 9: 7, 27: 15, 29: 16, 28: 2, 32: 12, 24: 6, 5: 1, 8: 1, 11: 8, 17: 13, 13: 6, 38: 6, 31: 19, 4: 2, 34: 12, 21: 3, 2: 2, 33: 12, 20: 13, 18: 1, 14: 13, 16: 8, 7: 5, 35: 16, 26: 10}
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
