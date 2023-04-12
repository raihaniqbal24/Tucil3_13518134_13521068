import heapq
import Graph as graf
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
        # print(current)
        # print(cost)

        # Jika node saat ini merupakan tujuan, maka pencarian selesai
        if current == goal:
            break

        # Menandai node saat ini sebagai sudah dieksplorasi
        explored.add(current)
        # print(g.getmoves(current))

        # Mengeksplorasi tetangga dari node saat ini
        for move in g.getmoves(current):
            # print(move)
            next_node = move
            move_cost = g.getBobot()
            # print(move_cost[current][move])
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









# def ucs(g, start, goal):
#     # Inisiasi open list dan closed list
#     open_list = queue.PriorityQueue()
#     open_list.put((0, start)) # mengatur prioritas berdasarkan cost
#     closed_list = set()
#     # Inisiasi g(n) untuk start node
#     g = {start: 0}
#     # Inisiasi parent node
#     parent = {}

#     # Loop hingga open list kosong
#     while not open_list.empty():
#         # Mengambil node dengan cost terendah
#         cost, current = open_list.get()
#         # Menambahkan current node ke closed list
#         closed_list.add(current)

#         # Jika current node sama dengan goal node
#         if current == goal:
#             # Mencari path dari start node ke goal node
#             path = g.reconstruct_path(parent, current)
#             return path, g[current]

#         # Loop untuk setiap moves dari current node
#         for move in g.getMoves(current):
#             # Menghitung cost baru
#             new_cost = g[current] +  jarak.euclideanDistance(g.getNodeKoordinat(current), g.getNodeKoordinat(move))

#             # Jika move belum pernah dikunjungi atau cost baru lebih kecil dari cost sebelumnya
#             if move not in closed_list or new_cost < g[move]:
#                 # Update g(n) dan parent
#                 g[move] = new_cost
#                 parent[move] = current
#                 # Masukkan node ke open list dengan prioritas berdasarkan cost
#                 open_list.put((g[move], move))

#     # Jika goal node tidak ditemukan, return None
#     return None, None