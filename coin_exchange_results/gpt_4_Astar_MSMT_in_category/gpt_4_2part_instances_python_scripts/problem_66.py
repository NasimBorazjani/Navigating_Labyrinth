
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 384
    coins = [3, 35, 33, 20, 31, 29, 12, 31, 8, 10, 3, 17, 2, 28, 6, 25, 10, 13, 31, 25, 37, 35, 9, 15, 113, 26, 18, 34, 30]
    taxes = {31: 11, 15: 6, 13: 13, 28: 1, 9: 6, 20: 1, 34: 15, 6: 5, 113: 20, 12: 6, 2: 1, 29: 10, 37: 2, 25: 11, 26: 10, 3: 3, 33: 19, 8: 7, 18: 6, 17: 7, 10: 8, 35: 11, 30: 16}
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
