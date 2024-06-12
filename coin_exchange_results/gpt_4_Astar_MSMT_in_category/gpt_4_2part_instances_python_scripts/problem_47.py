
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 342
    coins = [18, 26, 17, 17, 16, 27, 30, 3, 4, 2, 24, 26, 29, 23, 2, 31, 25, 25, 4, 24, 14, 29, 4, 34, 34, 23, 35, 23, 28, 18, 8, 10, 17, 8, 22, 32]
    taxes = {27: 14, 14: 1, 18: 3, 22: 9, 10: 8, 3: 2, 32: 20, 35: 16, 8: 3, 30: 20, 25: 18, 4: 3, 28: 12, 26: 16, 29: 2, 24: 20, 16: 6, 17: 3, 31: 9, 2: 2, 23: 17, 34: 17}
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
