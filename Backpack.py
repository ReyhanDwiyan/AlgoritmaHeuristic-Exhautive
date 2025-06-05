import itertools

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
    
    def __repr__(self):
        return f"{self.name} (Weight: {self.weight}, Value: {self.value})"

class KnapsackOptimizer:
    def __init__(self):
        self.items = []
        self.capacity = 0
    
    def add_item(self, name, weight, value):
        self.items.append(Item(name, weight, value))
    
    def set_capacity(self, capacity):
        self.capacity = capacity
    
    def exhaustive_search(self):
        """Try all possible combinations of items."""
        best_value = 0
        best_combination = []
        
        # Generate all possible combinations of items
        for i in range(len(self.items) + 1):
            for combination in itertools.combinations(self.items, i):
                total_weight = sum(item.weight for item in combination)
                total_value = sum(item.value for item in combination)
                
                # Check if this combination is valid and better than current best
                if total_weight <= self.capacity and total_value > best_value:
                    best_value = total_value
                    best_combination = combination
        
        return best_combination, sum(item.weight for item in best_combination), best_value
    
    def heuristic_search(self):
        """Greedy approach based on value/weight ratio."""
        # Sort items by value/weight ratio in descending order
        sorted_items = sorted(self.items, key=lambda item: item.value / item.weight, reverse=True)
        
        selected_items = []
        total_weight = 0
        total_value = 0
        
        for item in sorted_items:
            if total_weight + item.weight <= self.capacity:
                selected_items.append(item)
                total_weight += item.weight
                total_value += item.value
        
        return selected_items, total_weight, total_value

def main():
    optimizer = KnapsackOptimizer()
    
    print("===== KNAPSACK OPTIMIZER =====")
    
    # Get backpack capacity
    capacity = int(input("Enter backpack capacity: "))
    optimizer.set_capacity(capacity)
    
    # Get items
    num_items = int(input("Enter number of items: "))
    
    for i in range(num_items):
        print(f"\nItem {i+1}:")
        name = input("  Name: ")
        weight = int(input("  Weight: "))
        value = int(input("  Value: "))
        
        optimizer.add_item(name, weight, value)
    
    print("\n===== RESULTS =====")
    
    # Exhaustive search
    print("\nEXHAUSTIVE SEARCH (tries all combinations):")
    items, weight, value = optimizer.exhaustive_search()
    print("Selected items:")
    for item in items:
        print(f"  - {item}")
    print(f"Total weight: {weight}")
    print(f"Total value: {value}")
    
    # Heuristic search
    print("\nHEURISTIC SEARCH (based on value/weight ratio):")
    items, weight, value = optimizer.heuristic_search()
    print("Selected items:")
    for item in items:
        print(f"  - {item}")
    print(f"Total weight: {weight}")
    print(f"Total value: {value}")

if __name__ == "__main__":
    main()