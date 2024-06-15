import pygame
import time
import random

pygame.init()

# Definisi warna RGB
putih = (255, 255, 255)
hitam = (0, 0, 0)
merah = (213, 50, 80)
hijau = (0, 255, 0)
biru = (50, 153, 213)

# Pengaturan layar
lebar = 800
tinggi = 600

ukuran_blok = 20
kecepatan = 15

# Pengaturan font
font_kecil = pygame.font.SysFont(None, 25)
font_besar = pygame.font.SysFont(None, 50)

# Inisialisasi layar
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption('Game Ular')

# Clock untuk mengatur kecepatan permainan
clock = pygame.time.Clock()

# Fungsi untuk menampilkan pesan di layar
def pesan(teks, warna):
    pesan = font_kecil.render(teks, True, warna)
    layar.blit(pesan, [lebar / 2, tinggi / 2])

# Fungsi untuk menggambar ular
def ular(ukuran_blok, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(layar, hijau, [XnY[0], XnY[1], ukuran_blok, ukuran_blok])

# Fungsi utama permainan
def gameLoop():
    game_over = False
    game_close = False

    kepala_x = lebar / 2
    kepala_y = tinggi / 2

    kepala_x_change = 0
    kepala_y_change = 0

    snakeList = []
    snakeLength = 1

    makanan_x = round(random.randrange(0, lebar - ukuran_blok) / ukuran_blok) * ukuran_blok
    makanan_y = round(random.randrange(0, tinggi - ukuran_blok) / ukuran_blok) * ukuran_blok

    # Peringkat pengguna
    peringkat_pengguna = []

    while not game_over:
        while game_close == True:
            layar.fill(putih)
            pesan("Kamu kalah! Tekan C untuk coba lagi atau Q untuk keluar", merah)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    kepala_x_change = -ukuran_blok
                    kepala_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    kepala_x_change = ukuran_blok
                    kepala_y_change = 0
                elif event.key == pygame.K_UP:
                    kepala_y_change = -ukuran_blok
                    kepala_x_change = 0
                elif event.key == pygame.K_DOWN:
                    kepala_y_change = ukuran_blok
                    kepala_x_change = 0

        # Logika pergerakan ular dan aturan permainan
        if kepala_x >= lebar or kepala_x < 0 or kepala_y >= tinggi or kepala_y < 0:
            game_close = True
        kepala_x += kepala_x_change
        kepala_y += kepala_y_change
        layar.fill(putih)
        pygame.draw.rect(layar, merah, [makanan_x, makanan_y, ukuran_blok, ukuran_blok])
        snakeHead = []
        snakeHead.append(kepala_x)
        snakeHead.append(kepala_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snakeHead:
                game_close = True

        ular(ukuran_blok, snakeList)

        # Tampilkan peringkat pengguna di layar
        tampilkanPeringkat(peringkat_pengguna)

        pygame.display.update()

        if kepala_x == makanan_x and kepala_y == makanan_y:
            makanan_x = round(random.randrange(0, lebar - ukuran_blok) / ukuran_blok) * ukuran_blok
            makanan_y = round(random.randrange(0, tinggi - ukuran_blok) / ukuran_blok) * ukuran_blok
            snakeLength += 1

            # Simpan skor pengguna dan perbarui peringkat pengguna
            peringkat_pengguna.append((f"User{len(peringkat_pengguna)+1}", snakeLength))

            # Urutkan peringkat pengguna berdasarkan skor tertinggi
            peringkat_pengguna.sort(key=lambda x: x[1], reverse=True)

            # Hapus entri terakhir jika peringkat pengguna lebih dari 5
            if len(peringkat_pengguna) > 5:
                peringkat_pengguna = peringkat_pengguna[:5]

        clock.tick(kecepatan)

    pygame.quit()
    quit()

# Fungsi untuk menampilkan peringkat pengguna di layar
def tampilkanPeringkat(peringkat_pengguna):
    peringkat_surface = font_kecil.render("Peringkat Pengguna:", True, hitam)
    layar.blit(peringkat_surface, (10, 10))
    y_pos = 30
    for i, (pengguna, skor) in enumerate(peringkat_pengguna, 1):
        peringkat_surface = font_kecil.render(f"{i}. {pengguna}: {skor}", True, hitam)
        layar.blit(peringkat_surface, (10, y_pos))
        y_pos += 20

# Memulai permainan
gameLoop()