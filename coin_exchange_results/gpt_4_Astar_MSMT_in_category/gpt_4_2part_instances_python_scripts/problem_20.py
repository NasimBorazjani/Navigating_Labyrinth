
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 246
    coins = [12, 15, 3, 24, 10, 18, 10, 20, 21, 17, 9, 8, 2, 11, 5, 5, 3, 8, 6, 12, 20, 22, 4, 5, 17, 5, 14, 10, 15, 8, 9, 22, 4, 7, 15, 16, 4, 2, 5, 9, 24, 23, 3, 7, 20, 9, 12, 10, 4, 4, 8, 24, 11, 20, 2, 15]
    taxes = {20: 14, 15: 15, 6: 1, 14: 1, 7: 2, 18: 5, 2: 1, 16: 5, 21: 9, 3: 3, 12: 3, 17: 10, 22: 4, 10: 9, 4: 3, 11: 1, 5: 1, 23: 13, 24: 4, 9: 9, 8: 4}
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