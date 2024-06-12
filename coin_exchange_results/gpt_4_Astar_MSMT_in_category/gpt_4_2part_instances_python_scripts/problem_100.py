
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 449
    coins = [19, 11, 3, 37, 9, 29, 42, 12, 2, 13, 15, 11, 25, 14, 31, 17, 24, 45, 5, 18, 42, 21, 28, 23, 26, 40, 27, 42, 12, 13, 16, 14, 31, 38, 9, 24, 27, 36, 13, 27, 15, 43, 9, 14, 34, 7, 15, 12, 31, 44]
    taxes = {37: 7, 45: 7, 29: 6, 27: 2, 2: 2, 40: 6, 13: 9, 17: 2, 9: 2, 15: 12, 36: 2, 26: 18, 44: 5, 42: 4, 38: 8, 43: 2, 12: 4, 24: 20, 28: 15, 16: 7, 21: 13, 23: 5, 19: 4, 25: 16, 3: 2, 18: 13, 34: 16, 31: 2, 5: 4, 14: 2, 7: 1, 11: 8}
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
