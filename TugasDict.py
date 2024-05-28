    # Membuat kamus bahasa Indonesia- Belanda
indo_to_netherland = {
    "Burung": "Vogel",
    "Kuda": "Paard",
    "Bebek": "Eend",
    "Singa": "Leeuw",
    "Banteng": "Megachan"
}

# Fungsi untuk menerjemahkan kata
def translate_word(word):
    translation = indo_to_netherland.get(word) 
    if translation:
        return translation
    else:
        print("Kata tidak ditemukan dalam kamus.")
        choice = input("Ketik '1' untuk menambahkan kata ini atau '2' untuk keluar: ").capitalize()
        if choice == '1':
            new_translation = input("Masukkan terjemahan baru: ").capitalize
            indo_to_netherland[word] = new_translation
            return f"Kata '{word}' dengan terjemahan '{new_translation}' telah ditambahkan ke kamus."
        elif choice == '2':
            return "Keluar dari penambahan kata."
        else:
            return "Pilihan tidak valid."
# Fungsi untuk mengupdate kata dalam kamus
def update_word(old_word, new_word, new_translation):
    if old_word in indo_to_netherland:
        del indo_to_netherland[old_word]  # Menghapus kata lama
    indo_to_netherland[new_word] = new_translation  # Menambahkan kata baru
    print(f"Kata '{old_word}' telah diupdate menjadi '{new_translation}' yang merupakan terjemahan dari '{new_word}'.")

# Fungsi untuk menghapus kata dari kamus
def delete_word(word):
    if word in indo_to_netherland:
        del indo_to_netherland[word]
        print(f"Kata '{word}' telah dihapus dari kamus.")
    else:
        print("Kata tidak ditemukan dalam kamus.")

# Fungsi untuk menambahkan kata baru ke dalam kamus
def add_word():
    new_word = input("Masukkan kata baru dalam bahasa Indonesia: ").capitalize()
    new_translation = input("Masukkan terjemahan dalam bahasa Belanda: ").capitalize()
    indo_to_netherland[new_word] = new_translation
    print(f"Kata baru '{new_word}' dengan terjemahan '{new_translation}' telah ditambahkan ke kamus.")

# Program utama
def main():
    while True:
        print("Selamat datang di Kamus Indonesia - Belanda!")
        print("Kata-kata yang tersedia: " + ", ".join(indo_to_netherland.keys()))
        print("Menu:")
        print("1. Terjemahkan kata")
        print("2. Tambah kata baru")
        print("3. Keluar")
        choice = input("Pilih opsi (1, 2, atau 3): ").capitalize()
        
        if choice == "3":
            print("Terima kasih telah menggunakan kamus.")
            break
        elif choice == "2":
            add_word()
            continue
        elif choice == "1":
            while True:
                print("Kata-kata yang tersedia: " + ", ".join(indo_to_netherland.keys()))
                menu = input("Masukkan kata: ").capitalize()
                translation = translate_word(menu)
                print("Terjemahan:", translation)

                if translation != "Kata tidak ditemukan dalam kamus.":
                    print("Opsi:")
                    print("1. Update kata")
                    print("2. Hapus kata")
                    print("Enter untuk melanjutkan")
                    action = input("Pilih opsi (1, 2, atau Enter): ").capitalize()
                    if action == "1":
                        new_translation = input("Masukkan terjemahan baru: ").capitalize()
                        update_word(translate_word(menu), menu, new_translation)
                        break
                    elif action == "2":
                        delete_word(menu)
                        break
                    elif action == "":
                        break
        
# Menjalankan program utama
main()
