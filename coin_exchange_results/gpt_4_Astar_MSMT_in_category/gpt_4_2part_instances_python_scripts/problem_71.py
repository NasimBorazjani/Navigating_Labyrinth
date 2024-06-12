
import heapq

def initialize():
    initial_state = (0, 0, 0, ())
    goal_state = 400
    coins = [18, 11, 14, 3, 7, 18, 40, 3, 35, 30, 24, 29, 34, 11, 17, 14, 14, 10, 5, 40, 4, 31, 25, 14, 39, 12, 26, 24, 3, 8, 34, 2, 22, 189, 40]
    taxes = {29: 9, 40: 8, 30: 5, 17: 16, 3: 3, 5: 3, 2: 2, 22: 17, 11: 1, 14: 4, 8: 5, 18: 11, 26: 8, 39: 15, 7: 1, 31: 2, 24: 17, 189: 5, 12: 4, 25: 10, 35: 18, 10: 1, 4: 3, 34: 16}
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
