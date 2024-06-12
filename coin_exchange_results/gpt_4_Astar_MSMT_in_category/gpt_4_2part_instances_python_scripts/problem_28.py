
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 267
    coins = [26, 19, 7, 24, 27, 15, 9, 9, 9, 26, 15, 23, 6, 6, 24, 8, 21, 6, 6, 7, 25, 22, 8, 2, 7, 5, 8, 18, 14, 15, 24, 10, 4, 23, 21, 8, 18, 12, 16]
    taxes = {24: 14, 27: 10, 22: 14, 16: 7, 14: 12, 6: 3, 8: 7, 23: 6, 18: 18, 5: 3, 25: 8, 7: 6, 12: 3, 15: 8, 9: 2, 19: 15, 2: 1, 4: 1, 26: 15, 10: 8, 21: 19}
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
