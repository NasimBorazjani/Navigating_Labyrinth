
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 214
    coins = [4, 17, 8, 15, 6, 14, 2, 4, 16, 10, 6, 5, 14, 8, 18, 2, 17, 9, 17, 59, 3, 10, 21, 4, 9, 14, 14, 20, 14, 8, 14, 18, 5, 16, 14, 17, 5, 3]
    taxes = {15: 6, 5: 5, 17: 1, 14: 4, 2: 2, 8: 2, 10: 9, 59: 9, 16: 8, 4: 3, 18: 10, 20: 11, 21: 8, 6: 6, 9: 9, 3: 3}
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
