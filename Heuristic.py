# Ini jarak antar kota (matriks 4x4)
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def greedy_tsp(start, distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    route = [start]
    visited[start] = True
    current = start
    total_cost = 0

    for _ in range(n - 1):
        nearest = None
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and distance_matrix[current][i] < min_dist:
                min_dist = distance_matrix[current][i]
                nearest = i
        route.append(nearest)
        visited[nearest] = True
        total_cost += min_dist
        current = nearest

    total_cost += distance_matrix[current][start]  # kembali ke awal
    route.append(start)  # kembali ke kota awal
    return route, total_cost

# Panggil fungsi dan tampilkan hasil
route, cost = greedy_tsp(0, distance_matrix)
print("Greedy Heuristic Route:", route)
print("Total Cost:", cost)
