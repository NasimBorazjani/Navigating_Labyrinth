
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 490
    coins = [31, 8, 22, 27, 2, 25, 2, 8, 49, 26, 65, 6, 37, 49, 15, 21, 27, 5, 34, 28, 47, 15, 7, 42, 32, 20, 34, 48, 39, 7, 13]
    taxes = {7: 1, 65: 16, 21: 18, 25: 18, 15: 14, 31: 15, 6: 2, 37: 2, 5: 1, 22: 1, 8: 7, 26: 2, 2: 1, 32: 8, 27: 2, 13: 8, 39: 17, 28: 11, 47: 6, 42: 10, 34: 15, 20: 8, 48: 11, 49: 13}
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
