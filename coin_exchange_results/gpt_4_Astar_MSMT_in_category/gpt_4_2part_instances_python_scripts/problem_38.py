
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 300
    coins = [30, 24, 27, 14, 29, 17, 4, 21, 20, 14, 19, 23, 18, 4, 12, 9, 24, 26, 21, 17, 3, 13, 25, 20, 16, 12, 2, 9, 17, 5, 6, 24, 13, 11, 6, 15, 13, 5, 13, 25, 10, 15, 10, 3, 2, 18, 7, 23, 5, 18, 21, 6]
    taxes = {14: 11, 3: 1, 18: 5, 21: 1, 27: 2, 19: 14, 6: 6, 25: 8, 5: 3, 29: 4, 7: 6, 24: 10, 10: 2, 13: 9, 9: 1, 11: 8, 16: 10, 2: 1, 12: 12, 15: 4, 23: 17, 17: 9, 26: 13, 30: 17, 4: 3, 20: 6}
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
