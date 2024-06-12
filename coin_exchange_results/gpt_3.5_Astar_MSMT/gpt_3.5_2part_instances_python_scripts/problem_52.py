
import heapq

def initialize():
    coins = [31, 9, 2, 24, 32, 6, 13, 29, 33, 22, 12, 28, 10, 7, 33, 15, 28, 7, 14, 26, 1, 10, 28, 30, 7, 29, 17, 2, 28, 13, 28, 17, 3, 4, 4, 4, 13, 3, 19, 2, 4, 26, 27, 27, 11, 25, 12]
    tax_values = {2: 1, 33: 8, 9: 9, 31: 3, 19: 11, 17: 8, 28: 3, 24: 12, 6: 1, 22: 7, 26: 7, 27: 5, 29: 9, 4: 4, 10: 3, 3: 2, 11: 3, 15: 12, 7: 2, 1: 1, 12: 3, 30: 2, 14: 12, 32: 7, 13: 2, 25: 9}
    target_sum = 337
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
