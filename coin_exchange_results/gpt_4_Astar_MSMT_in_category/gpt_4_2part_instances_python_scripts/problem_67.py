
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 384
    coins = [8, 13, 16, 4, 35, 2, 19, 2, 21, 26, 28, 12, 58, 28, 12, 35, 33, 4, 19, 27, 61, 30, 17, 20, 27, 25, 30, 31, 9, 15, 4, 13, 11, 29]
    taxes = {13: 1, 4: 1, 61: 2, 30: 19, 12: 4, 20: 16, 29: 10, 2: 2, 35: 17, 31: 17, 19: 15, 25: 11, 21: 8, 27: 16, 17: 17, 11: 7, 58: 12, 26: 4, 15: 14, 28: 10, 8: 5, 16: 5, 9: 8, 33: 13}
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
