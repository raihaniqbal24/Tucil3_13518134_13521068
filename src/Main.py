import graph as g
import Jarak_Euclidean as jarak
import gmplot
import baca_file as baca
import UCS as ucs

def main():
    # Menampilkan judul program
    print("Program Jarak Terpendek dengan A* dan UCS")
    print("-----------------------------------------")
    # Memanggil fungsi baca_file() untuk membaca input dari file
    numNode, latitude, longitude, listKoordinat, listNode, adjacencyMatrix = baca.baca_file()
    
    # Menampilkan nilai variabel yang telah dibaca dari file
    print("Banyak Node :", numNode)
    print("")
    print("Latitude :", latitude)
    print("")
    print("Longitude :", longitude)
    print("")
    print("Koordinat :")
    for koordinat in listKoordinat:
        print(koordinat)
    print("")
    print("Adjacency Matrix:")
    for row in adjacencyMatrix:
        print(row)
    print("")
    print("Nama Jalan : ")
    for node in listNode:
        print('>',node)
    print("")
    
    # Inisiasi graf
    graf = g.Graph(numNode, listNode, listKoordinat, adjacencyMatrix)
    
    # Meminta Input Pengguna
    start = input("Masukkan Start (Nama Jalan) : ")
    while not graf.cek_node(start, listNode):
        print("Node Tidak ditemukan, silakan input ulang")
        start = input("Masukkan Start (Nama Jalan) : ")
    tujuan = input("Masukkan Tujuan (nama jalan) : ")
    while not graf.cek_node(tujuan, listNode):
        print("Node Tidak ditemukan, silakan input ulang")
        tujuan = input("Masukkan Tujuan (nama jalan) : ")
    
    # Memilih algoritma yang digunakan
    print("1. A*")
    print("2. UCS")
    pilihan = input("Pilih algoritma yang digunakan (1 atau 2) : ")
    
    if pilihan == "1":
        # Menjalankan A*
        list_arah = graf.a_star(graf.getIdxNode(start), graf.getIdxNode(tujuan))
        # Menghitung bobot
        bobot = 0
        for i in range(len(list_arah)-1):
            bobot += jarak.euclidean(listKoordinat[list_arah[i]], listKoordinat[list_arah[i+1]])
        
        # inisiasi node yang dikunjungi
        node_dikunjungi = graf.idxToNode(list_arah)
        node_dikunjungi_reversed = node_dikunjungi[::-1]
        print()
        print("Rute Terpendeknya adalah : ")
        # Menampilkan rute terpendek
        kunjungan = 0
        for node in node_dikunjungi_reversed:
            if kunjungan == 0:
                print(node, end='')
            elif kunjungan == numNode:
                print(" -> ",node)
            else:
                print(" -> ",node,end='')
            kunjungan += 1
            
        print()
        print("Jarak terpendek dari " + start + " menuju " + tujuan + " adalah " + str(bobot) + " meter.")
        print()
        ## Plotter

        rute_latitude = graf.idxToKoordinatX(list_arah)
        rute_longitude = graf.idxToKoordinatY(list_arah)

        map_latitude = latitude
        map_longitude = longitude

        gmap = gmplot.GoogleMapPlotter(map_latitude, map_longitude, 18)
        for i in range(numNode):
            for j in range(numNode):
                if(adjacencyMatrix[i][j] == 1):
                    latitude = [graf.getKoordinatX(i), graf.getKoordinatX(j)]
                    longitude = [graf.getKoordinatY(i), graf.getKoordinatY(j)]
                    gmap.scatter(latitude, longitude, 'blue', size = 4.5, marker=False)
                    gmap.plot(latitude, longitude, 'black', edge_width = 2.5)

        gmap.scatter(rute_latitude, rute_longitude, 'red', size = 4.5, marker=False)
        gmap.plot(rute_latitude, rute_longitude, 'red', edge_width = 2.5)

        gmap.marker(rute_latitude[0], rute_longitude[0], 'red', label='S', title='titik start', info_window="<text>Titik start</text>")
        gmap.marker(rute_latitude[-1], rute_longitude[-1], 'green', label='F', title='titik finish', info_window="<text>Titik finish</text>")

        # Menyimpan peta dalam file HTML
        gmap.draw("output-astar.html")
        print("")
        print("Peta telah disimpan dalam file output-astar.html di folder yang sama dengan program ini.")
    
    elif pilihan == "2":
        list_arah = ucs.ucs(graf, graf.getIdxNode(start), graf.getIdxNode(tujuan))
        # Menghitung bobot
        bobot = 0
        for i in range(len(list_arah)-1):
            bobot += jarak.euclidean(listKoordinat[list_arah[i]], listKoordinat[list_arah[i+1]])
        
        # inisiasi node yang dikunjungi
        node_dikunjungi = graf.idxToNode(list_arah)
        node_dikunjungi_reversed = node_dikunjungi[::-1]
        print()
        print("Rute Terpendeknya adalah : ")
        # Menampilkan rute terpendek
        kunjungan = 0
        for node in node_dikunjungi_reversed:
            if kunjungan == 0:
                print(node, end='')
            elif kunjungan == numNode:
                print(" -> ",node)
            else:
                print(" -> ",node,end='')
            kunjungan += 1
            
        print()
        print("Jarak terpendek dari " + start + " menuju " + tujuan + " adalah " + str(bobot) + " meter.")
        print()
        ## Plotter

        rute_latitude = graf.idxToKoordinatX(list_arah)
        rute_longitude = graf.idxToKoordinatY(list_arah)

        map_latitude = latitude
        map_longitude = longitude

        gmap = gmplot.GoogleMapPlotter(map_latitude, map_longitude, 18)
        for i in range(numNode):
            for j in range(numNode):
                if(adjacencyMatrix[i][j] == 1):
                    latitude = [graf.getKoordinatX(i), graf.getKoordinatX(j)]
                    longitude = [graf.getKoordinatY(i), graf.getKoordinatY(j)]
                    gmap.scatter(latitude, longitude, 'blue', size = 4.5, marker=False)
                    gmap.plot(latitude, longitude, 'black', edge_width = 2.5)

        gmap.scatter(rute_latitude, rute_longitude, 'red', size = 4.5, marker=False)
        gmap.plot(rute_latitude, rute_longitude, 'red', edge_width = 2.5)

        gmap.marker(rute_latitude[0], rute_longitude[0], 'red', label='S', title='titik start', info_window="<text>Titik start</text>")
        gmap.marker(rute_latitude[-1], rute_longitude[-1], 'green', label='F', title='titik finish', info_window="<text>Titik finish</text>")

        gmap.draw("output-ucs.html")
        print("")
        print("Peta telah disimpan dalam file output-ucs.html di folder yang sama dengan program ini.")

    else:
        print("Pilihan algoritma tidak valid. Program dihentikan.")
        


if __name__ == "__main__":
    main()

