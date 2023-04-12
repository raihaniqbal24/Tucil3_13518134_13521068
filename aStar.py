import graph as graf
import Jarak_Euclidean as jarak
from queue import PriorityQueue


def aStar(g, start, goal):
    numOfNode = g.getNumNode()

    count = 0

    openSet = PriorityQueue()
    openSet.put((0, count, start))
    cameFrom = {}

    gScore = [float("inf") for j in range(numOfNode)]
    gScore[start] = 0

    fScore = [float("inf") for j in range(numOfNode)]
    fScore[start] = jarak.euclideanDistance(g.getNodeKoordinat(start),g.getNodeKoordinat(goal))

    openSetHash = {start} # nantinya untuk mengetahui apakah suatu node/neighbor sudah ada di openList

    while (not openSet.empty()):
        current = openSet.get()[2]
        openSetHash.remove(current)
        
        if(current == goal):
            return g.reconstruct_path(cameFrom, current)
        
        for neighbor in g.getmoves(current):
            temp_gScore = gScore[current] + jarak.euclideanDistance(g.getNodeKoordinat(current), g.getNodeKoordinat(neighbor))
            if(temp_gScore < gScore[neighbor]):
                cameFrom[neighbor] = current
                gScore[neighbor] = temp_gScore
                fScore[neighbor] = temp_gScore + jarak.euclideanDistance(g.getNodeKoordinat(neighbor), g.getNodeKoordinat(goal))
                if (neighbor not in openSetHash):
                    count += 1
                    openSet.put((fScore[neighbor], count, neighbor))
                    openSetHash.add(neighbor)
                    
    return -1


