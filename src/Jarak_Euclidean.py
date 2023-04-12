import math

def euclidean(x,y):
    
    # latitude dan longtitude
    latitude_x = x[0]
    longitude_x = x[1]
    latitude_y = y[0]
    longitude_y = y[1]
 
     # convert ke radian
    x_rad = latitude_x * math.pi / 180.0
    y_rad = latitude_y * math.pi / 180.0 
    
    # selisih
    selisih_latitude = (latitude_y - latitude_x) * math.pi / 180.0     # 1 derajat = 1/180 * pi rad
    selisih_longitude = (longitude_y - longitude_x) * math.pi / 180.0
    
    # akar
    a = (pow(math.sin(selisih_latitude / 2), 2) + pow(math.sin(selisih_longitude / 2), 2) * math.cos(x_rad) * math.cos(y_rad))
    
    # jari jari bumi
    r = 6371
    
    # rumus untuk mendapatkan distance dalam meter
    hasil = 2*r*math.asin(math.sqrt(a))*1000
    
    return hasil