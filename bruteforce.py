import time
import csv

max_cost = 500

def get_dataset(name):
    dataset = []
    with open(name, newline='') as dataset_file:
        reader = csv.DictReader(dataset_file)
        for row in reader:
            dataset.append({
                "name": row["name"],
                "price": float(row["price"]),
                "value": ((float(row["profit"]) / 100 + 1) * float(row["price"])) - float(row["price"])
            })
        return dataset

def brute_force():
    dataset = get_dataset("datasets/dataset0_Python+P7.csv")
    best_possibilities = {}
    max_value = 0
    number_of_possibles = 2**len(dataset)
    for i in range(0, number_of_possibles):
        way = str(bin(i))[2::]
        auctions = []
        weight = 0
        value = 0
        index = len(way) - 1
        for boolean in range(0, len(way)):
            take = int(way[boolean])
            if take:
                auction = dataset[index]
                auctions.append(auction["name"])
                value += auction["value"]
                weight += auction["price"]
            index -= 1
        if weight <= max_cost and max_value <= value:
            try:
                best_possibilities[value].append({
                    "weight": weight,
                    "auctions": auctions,
                })
            except KeyError:
                best_possibilities = {}
                best_possibilities[value] = [
                    {
                        "weight": weight,
                        "auctions": auctions,
                    }
                ]

            max_value = value
    best_possibilities[max_value].sort(key=lambda x: x["weight"], reverse=True)
    print(f"The best is {best_possibilities[max_value][0]} for a benefit of {max_value} and a cost of {best_possibilities[max_value][0]['weight']}")
    return best_possibilities[max_value][0]

if __name__ == "__main__":
    print("Brute force")
    start = time.time()
    result = brute_force()
    end = time.time()
    print(f"Brute force end in {end - start}s to get result")