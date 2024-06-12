
import heapq

def initialize():
    coins = [4, 17, 14, 12, 1, 3, 12, 10, 14, 9, 30, 20, 11, 17, 11, 16, 22, 17, 30, 5, 10, 16, 19, 27, 6, 18, 20, 19, 32, 25, 30, 15, 30, 21, 19, 25, 31, 33, 19, 10, 8, 16, 8]
    tax_values = {1: 1, 31: 13, 25: 13, 11: 3, 3: 1, 10: 8, 33: 14, 8: 4, 9: 9, 4: 1, 20: 4, 12: 8, 27: 13, 30: 14, 16: 10, 18: 9, 32: 5, 21: 20, 6: 4, 5: 5, 22: 11, 17: 11, 19: 2, 14: 10, 15: 6}
    target_sum = 328
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
