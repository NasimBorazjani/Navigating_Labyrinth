
import heapq

def initialize():
    coins = [14, 8, 11, 30, 3, 3, 27, 16, 19, 4, 6, 14, 7, 2, 39, 103, 15, 100, 27, 36, 7, 36, 13, 7, 18, 39, 14, 3, 28]
    tax_values = {13: 11, 18: 8, 36: 15, 11: 4, 6: 1, 16: 8, 100: 12, 39: 10, 28: 9, 27: 20, 103: 6, 19: 5, 30: 14, 2: 1, 4: 3, 3: 3, 15: 10, 8: 5, 7: 2, 14: 14}
    target_sum = 410
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
