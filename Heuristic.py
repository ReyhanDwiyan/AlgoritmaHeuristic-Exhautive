# Matriks jarak yang merepresentasikan jarak antar kota
# Baris dan kolom mewakili kota, nilai mewakili jarak antar kota
distance_matrix = [
    [0, 10, 15, 20],   # Jarak dari kota 0 ke kota lainnya
    [10, 0, 35, 25],   # Jarak dari kota 1 ke kota lainnya
    [15, 35, 0, 30],   # Jarak dari kota 2 ke kota lainnya
    [20, 25, 30, 0]    # Jarak dari kota 3 ke kota lainnya
]

def greedy_tsp(start, distance_matrix):
    # Inisialisasi variabel
    n = len(distance_matrix)                # Mendapatkan jumlah kota
    visited = [False] * n                   # Array untuk menandai kota yang sudah dikunjungi
    route = [start]                         # Menyimpan rute perjalanan, dimulai dari kota awal
    visited[start] = True                   # Menandai kota awal sebagai sudah dikunjungi
    current = start                         # Menyimpan posisi kota saat ini
    total_cost = 0                         # Menyimpan total jarak yang ditempuh

    # Perulangan untuk mengunjungi semua kota
    for _ in range(n - 1):
        nearest = None                      # Menyimpan kota terdekat berikutnya
        min_dist = float('inf')            # Menyimpan jarak minimum ke kota berikutnya
        
        # Mencari kota terdekat yang belum dikunjungi
        for i in range(n):
            if not visited[i] and distance_matrix[current][i] < min_dist:
                min_dist = distance_matrix[current][i]    # Update jarak minimum
                nearest = i                               # Update kota terdekat

        route.append(nearest)               # Menambahkan kota terdekat ke rute
        visited[nearest] = True            # Menandai kota terdekat sebagai sudah dikunjungi
        total_cost += min_dist            # Menambahkan jarak ke total cost
        current = nearest                 # Memperbarui posisi kota saat ini

    # Menambahkan jarak kembali ke kota awal
    total_cost += distance_matrix[current][start]
    route.append(start)                    # Menambahkan kota awal ke rute untuk kembali
    return route, total_cost              # Mengembalikan rute dan total jarak

# Memanggil fungsi dan menampilkan hasil
route, cost = greedy_tsp(0, distance_matrix)
print("Heuristic:", route)                # Menampilkan rute perjalanan
print("Total Cost:", cost)                # Menampilkan total jarak yang ditempuh
