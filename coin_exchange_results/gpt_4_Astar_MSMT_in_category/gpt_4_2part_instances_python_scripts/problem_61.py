
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 351
    coins = [30, 4, 10, 25, 2, 20, 23, 22, 29, 13, 21, 23, 23, 24, 3, 26, 29, 27, 15, 18, 28, 10, 22, 24, 2, 22, 13, 32, 8, 28, 31, 13, 27, 6, 35, 2, 20, 25, 24, 2, 16, 31, 3, 5, 23, 32, 24, 20, 13, 7, 11, 12]
    taxes = {10: 8, 32: 8, 25: 5, 7: 2, 30: 9, 18: 3, 5: 2, 35: 14, 2: 1, 15: 10, 12: 6, 29: 14, 23: 12, 31: 14, 11: 3, 8: 7, 21: 5, 13: 3, 28: 3, 6: 1, 3: 2, 4: 2, 22: 5, 16: 9, 24: 4, 27: 16, 26: 6, 20: 20}
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
