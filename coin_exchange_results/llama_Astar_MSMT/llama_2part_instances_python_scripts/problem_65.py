
import heapq

def initialize():
    coins = [9, 30, 18, 32, 31, 20, 34, 9, 12, 18, 14, 16, 29, 37, 37, 6, 24, 10, 10, 35, 23, 4, 30, 121, 31, 16, 35]
    tax_values = {35: 20, 4: 2, 18: 11, 24: 10, 10: 7, 14: 3, 37: 1, 16: 14, 12: 7, 6: 2, 29: 18, 34: 19, 121: 10, 31: 7, 30: 12, 32: 12, 23: 8, 20: 8, 9: 9}
    target_sum = 406
    num_coins = len(coins)
    visited_costs = {}
    visited_costs[()] = 0
    queue = [(0, 0, [], ())]
    return (coins, tax_values, target_sum, num_coins, visited_costs, queue)

def a_star():
    (coins, tax_values, target_sum, num_coins, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (sum(state) == target_sum):
            return actions
        for coin_ind in range(num_coins):
            if ((coin_ind not in state) and ((not state) or (((coins[coin_ind] % 2) == 0) and (state[(- 1)] < coins[coin_ind])) or (((coins[coin_ind] % 2) == 1) and (state[(- 1)] >= coins[coin_ind])))):
                new_state = (state + (coin_ind,))
                new_cost = (g + tax_values[coins[coin_ind]])
                if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, target_sum, coins, tax_values)
                    heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [coins[coin_ind]]), new_state))
    return None

def heuristic(state, target_sum, coins, tax_values):
    h = 0
    coins = sorted(coins, reverse=True)
    for coin_ind in state:
        if ((sum(state) + coins[coin_ind]) <= target_sum):
            h += tax_values[coins[coin_ind]]
    return h
print(a_star())
