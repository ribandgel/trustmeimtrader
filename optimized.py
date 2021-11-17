import time
import numpy
import csv

max_cost = 500

def get_dataset(name):
    dataset = []

    with open(name, newline='') as dataset_file:
        reader = csv.DictReader(dataset_file)
        for row in reader:
            price = float(row["price"])
            profit = ((float(row["profit"]) / 100 + 1) * price) - price
            if price < float(max_cost) and price > 0.0 and profit > 0.0:
                ratio = profit / price
                dataset.append({
                    "name": row["name"],
                    "price": price,
                    "profit": profit,
                    "ratio": ratio
                })
        return dataset

def optimized():
    dataset1 = get_dataset("datasets/dataset1_Python+P7.csv")
    dataset2 = get_dataset("datasets/dataset2_Python+P7.csv")
    dataset = dataset1 + dataset2
    # nlogn
    dataset.sort(key=lambda item: item["ratio"], reverse=True)
    final_cost = 0
    final_profit = 0
    selected_auctions = []
    for item in dataset:
        new_cost = item["price"]
        if (new_cost + final_cost) < max_cost:
            final_cost += new_cost
            final_profit += item["profit"]
            selected_auctions.append(item["name"])
    return selected_auctions, final_cost, final_profit

if __name__ == "__main__":
    print("Optimized")
    start = time.time()
    selected_auctions, cost, profit = optimized()
    end = time.time()
    print(f"Optimized version end in {end - start}s to get result")
    print(f"Selected auctions are {selected_auctions}")
    print(f"For a cost of {cost}")
    print(f"And {profit} profit")