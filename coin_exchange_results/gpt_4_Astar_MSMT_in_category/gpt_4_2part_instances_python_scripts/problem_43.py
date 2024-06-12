
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 322
    coins = [69, 32, 32, 6, 19, 13, 21, 68, 32, 16, 21, 29, 20, 13, 21, 24, 26, 5, 23, 18, 16, 24, 2, 17, 15, 30, 26]
    taxes = {30: 3, 20: 11, 24: 15, 26: 6, 68: 2, 29: 5, 13: 2, 2: 1, 17: 2, 32: 11, 18: 4, 15: 9, 5: 3, 21: 11, 69: 19, 6: 3, 16: 4, 23: 17, 19: 15}
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
