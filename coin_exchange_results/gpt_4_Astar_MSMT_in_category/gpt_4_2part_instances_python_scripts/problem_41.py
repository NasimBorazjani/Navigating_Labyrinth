
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 284
    coins = [20, 27, 20, 26, 2, 19, 25, 5, 14, 28, 7, 4, 20, 25, 9, 7, 3, 9, 27, 23, 2, 17, 25, 19, 10, 2, 8, 15, 3, 6, 24, 6, 22, 3, 10, 3, 2, 24, 7, 16, 2, 24, 21, 5, 23, 25, 10, 5, 20, 14, 24, 12, 11, 11, 13]
    taxes = {14: 7, 15: 15, 2: 2, 22: 7, 7: 1, 25: 7, 10: 4, 11: 11, 16: 11, 27: 8, 3: 2, 13: 5, 19: 10, 8: 5, 23: 18, 5: 4, 12: 4, 28: 6, 6: 4, 21: 3, 20: 15, 26: 1, 4: 4, 9: 9, 24: 6, 17: 13}
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
