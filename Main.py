import os
import sys
import Graph as graf
import Jarak_Euclidean as jarak
import aStar as algo
import gmplot
import re
import baca_file as baca
import UCS as ucs

def main():
    print("Program Jarak Terpendek dengan A* dan UCS")
    print("----------------")
    # Memanggil fungsi baca_file() untuk membaca input dari file
    numNode, latitude, longitude, listKoordinat, listNode, adjacencyMatrix = baca.baca_file()
    
    # Menampilkan nilai variabel yang telah dibaca dari file
    print("numNode:", numNode)
    print("")
    print("latitude:", latitude)
    print("")
    print("longitude:", longitude)
    print("")
    print("listKoordinat:")
    for koordinat in listKoordinat:
        print(koordinat)
    print("")
    print("adjacencyMatrix:")
    for row in adjacencyMatrix:
        print(row)
    print("")
    
    # Inisiasi graf
    g = graf.Graph(numNode, listNode, listKoordinat, adjacencyMatrix)
    
    # Menampilkan node-node dari graf
    print("List of node dari peta yang dipilih: ")
    for node in listNode:
        print('- ',node)
    print()
    
    # Meminta Input Pengguna
    start = input("Masukkan start: ")
    # start = "Jalan A-I"
    # print("Masukkan start: Jalan A-I")
    while not g.cek_node(start, listNode):
        print("Node Tidak ditemukan, silakan input ulang")
        start = input("Masukkan start: ")

    tujuan = input("Masukkan tujuan: ")
    # tujuan = "Jalan G-IV"
    # print("Masukkan tujuan: Jalan G-IV")
    while not g.cek_node(tujuan, listNode):
        print("Node Tidak ditemukan, silakan input ulang")
        tujuan = input("Masukkan tujuan: ")

    pilihan = input("Pilih algoritma yang digunakan (A* atau UCS): ")
    if pilihan == "A*":
        listIdxAnswer = algo.aStar(g, g.getIdxNode(start), g.getIdxNode(tujuan))

        listNodeAnswer = g.idxToNodeList(listIdxAnswer)
        print()
        print("Rute Terpendeknya adalah: ")
        it = 0
        for node in listNodeAnswer:
            if it == 0:
                print(node, end='')
            elif it == numNode:
                print(" -->",node)
            else:
                print(" -->",node,end='')
            it+=1

        for i in range(len(listIdxAnswer)-1):
            dist = jarak.euclideanDistance(listKoordinat[listIdxAnswer[i]], listKoordinat[listIdxAnswer[i+1]])
            
        print()
        print("Jarak terpendek dari " + start + " menuju " + tujuan + " adalah " + str(dist) + " meter.")

        ## Plotter

        latitudeRute = g.idxToKoordinatX(listIdxAnswer)
        longitudeRute = g.idxToKoordinatY(listIdxAnswer)

        petaLatitude = latitude
        petaLongitude = longitude

        gmap = gmplot.GoogleMapPlotter(petaLatitude, petaLongitude, 18)
        for i in range(numNode):
            for j in range(numNode):
                if(adjacencyMatrix[i][j] == 1):
                    latitude = [g.getKoordinatX(i), g.getKoordinatX(j)]
                    longitude = [g.getKoordinatY(i), g.getKoordinatY(j)]
                    gmap.scatter(latitude, longitude, 'blue', size = 4.5, marker=False)
                    gmap.plot(latitude, longitude, 'black', edge_width = 2.5)

        gmap.scatter(latitudeRute, longitudeRute, 'red', size = 4.5, marker=False)
        gmap.plot(latitudeRute, longitudeRute, 'red', edge_width = 2.5)

        gmap.marker(latitudeRute[0], longitudeRute[0], 'red', label='S', title='titik start', info_window="<text>Titik start</text>")
        gmap.marker(latitudeRute[-1], longitudeRute[-1], 'green', label='F', title='titik finish', info_window="<text>Titik finish</text>")

        # Menyimpan peta dalam file HTML
        gmap.draw("output-astar.html")
        print("")
        print("Peta telah disimpan dalam file output-astar.html di folder yang sama dengan program ini.")
    
    elif pilihan == "UCS":
        listIdxAnswer = ucs.ucs(g, g.getIdxNode(start), g.getIdxNode(tujuan))
        listNodeAnswer = g.idxToNodeList(listIdxAnswer)
        print()
        print("Rute Terpendeknya adalah: ")
        it = 0
        for node in listNodeAnswer:
            if it == 0:
                print(node, end='')
            elif it == numNode:
                print(" -->", node)
            else:
                print(" -->", node, end='')
            it += 1

        for i in range(len(listIdxAnswer) - 1):
            dist = jarak.euclideanDistance(listKoordinat[listIdxAnswer[i]], listKoordinat[listIdxAnswer[i + 1]])

        print()
        print("Jarak terpendek dari " + start + " menuju " + tujuan + " adalah " + str(dist) + " meter.")

        ## Plotter

        latitudeRute = g.idxToKoordinatX(listIdxAnswer)
        longitudeRute = g.idxToKoordinatY(listIdxAnswer)

        petaLatitude = latitude
        petaLongitude = longitude

        gmap = gmplot.GoogleMapPlotter(petaLatitude, petaLongitude, 18)
        for i in range(numNode):
            for j in range(numNode):
                if adjacencyMatrix[i][j] == 1:
                    latitude = [g.getKoordinatX(i), g.getKoordinatX(j)]
                    longitude = [g.getKoordinatY(i), g.getKoordinatY(j)]
                    gmap.scatter(latitude, longitude, 'blue', size = 4.5, marker=False)
                    gmap.plot(latitude, longitude, 'black', edge_width = 2.5)

        gmap.scatter(latitudeRute, longitudeRute, 'red', size = 4.5, marker=False)
        gmap.plot(latitudeRute, longitudeRute, 'red', edge_width=2.5)

        gmap.marker(latitudeRute[0], longitudeRute[0], 'red', label='S', title='titik start', info_window="<text>Titik start</text>")
        gmap.marker(latitudeRute[-1], longitudeRute[-1], 'green', label='F', title='titik finish', info_window="<text>Titik finish</text>")

        gmap.draw("output-ucs.html")
        print("")
        print("Peta telah disimpan dalam file output-ucs.html di folder yang sama dengan program ini.")

    else:
        print("Pilihan algoritma tidak valid. Program dihentikan.")
        


if __name__ == "__main__":
    main()

