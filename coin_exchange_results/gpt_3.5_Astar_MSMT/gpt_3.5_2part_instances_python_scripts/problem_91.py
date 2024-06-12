
import heapq

def initialize():
    coins = [36, 40, 17, 7, 15, 23, 18, 26, 29, 24, 15, 43, 13, 12, 31, 33, 30, 31, 26, 37, 14, 31, 43, 25, 30, 7, 37, 27, 221, 13, 26, 21]
    tax_values = {36: 14, 27: 19, 21: 6, 13: 8, 23: 17, 26: 17, 15: 6, 25: 7, 31: 20, 30: 5, 18: 14, 12: 6, 37: 2, 221: 18, 14: 13, 24: 10, 33: 4, 43: 11, 29: 18, 40: 1, 7: 6, 17: 2}
    target_sum = 445
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    queue = [(0, 0, [], (0, 0, 0))]
    return (coins, tax_values, target_sum, visited_costs, queue)

def a_star():
    (coins, tax_values, target_sum, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        (total_value, prev_coin, total_tax) = state
        if (total_value == target_sum):
            return actions
        for coin in coins:
            if ((coin not in actions) and ((total_value + coin) <= target_sum)):
                if (((coin < prev_coin) and ((coin % 2) == 0)) or ((coin >= prev_coin) and ((coin % 2) != 0))):
                    coin_tax = tax_values[coin]
                    new_total_tax = (total_tax + coin_tax)
                    new_state = ((total_value + coin), coin, new_total_tax)
                    new_cost = (g + coin_tax)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + new_total_tax), new_cost, (actions + [coin]), new_state))
    return None
print(a_star())
