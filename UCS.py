import heapq
import graph as graf
import Jarak_Euclidean as jarak
import queue

# Implementasi algoritma Uniform Cost Search (UCS)
def ucs(g, start, goal):
    # Inisialisasi heap (prioritas antrian)
    heap = []
    # Memasukkan titik awal ke dalam heap
    heapq.heappush(heap, (0, start))

    # Inisialisasi set untuk menyimpan node yang sudah dieksplorasi
    explored = set()

    # Inisialisasi kamus untuk menyimpan nilai cost terkecil untuk mencapai suatu node
    cost_so_far = {}
    # Memasukkan titik awal dengan cost 0 ke dalam kamus cost_so_far
    cost_so_far[start] = 0

    # Inisialisasi kamus untuk menyimpan jalur terpendek untuk mencapai suatu node
    came_from = {}

    # Melakukan pencarian
    while heap:
        # Mengambil node dengan cost terkecil dari heap
        (cost, current) = heapq.heappop(heap)

        # Jika node saat ini merupakan tujuan, maka pencarian selesai
        if current == goal:
            break

        # Menandai node saat ini sebagai sudah dieksplorasi
        explored.add(current)

        # Mengeksplorasi tetangga dari node saat ini
        for move in g.getmoves(current):
            next_node = move
            move_cost = g.getBobot()
            cost_to_next_node = move_cost[current][move]

            # Menghitung total cost untuk mencapai next_node melalui current
            new_cost = cost_so_far[current] + cost_to_next_node

            # Jika next_node belum pernah dieksplorasi atau memiliki cost lebih kecil, update cost_so_far dan heap
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost
                heapq.heappush(heap, (priority, next_node))
                came_from[next_node] = current

    # Jika goal tidak dapat dicapai, kembalikan None
    if goal not in came_from:
        return None

    # Membalikan jalur terpendek dari start ke goal
    path = [goal]
    while goal != start:
        goal = came_from[goal]
        path.append(goal)
    path.reverse()

    return path
