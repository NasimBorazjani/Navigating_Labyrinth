
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 236
    coins = [6, 20, 15, 14, 23, 6, 8, 15, 11, 2, 16, 21, 17, 10, 23, 20, 21, 16, 13, 3, 7, 4, 9, 21, 7, 13, 10, 18, 11, 9, 13, 12, 15, 17, 2, 8, 18, 3, 16, 9, 3, 14, 23, 16]
    taxes = {21: 11, 18: 16, 16: 6, 12: 5, 14: 11, 11: 8, 15: 11, 4: 3, 9: 2, 23: 14, 7: 5, 20: 12, 6: 2, 8: 3, 17: 6, 13: 3, 3: 3, 2: 1, 10: 5}
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
