
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 211
    coins = [10, 5, 6, 2, 16, 19, 18, 5, 11, 12, 11, 7, 13, 19, 11, 12, 8, 17, 5, 18, 3, 12, 10, 14, 20, 18, 10, 11, 20, 13, 8, 8, 2, 7, 17, 10, 7, 21, 9, 20, 17, 1, 8, 19, 17, 16, 17, 10, 20, 8, 16, 14, 9]
    taxes = {7: 2, 3: 2, 18: 1, 13: 3, 2: 2, 19: 17, 16: 6, 10: 1, 9: 9, 12: 7, 8: 7, 6: 3, 21: 18, 11: 10, 14: 13, 1: 1, 5: 5, 20: 18, 17: 14}
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