
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 322
    coins = [25, 22, 28, 23, 5, 14, 28, 14, 20, 6, 22, 1, 25, 18, 30, 10, 19, 12, 17, 17, 6, 28, 21, 28, 21, 2, 20, 2, 19, 14, 31, 31, 14, 7, 20, 13, 7, 18, 22, 15, 6, 6, 21, 9, 18, 11, 20, 26, 15]
    taxes = {11: 1, 14: 4, 7: 2, 25: 4, 12: 5, 20: 19, 13: 6, 15: 11, 30: 18, 1: 1, 2: 2, 31: 6, 10: 2, 23: 1, 6: 2, 21: 18, 18: 8, 28: 15, 17: 5, 26: 6, 22: 6, 9: 1, 19: 2, 5: 4}
    num_coins = len(coins)
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, goal_sum, coins, taxes, num_coins, visited_costs, queue)

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
