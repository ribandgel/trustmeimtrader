import time
import numpy

stock_for_brute_force = [
    {"name": "action_1", "cost": 20, "stonks": 5},
    {"name": "action_2", "cost": 30, "stonks": 10},
    {"name": "action_3", "cost": 50, "stonks": 15},
    {"name": "action_4", "cost": 70, "stonks": 20},
    {"name": "action_5", "cost": 60, "stonks": 17},
    {"name": "action_6", "cost": 80, "stonks": 25},
    {"name": "action_7", "cost": 22, "stonks": 7},
    {"name": "action_8", "cost": 26, "stonks": 11},
    {"name": "action_9", "cost": 48, "stonks": 13},
    {"name": "action_10", "cost": 34, "stonks": 27},
    {"name": "action_11", "cost": 42, "stonks": 17},
    {"name": "action_12", "cost": 110, "stonks": 9},
    {"name": "action_13", "cost": 38, "stonks": 23},
    {"name": "action_14", "cost": 14, "stonks": 1},
    {"name": "action_15", "cost": 18, "stonks": 3},
    {"name": "action_16", "cost": 8, "stonks": 8},
    {"name": "action_17", "cost": 4, "stonks": 12},
    {"name": "action_18", "cost": 10, "stonks": 14},
    {"name": "action_19", "cost": 24, "stonks": 21},
    {"name": "action_20", "cost": 114, "stonks": 18},
]

def brute_force():
    print("sum", sum(stock["stonks"] for stock in stock_for_brute_force))
    # Calculate each possibility and keep the best one.
    max_cost = 500
    OPT = numpy.zeros(shape=(len(stock_for_brute_force)+1, sum(stock["stonks"] for stock in stock_for_brute_force)))
    ACTIONS = numpy.zeros(shape=(len(stock_for_brute_force)+1, sum(stock["stonks"] for stock in stock_for_brute_force)),dtype=object)

    def sum_value(i,j):
        v = 0
        for index in range(i-1,j):
            v = v + stock_for_brute_force[index]["stonks"]
        return v

    for i in range(1,len(stock_for_brute_force)):
        for value in range(1,sum_value(1,i)):
            #breakpoint()
            if value > sum_value(1,i-1):
                OPT[i][value] = stock_for_brute_force[i-1]["cost"] + OPT[i-1][max(0, value - stock_for_brute_force[i-1]["stonks"])]
                if not ACTIONS[i-1][value]:
                    ACTIONS[i][value] = [stock_for_brute_force[i-1]]
                else:
                    ACTIONS[i][value] = ACTIONS[i-1][max(0, value - stock_for_brute_force[i-1]["stonks"])] + [stock_for_brute_force[i-1]]
            else:
                no_take = OPT[i-1][value]
                take =  stock_for_brute_force[i-1]["cost"] + OPT[i-1][max(0, value - stock_for_brute_force[i-1]["stonks"])]
                minimum = min(take, no_take)
                if minimum == take:
                    if not ACTIONS[i-1][max(0, value - stock_for_brute_force[i-1]["stonks"])]:
                        ACTIONS[i][value] = [stock_for_brute_force[i-1]]
                    else:
                        ACTIONS[i][value] = ACTIONS[i-1][max(0, value - stock_for_brute_force[i-1]["stonks"])] + [stock_for_brute_force[i-1]]
                else:
                    ACTIONS[i][value] =  ACTIONS[i-1][value]
                OPT[i][value] =  min(take, no_take)

    solution = 0
    actions = []
    for value in range(1, sum_value(1, len(stock_for_brute_force))):
        if OPT[len(stock_for_brute_force)][value] <= max_cost:
            solution = value
            actions = ACTIONS[len(stock_for_brute_force)][value]
    print("Cost:", OPT[len(stock_for_brute_force)][solution])
    print(actions)
    return solution

def smart_way():
    return None

if __name__ == "__main__":
    print("Brute force")
    start = time.time()
    result = brute_force()
    end = time.time()
    print(f"Brute force end in {end - start}s to get result {result}")
    print("Smart way")
    start = time.time()
    result = smart_way()
    end = time.time()
    print(f"Smart way end in {end - start}s to get result {result}")