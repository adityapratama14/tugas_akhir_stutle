# Program Perpustakaan
buku = ["Harry Potter", "Sword Art Online", "Band of Brothers", "Tower of God", "One Piece"] # lists data buku

def tampil_buku(): # fungsi untuk menampilkan  data buku
    if len(buku) <= 0:
        print("DATA BELUM TERSEDIA")
    else:
        for indeks in range(len(buku)):
            print("[{}]] {}".format(indeks, buku[indeks]))

def tambah_buku(): # fungsi untuk menambah data buku
    buku_baru = input("Tambahkan Judul Buku: ")
    buku.append(buku_baru)

def update_buku(): # fungsi untuk mengupdate data buku
    tampil_buku()
    indeks = int(input("Inputkan ID Buku: "))
    if indeks > len(buku) - 1:
        print("ID Buku Tidak Ditemukan")
    else:
        judul_baru = input("Judul Baru: ")
        buku[indeks] = judul_baru
        
    
def hapus_buku(): # fungsi untuk menghapus data buku
    tampil_buku()
    indeks = int(input("Inputkan ID Buku: "))
    if indeks > len(buku) - 1:
        print("ID Buku Tidak Ditemukan")
    else:
        buku.remove(buku[indeks])

keluar = 'y'

while(keluar != 't' or keluar != 'T'): #fungsi untuk mengulangi program
    if (keluar == 't' or keluar == 'T'):
         break
    
    print("Selamat Datang di Perpustakaan Stutle")  # menampilkan menu
    print("===============") 
    print("[1] Lihat Daftar Buku")
    print("[2] Tambah Stock Buku")
    print("[3] Update Stock Buku")
    print("[4] Delete Data Buku")
    print("===============")

    menu = int(input("Silahkan Pilih Menu :  ")) # mengambil inputan dari user

    if int(menu) == 1:
        tampil_buku()
    elif int(menu) == 2:
        tambah_buku()
    elif int(menu) == 3:
        update_buku()
    elif int(menu) == 4:
        hapus_buku()
    else:
        print("Pilihan Tidak Tersedia!!")

    keluar = input("Apakah anda ingin melanjutkan? (y/t) : ") # mengulangi program
        

    

    

        