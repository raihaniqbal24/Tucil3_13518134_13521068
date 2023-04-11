import Jarak_Euclidean as jarak
import queue 


class Graph:
    
    # Inisiasi graf
    def __init__(self, numNode, listNode, listKoordinat, adjacencyMatrix):
        self.__numNode = numNode
        self.__listnode = listNode
        self.__adjacencyMatrix = adjacencyMatrix
        self.__listKoordinat = listKoordinat
        self.__bobot = [[0 for j in range(self.__numNode)] for i in range(self.__numNode)]
        
        # Menghitung bobot dari setiap edge
        for i in range(self.__numNode):
            for j in range(self.__numNode):
                if(self.__adjacencyMatrix[i][j] == 1):
                    x = self.__listKoordinat[i]
                    y = self.__listKoordinat[j]
                    bobot = jarak.euclideanDistance(x,y) 
                    self.__bobot[i][j] = bobot

        # Mengubah adjacency matrix menjadi adjacency list
        self.__adjacencyList = []
        for i in range(self.__numNode):
            moves = []
            for j in range(self.__numNode):
                if(self.__adjacencyMatrix[i][j] == 1):
                    moves = moves + [j]
            self.__adjacencyList = self.__adjacencyList + [moves]
    
    # mengembalikan list koordinat x
    def reconstruct_path(self, awal, curr):
        path = [curr]
        while curr in awal:
            curr = awal[curr]
            path = [curr] + path
        return path
    
    # mengecek apakah node ada di array_node
    def cek_node(self, node, array_node):
        for i in range(len(array_node)):
            if node == array_node[i]:
                return True
        return False
    
    # mengembalikan jumlah node
    def getNumNode(self):
        return self.__numNode  
    
    # mengembalikan node
    def getNode(self, idxNode):
        return self.__listnode[idxNode]
    
    # mengembalikan index node
    def getIdxNode(self, node):
        for i in range(self.__numNode):
            if(self.__listnode[i] == node):
                return i
        return -1
    
    # mengembalikan list node dengan idx node yang dimasukkan
    def idxToNodeList(self, idxList):
        list = []
        for idx in idxList:
            list = list + [self.getNode(idx)]
        return list
    
    # mengembalikan list node
    def getListNode(self):
        return self.__listnode

    # mengembalikan adjacency matrix
    def getAdjacencyMatrix(self):
        return self.__adjacencyMatrix
    
    # mengembalikan list koordinat
    def getListKoordinat(self):
        return self.__listKoordinat

    # mengembalikan koordinat node
    def getNodeKoordinat(self, idxNode):
        return self.__listKoordinat[idxNode]

    # mengembalikan koordinat X node
    def getKoordinatX(self, idxNode):
        return self.getNodeKoordinat(idxNode)[0]
    
    # mengembalikan koordinat Y node
    def getKoordinatY(self, idxNode):
        return self.getNodeKoordinat(idxNode)[1]
    
    # mengembalikan adjacency list
    def getAdjacencyList(self):
        return self.__adjacencyList
    
    # mengembalikan bobot
    def getBobot(self):
        return self.__bobot

    # mengembalikan adjacency list
    def getAdjacencyList(self):
        return self.__adjacencyList

    # mengembalikan list koordinat X
    def idxToKoordinatX(self, idxList):
        koordinat_X = []
        for idx in idxList:
            koordinat_X = koordinat_X + [self.getNodeKoordinat(idx)[0]]
        return koordinat_X

    # mengembalikan list koordinat Y
    def idxToKoordinatY(self, idxList):
        koordinat_Y = []
        for idx in idxList:
            koordinat_Y = koordinat_Y + [self.getNodeKoordinat(idx)[1]]
        return koordinat_Y

    # mengembalikan moves dari node
    def getmoves(self, kemana):
        return self.__adjacencyList[kemana]
    
    
    
    # Algoritma UCS (Uniform Cost Search)
    # Algoritma UCS (Uniform Cost Search)
def ucs(self, start, goal):
    # Inisiasi open list dan closed list
    open_list = queue.PriorityQueue()
    open_list.put((0, start)) # mengatur prioritas berdasarkan cost
    closed_list = set()
    # Inisiasi g(n) untuk start node
    g = {start: 0}
    # Inisiasi parent node
    parent = {}

    # Loop hingga open list kosong
    while not open_list.empty():
        # Mengambil node dengan cost terendah
        cost, current = open_list.get()
        # Menambahkan current node ke closed list
        closed_list.add(current)

        # Jika current node sama dengan goal node
        if current == goal:
            # Mencari path dari start node ke goal node
            path = self.reconstruct_path(parent, current)
            return path, g[current]

        # Loop untuk setiap moves dari current node
        for move in self.__adjacencyList[current]:
            # Menghitung cost baru
            new_cost = g[current] + self.__bobot[current][move]

            # Jika move belum pernah dikunjungi atau cost baru lebih kecil dari cost sebelumnya
            if move not in closed_list or new_cost < g[move]:
                # Update g(n) dan parent
                g[move] = new_cost
                parent[move] = current
                # Masukkan node ke open list dengan prioritas berdasarkan cost
                open_list.put((g[move], move))

    # Jika goal node tidak ditemukan, return None
    return None, None

    
    

