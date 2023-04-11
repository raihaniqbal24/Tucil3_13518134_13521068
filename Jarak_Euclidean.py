import math

def euclideanDistance(x, y):
    lat1, lon1 = x
    lat2, lon2 = y

    # Menghitung perbedaan latitude dan longitude
    selisih_latitude = lat2 - lat1
    selisih_longitude = lon2 - lon1

    # Menghitung perbedaan kuadrat latitude dan longitude
    selisih_latitude_kuadrat = selisih_latitude ** 2
    selisih_longitude_kuadrat = selisih_longitude ** 2

    # Menghitung jarak Euclidean dalam satuan meter
    jarak = math.sqrt(selisih_latitude_kuadrat + selisih_longitude_kuadrat) * 111322

    return jarak