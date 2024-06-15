import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Pengaturan warna
putih = (255, 255, 255)
hitam = (0, 0, 0)
hijau = (0, 255, 0)

# Pengaturan layar
lebar = 800
tinggi = 600
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption('Game Ular Multiplayer')

# Pengaturan font
font = pygame.font.SysFont(None, 35)

# Ukuran blok untuk ular dan makanan
ukuran_blok = 20  # Anda bisa menyesuaikan ukuran ini sesuai kebutuhan

# Inisialisasi clock
clock = pygame.time.Clock()

# Fungsi untuk menampilkan skor
def tampil_skor(skor):
    teks = font.render("Skor: " + str(skor), True, hitam)
    layar.blit(teks, [0, 0])

# Fungsi untuk menggambar ular
def gambar_ular(ukuran_blok, snake_list):
    for x in snake_list:
        pygame.draw.rect(layar, hijau, [x[0], x[1], ukuran_blok, ukuran_blok])

# Fungsi utama game
def game_loop():
    bermain = True
    game_over = False

    x1 = lebar / 2
    y1 = tinggi / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    panjang_ular = 1

    makananx = round(random.randrange(0, lebar - ukuran_blok) / 10.0) * 10.0
    makanany = round(random.randrange(0, tinggi - ukuran_blok) / 10.0) * 10.0

    skor = 0

    while bermain:
        while game_over == True:
            layar.fill(putih)
            pesan = font.render("Game Over! Tekan C-Continue atau Q-Quit", True, hitam)
            layar.blit(pesan, [lebar / 6, tinggi / 3])
            tampil_skor(skor)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        bermain = False
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bermain = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -ukuran_blok
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = ukuran_blok
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -ukuran_blok
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = ukuran_blok
                    x1_change = 0

        if x1 >= lebar or x1 < 0 or y1 >= tinggi or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        layar.fill(putih)
        pygame.draw.rect(layar, hitam, [makananx, makanany, ukuran_blok, ukuran_blok])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > panjang_ular:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        gambar_ular(ukuran_blok, snake_list)
        tampil_skor(panjang_ular - 1)

        pygame.display.update()

        if x1 == makananx and y1 == makanany:
            makananx = round(random.randrange(0, lebar - ukuran_blok) / 10.0) * 10.0
            makanany = round(random.randrange(0, tinggi - ukuran_blok) / 10.0) * 10.0
            panjang_ular += 1
            skor += 10

        clock.tick(15)

    pygame.quit()
    quit()

game_loop()
