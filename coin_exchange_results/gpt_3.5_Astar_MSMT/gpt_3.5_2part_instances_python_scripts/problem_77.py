
import heapq

def initialize():
    coins = [26, 32, 14, 36, 14, 8, 9, 3, 8, 18, 7, 23, 6, 20, 34, 8, 37, 19, 15, 6, 2, 13, 37, 7, 31, 2, 7, 4, 17, 9, 4, 22, 7, 16, 33, 14, 11, 30, 36, 14, 34, 37, 36, 37, 32, 38, 15, 17, 19, 14]
    tax_values = {17: 16, 4: 2, 15: 2, 8: 1, 19: 5, 9: 4, 23: 7, 3: 2, 16: 13, 2: 1, 38: 13, 11: 2, 31: 6, 7: 6, 36: 8, 14: 8, 37: 17, 32: 5, 6: 1, 13: 11, 22: 9, 20: 8, 18: 4, 30: 6, 34: 2, 33: 1, 26: 3}
    target_sum = 396
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
