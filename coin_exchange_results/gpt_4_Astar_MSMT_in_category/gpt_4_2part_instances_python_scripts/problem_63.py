
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 348
    coins = [12, 12, 5, 32, 25, 3, 23, 49, 31, 6, 12, 23, 20, 14, 34, 17, 16, 16, 21, 18, 7, 30, 7, 27, 29, 14, 5, 9, 48, 33, 5, 18, 15, 29, 2, 28, 29, 25, 26, 6, 4, 4, 6, 8, 16, 5, 4, 4, 20, 25, 10, 6, 3, 24, 19]
    taxes = {20: 18, 16: 6, 19: 2, 27: 12, 25: 2, 6: 2, 26: 16, 23: 9, 28: 12, 49: 16, 33: 13, 30: 12, 8: 6, 21: 18, 31: 16, 48: 5, 15: 5, 10: 2, 3: 1, 29: 14, 32: 15, 5: 3, 4: 4, 34: 3, 17: 14, 12: 11, 7: 3, 9: 9, 14: 7, 24: 14, 18: 15, 2: 1}
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
