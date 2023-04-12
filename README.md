# Tugas Kecil 3 IF2211 Strategi Algoritma
## Implementasi Algoritma UCS dan A* untuk Menentukan Lintasan Terpendek

<p align="center">
    <img src="https://www.balidev.top/wp-content/uploads/2021/05/cara-menghapus-riwayat-lokasi-google-map.jpg" height="250" width="auto">
</p>

## Table of Contents

- [Brief Explanation](#brief-explanation)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Author](#author)

## Brief Explanation
Pada tugas kecil 3 ini, program menentukan lintasan terpendek berdasarkan peta Google Map jalan-jalan di kota Bandung. Dari ruas-ruas jalan di peta dibentuk graf. Simpul menyatakan persilangan jalan (simpang 3, 4 atau 5) atau ujung jalan. Asumsikan jalan dapat dilalui dari dua arah. Bobot graf menyatakan jarak (m atau km) antar simpul. Jarak antar dua simpul dapat dihitung dari koordinat kedua simpul menggunakan rumus jarak Euclidean (berdasarkan koordinat) atau dapat menggunakan ruler di Google Map, atau cara lainnya yang disediakan oleh Google Map.

## Requirements
- [python3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- Python library [networkx](https://pypi.org/project/networkx/)
- Python library [gmplot](https://pypi.org/project/gmplot/)

## How to Run
1. Jalankan terminal

2. Clone Repository dengan menjalankan perintah:
```
git clone https://github.com/raihaniqbal24/Tucil3_13518134_13521068.git
cd Tucil3_13518134_13521068
```

3. Jalankan perintah `cd src` untuk masuk ke dalam folder src tempat program berada

4. Jalankan program dengan cara memasukkan perintah `python Main.py`

5. Masukkan file peta, titik mulai, titik akhir, dan algoritma yang ingin digunakan

6. Program akan menampilkan hasil rute, jarak, dan menghasilkan file keluaran peta yang dapat dibuka dengan browser 

## Author
- 13518134 Muhammad Raihan Iqbal
- 13521068 Ilham Akbar