# Membuat kamus bahasa Indonesia- Rusia
indo_to_russia = {
    "kucing": "Кошка",
    "anjing": "Собака",
    "hamster": "Хомяк",
    "penyu": "Черепаха",
    "siput": "Улитка"
}

# Fungsi untuk menerjemahkan kata
def translate_word(word):
    translation = indo_to_russia.get(word)
    if translation:
        return translation
    else:
        return "Kata tidak ditemukan dalam kamus."

# Fungsi untuk mengupdate kata dalam kamus
def update_word(old_word, new_word, new_translation):
    if old_word in indo_to_russia:
        del indo_to_russia[old_word]  # Menghapus kata lama
    indo_to_russia[new_word] = new_translation  # Menambahkan kata baru
    print(f"Kata '{old_word}' telah diupdate menjadi '{new_word}' dengan terjemahan '{new_translation}'.")

# Fungsi untuk menghapus kata dari kamus
def delete_word(word):
    if word in indo_to_russia:
        del indo_to_russia[word]
        print(f"Kata '{word}' telah dihapus dari kamus.")
    else:
        print("Kata tidak ditemukan dalam kamus.")

# Program utama
def main():
    print("Selamat datang di Kamus Indonesia - Rusia!")
    print("Kata-kata yang tersedia: kucing, anjing, hamster, penyu, siput")
    
    while True:
        menu = input("Masukkan kata (atau ketik 'selesai' untuk keluar): ").lower()
        
        if menu == "selesai":
            print("Terima kasih telah menggunakan kamus.")
            break
        
        translation = translate_word(menu)
        print("Terjemahan:", translation)

        if translation != "Kata tidak ditemukan dalam kamus.":
            action = input("Ketik 'update' untuk mengupdate, 'delete' untuk menghapus, atau tekan Enter untuk melanjutkan: ").lower()
            if action == "update":
                new_word = input("Masukkan kata baru: ").lower()
                new_translation = input("Masukkan terjemahan baru: ")
                update_word(menu, new_word, new_translation)
            elif action == "delete":
                delete_word(menu)

# Menjalankan program utama
main()
