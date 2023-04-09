import heapq
import math
import matplotlib.pyplot as plt
import networkx as nx

# Membaca file graf (matriks ketetanggaan berbobot) dan menyimpannya dalam bentuk graf (dictionary of dictionary).
def read_graph(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        graph = {}
        for i, line in enumerate(lines):
            row = [int(x) for x in line.strip().split()]
            graph[i] = {}
            for j, weight in enumerate(row):
                if weight != 0:
                    graph[i][j] = weight
        return graph

# Menampilkan peta/graf menggunakan library NetworkX.
def show_graph(graph):
    G = nx.DiGraph()
    for u, edges in graph.items():
        for v, weight in edges.items():
            G.add_edge(u, v, weight=weight)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Menerima input simpul asal dan simpul tujuan dari pengguna.
def get_start_and_goal(graph):
    start = int(input('Masukkan simpul asal: '))
    goal = int(input('Masukkan simpul tujuan: '))
    if start not in graph or goal not in graph:
        print('Simpul asal atau tujuan tidak valid.')
        exit(1)
    return start, goal

# Algoritma UCS (Uniform Cost Search).
def ucs(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == goal:
            return path + [node], cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                heapq.heappush(queue, (cost + weight, neighbor, path + [node]))
    return [], math.inf

# Algoritma A* (A-star).
def a_star(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == goal:
            return path + [node], cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                heur = math.sqrt((neighbor[0] - goal[0]) ** 2 + (neighbor[1] - goal[1]) ** 2)
                heapq.heappush(queue, (cost + weight + heur, neighbor, path + [node]))
    return [], math.inf

# Contoh penggunaan.
graph = read_graph('graph.txt')
show_graph(graph)
start, goal = get_start_and_goal(graph)
print('UCS:', ucs(graph, start, goal))
print('A*:', a_star(graph, start, goal))
