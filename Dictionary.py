#kamus sederhana 
kamus = {
    'kucing':'cat',
    'anjing':'dog',
    'burung':'bird',
    'kelinci':'rabbit',
    'kuda':'horse',
    'singa':'lion',
    'gajah':'elephant',
    'kura-kura':'turtle',
    'monyet':'monkey',
    'ular':'snake'
}

#Fungsi untuk mencari arti dari sebuah kata
def cari_arti(kata):
    if kata in kamus:
        return kamus[kata]
    else:
        return None
    
#program utama
def main():
    print("selamat datang dikamus sederhana.")

    while True:
        kata = input ("Masukan kata (ketik 'selesai' untuk keluar):")

        if kata.lower() == 'selesai':
            print("Terima kasih telah menggunakan kamus ini")
        break 
    arti = cari_arti(kata.lower())
    if arti:
            print(f"arti dari '{kata}' adalah '{arti}'.")
    else:
        print(f"kata '{kata}' Maaf, Arti tidak ditemukan dalam kamus.")
#memanggil program utama
if __name__ == "__main__":
    main()