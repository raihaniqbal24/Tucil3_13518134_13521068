import Jarak_Euclidean as jarak
from queue import PriorityQueue

class Graph:
    # Inisiasi graf
    def __init__(self, banyakNode, listNode, listKoordinat, adjacencyMatrix):
        self.__banyakNode = banyakNode
        self.__listnode = listNode
        self.__adjacencyMatrix = adjacencyMatrix
        self.__listKoordinat = listKoordinat
        self.__bobot = [[0 for y in range(self.__banyakNode)] for x in range(self.__banyakNode)]
        
        # Mengubah adjacency matrix menjadi adjacency list
        self.__adjacencyList = []
        for x in range(self.__banyakNode):
            moves = []
            for y in range(self.__banyakNode):
                if(self.__adjacencyMatrix[x][y] == 1):
                    moves = moves + [y]
            self.__adjacencyList = self.__adjacencyList + [moves]
            
        # Menghitung bobot dari setiap edge
        for x in range(self.__banyakNode):
            for y in range(self.__banyakNode):
                if(self.__adjacencyMatrix[x][y] == 1):
                    m = self.__listKoordinat[x]
                    n = self.__listKoordinat[y]
                    bobot = jarak.euclidean(m,n) 
                    self.__bobot[x][y] = bobot
    
    # mengembalikan path dari start ke tujuan
    def path(self, awal, curr):
        path = [curr]
        while curr in awal:
            curr = awal[curr]
            path += [curr] 
        return path
    
    # mengecek apakah node ada di array_node
    def cek_node(self, node, array_node):
        for x in range(len(array_node)):
            if node == array_node[x]:
                return True
        return False
    
    # mengembalikan jumlah node
    def getNumNode(self):
        return self.__banyakNode  
    
    # mengembalikan node
    def getNode(self, idxNode):
        return self.__listnode[idxNode]
    
    # mengembalikan index node
    def getIdxNode(self, node):
        for x in range(self.__banyakNode):
            if(self.__listnode[x] == node):
                return x
        return -1
    
    # mengembalikan list node dengan idx node yang dimasukkan
    def idxToNode(self, listnode):
        list = []
        for x in listnode:
            list += [self.getNode(x)]
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
    def idxToKoordinatX(self, listnode):
        koordinat_X = []
        for x in listnode:
            koordinat_X = koordinat_X + [self.getNodeKoordinat(x)[0]]
        return koordinat_X

    # mengembalikan list koordinat Y
    def idxToKoordinatY(self, listnode):
        koordinat_Y = []
        for x in listnode:
            koordinat_Y = koordinat_Y + [self.getNodeKoordinat(x)[1]]
        return koordinat_Y

    # mengembalikan moves dari node
    def getmoves(self, kemana):
        return self.__adjacencyList[kemana]
    
    # # mengembalikan bobot dari node
    # def getBobot(self, dari, ke):
    #     return self.__bobot[dari][ke]

    # algoritma A*
    def a_star(self, start, tujuan):
        # inisiasi
        banyakNode = self.__banyakNode
        count = 0
        antrian = PriorityQueue()
        antrian.put((0, count, start))
        asal = {}

        # inisiasi g(n) dan f(n)
        g = [float("inf") for x in range(banyakNode)]
        g[start] = 0

        f = [float("inf") for x in range(banyakNode)]
        f[start] = jarak.euclidean(self.__listKoordinat[start],self.__listKoordinat[tujuan])

        # inisiasi dikunjungi
        dikunjungi = {start} 

        # looping
        while (not antrian.empty()):
            # mengambil node dengan f(n) terkecil
            current = antrian.get()[2]
            dikunjungi.remove(current)
            
            # jika node tujuan ditemukan
            if(current == tujuan):
                return self.path(asal, current)
            
            # looping untuk setiap node yang bisa diakses dari node current
            for moves in self.__adjacencyList[current]:
                # menghitung g(n) dan f(n)
                temp_g = g[current] + jarak.euclidean(self.__listKoordinat[current], self.__listKoordinat[moves])
                # jika g(n) lebih kecil dari g(n) sebelumnya
                if(temp_g < g[moves]):
                    asal[moves] = current
                    g[moves] = temp_g
                    f[moves] = temp_g + jarak.euclidean(self.__listKoordinat[moves], self.__listKoordinat[current])
                    # jika node moves belum ada di antrian
                    if (moves not in dikunjungi):
                        count = count + 1
                        antrian.put((f[moves], count, moves))
                        dikunjungi.add(moves)
                        
        return None
    