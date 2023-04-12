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
    