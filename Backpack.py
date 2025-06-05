import itertools  # Mengimpor modul itertools untuk menghasilkan kombinasi

# Kelas untuk merepresentasikan sebuah item
class Item:
    def __init__(self, name, weight, value):
        self.name = name      # Menyimpan nama item
        self.weight = weight  # Menyimpan berat item
        self.value = value    # Menyimpan nilai item
    
    def __repr__(self):
        # Menentukan cara menampilkan objek item saat diprint
        return f"{self.name} (Weight: {self.weight}, Value: {self.value})"

# Kelas utama untuk optimasi knapsack
class KnapsackOptimizer:
    def __init__(self):
        self.items = []           # Menyimpan daftar item
        self.capacity = 0         # Menyimpan kapasitas ransel
    
    def add_item(self, name, weight, value):
        # Menambahkan item baru ke daftar
        self.items.append(Item(name, weight, value))
    
    def set_capacity(self, capacity):
        # Mengatur kapasitas ransel
        self.capacity = capacity
    
    def exhaustive_search(self):
        """Mencoba semua kombinasi item yang mungkin"""
        best_value = 0            # Menyimpan nilai terbaik
        best_combination = []     # Menyimpan kombinasi terbaik
        
        # Menghasilkan semua kombinasi yang mungkin
        for i in range(len(self.items) + 1):
            for combination in itertools.combinations(self.items, i):
                # Menghitung total berat dan nilai untuk setiap kombinasi
                total_weight = sum(item.weight for item in combination)
                total_value = sum(item.value for item in combination)
                
                # Memeriksa apakah kombinasi ini valid dan lebih baik
                if total_weight <= self.capacity and total_value > best_value:
                    best_value = total_value
                    best_combination = combination
        
        return best_combination, sum(item.weight for item in best_combination), best_value
    
    def heuristic_search(self):
        """Pendekatan greedy berdasarkan rasio nilai/berat"""
        # Mengurutkan item berdasarkan rasio nilai/berat secara menurun
        sorted_items = sorted(self.items, key=lambda item: item.value / item.weight, reverse=True)
        
        selected_items = []    # Menyimpan item yang dipilih
        total_weight = 0      # Menyimpan total berat
        total_value = 0       # Menyimpan total nilai
        
        # Memilih item berdasarkan rasio terbaik
        for item in sorted_items:
            if total_weight + item.weight <= self.capacity:
                selected_items.append(item)
                total_weight += item.weight
                total_value += item.value
        
        return selected_items, total_weight, total_value

def main():
    optimizer = KnapsackOptimizer()    # Membuat objek optimizer
    
    print("===== KNAPSACK OPTIMIZER =====")
    
    # Mendapatkan kapasitas ransel dari pengguna
    capacity = int(input("Enter backpack capacity: "))
    optimizer.set_capacity(capacity)
    
    # Mendapatkan jumlah dan detail item dari pengguna
    num_items = int(input("Enter number of items: "))
    
    for i in range(num_items):
        print(f"\nItem {i+1}:")
        name = input("  Name: ")
        weight = int(input("  Weight: "))
        value = int(input("  Value: "))
        optimizer.add_item(name, weight, value)
    
    # Menampilkan hasil pencarian exhaustive
    print("\n===== RESULTS =====")
    print("\nEXHAUSTIVE SEARCH (tries all combinations):")
    items, weight, value = optimizer.exhaustive_search()
    print("Selected items:")
    for item in items:
        print(f"  - {item}")
    print(f"Total weight: {weight}")
    print(f"Total value: {value}")
    
    # Menampilkan hasil pencarian heuristik
    print("\nHEURISTIC SEARCH (based on value/weight ratio):")
    items, weight, value = optimizer.heuristic_search()
    print("Selected items:")
    for item in items:
        print(f"  - {item}")
    print(f"Total weight: {weight}")
    print(f"Total value: {value}")

# Menjalankan program jika file dieksekusi langsung
if __name__ == "__main__":
    main()