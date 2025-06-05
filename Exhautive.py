from itertools import permutations

# Representasi jarak antar kota
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i+1]]
    cost += distance_matrix[route[-1]][route[0]]  # Kembali ke kota awal
    return cost

cities = [0, 1, 2, 3]
min_cost = float('inf')
best_route = None

for perm in permutations(cities):
    cost = calculate_route_cost(perm)
    if cost < min_cost:
        min_cost = cost
        best_route = perm

print("Best route (Exhaustive Search):", best_route)
print("Minimum cost:", min_cost)
