
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 260
    coins = [12, 23, 57, 18, 6, 5, 21, 15, 14, 23, 5, 16, 9, 8, 19, 8, 19, 6, 8, 3, 12, 2, 14, 3, 3, 4, 26, 6, 6, 25, 9, 13, 20, 24, 6, 26, 14, 25, 5, 26]
    taxes = {6: 2, 12: 3, 9: 2, 2: 1, 14: 1, 16: 12, 21: 10, 4: 1, 8: 5, 26: 7, 23: 7, 57: 11, 15: 15, 19: 13, 25: 15, 13: 4, 5: 3, 24: 4, 3: 3, 18: 4, 20: 10}
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
