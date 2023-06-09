import re

# membaca input dari file
def baca_file():
    # Membaca nama file dari user
    namaFile = input("Silakan masukkan nama file yang dipilih (beserta extensi): ")
    print("")
    # Membaca isi file
    try:
        with open(namaFile, 'r') as file:
            # Membaca seluruh isi file
            file_contents = file.read()
            
            # Mengekstrak nilai variabel dari isi file menggunakan ekspresi reguler
            banyakNode = int(re.search(r'jumalahNode\s*=\s*(\d+)', file_contents).group(1))
            latitude = float(re.search(r'latitude\s*=\s*([\d.-]+)', file_contents).group(1))
            longitude = float(re.search(r'longitude\s*=\s*([\d.-]+)', file_contents).group(1))
            listKoordinat = eval(re.search(r'listKoordinat\s*=\s*(\[.*?\])', file_contents, re.DOTALL).group(1))
            listNode = eval(re.search(r'listNode\s*=\s*(\[.*?\])', file_contents, re.DOTALL).group(1))
            adjacencyMatrix = eval(re.search(r'matrix\s*=\s*(\[.*?\])', file_contents, re.DOTALL).group(1))
            
            # Mengembalikan nilai variabel dalam bentuk tuple
        return banyakNode, latitude, longitude, listKoordinat, listNode, adjacencyMatrix
    
    # Jika file tidak ditemukan, maka akan memanggil fungsi baca_file() kembali
    except:
        print("File tidak ditemukan, silakan coba lagi")
        baca_file()