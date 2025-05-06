import pyxel
import time

#初期設定======================================================
pyxel.init(273, 290, title="がうのかくれんぼチャレンジ！！")
#画像挿入======================================================
pyxel.load("my_resource.pyxres")
#変数設定======================================================
game = True

pyxel.mouse(True)
#上バーを設定する===============================================
result_list = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
#関数設定======================================================
def draw_picture(pyxel_X, pyxel_y, pyxel_number_x, pyxel_number_y, pyxel_width, pyxel_high, transpaarent):
    pyxel.blt(pyxel_X, pyxel_y, 0, pyxel_number_x, pyxel_number_y, pyxel_width, pyxel_high, transpaarent)

def draw_line():
    for line_y in range(0, 19):
        pyxel.line(0, 17 * line_y, 273, 17 * line_y, 12)
    for line_x in range(0, 19):
        pyxel.line(17 * line_x, 0,17 * line_x, 290, 12)
    pyxel.rect(0, 0, 273, 17, 6)

def draw_number(number_x, number_y, number):
    pyxel.blt(number_x, number_y, 0, number * 7 + 49, 1, 6, 13, 9)

def draw_block():
    for block_x in range(0, 16):
        for block_y in range(0, 16):
            if blk_list[block_y][block_x] == 0:
                pyxel.blt(block_x * 17 + 1, block_y * 17 + 18, 0, 16, 0, 16, 16)
            if blk_list[block_y][block_x] == 2:
                pyxel.blt(block_x * 17 + 1, block_y * 17 + 18, 0, 128, 0, 16, 16)

def select_gau(gau_number):
    global tora
    for gau in range(0, int(gau_number)):
        tora = True
        while tora == True:
            gau_1 = pyxel.rndi(0, 15)
            gau_2 = pyxel.rndi(0, 15)
            if gau_list[gau_2][gau_1] == 1:
                pass
            elif blk_list[gau_2][gau_1] == 1:
                pass
            else:
                gau_list[gau_2][gau_1] = 1
                gau_list_1[gau_2][gau_1] = 1
                tora = False
    
    for nmb_x in range(0, 16):
        for nmb_y in range(0, 16):
            if gau_list[nmb_y][nmb_x] == 1:
                if nmb_y != 0:
                    if gau_list[nmb_y - 1][nmb_x] == 0:
                        nmb_list[nmb_y - 1][nmb_x] += 1
                
                if nmb_y != 0 and nmb_x != 0:
                    if gau_list[nmb_y - 1][nmb_x - 1] == 0:
                        nmb_list[nmb_y - 1][nmb_x - 1] += 1
                
                if nmb_y != 0 and nmb_x != 15:
                    if gau_list[nmb_y - 1][nmb_x + 1] == 0:
                        nmb_list[nmb_y - 1][nmb_x + 1] += 1
                
                if nmb_x != 0:
                    if gau_list[nmb_y][nmb_x - 1] == 0:
                        nmb_list[nmb_y][nmb_x - 1] += 1
                
                if nmb_x != 15:
                    if gau_list[nmb_y][nmb_x + 1] == 0:
                        nmb_list[nmb_y][nmb_x + 1] += 1
                
                if nmb_y != 15:
                    if gau_list[nmb_y + 1][nmb_x] == 0:
                        nmb_list[nmb_y + 1][nmb_x] += 1
                
                if nmb_y != 15 and nmb_x != 15:
                    if gau_list[nmb_y + 1][nmb_x + 1] == 0:
                        nmb_list[nmb_y + 1][nmb_x + 1] += 1
                
                if nmb_y != 15 and nmb_x != 0:
                    if gau_list[nmb_y + 1][nmb_x - 1] == 0:
                        nmb_list[nmb_y + 1][nmb_x - 1] += 1
    
    for hrt in range(0, 3):
        heart = True
        while heart == True:
            hrt_1 = pyxel.rndi(0, 15)
            hrt_2 = pyxel.rndi(0, 15)
            if hrt_list[hrt_2][hrt_1] == 1:
                pass
            elif gau_list[hrt_2][hrt_1] >= 1:
                pass
            elif blk_list[hrt_2][hrt_1] == 1:
                pass
            elif nmb_list[hrt_2][hrt_1] != 0:
                pass
            else:
                hrt_list[hrt_2][hrt_1] = 1
                hrt_list_1[hrt_2][hrt_1] = 1
                heart = False

def draw_gau():
    for gau_x in range(0, 16):
        for gau_y in range(0, 16):
            if gau_list[gau_y][gau_x] == 1:
                pyxel.blt(gau_x * 17 + 1, gau_y * 17 + 18, 0, 0, 0, 16, 16, 9)
            if hrt_list[gau_y][gau_x] == 1:
                pyxel.blt(gau_x * 17 + 1, gau_y * 17 + 18, 0, 32, 0, 16, 16, 9)

def draw_number():
    for suzi_x in range(0, 16):
        for suzi_y in range(0, 16):
            if nmb_list[suzi_y][suzi_x] > 0 and nmb_list[suzi_y][suzi_x] < 9:
                pyxel.blt(suzi_x * 17 + 1, suzi_y * 17 + 18, 0,(nmb_list[suzi_y][suzi_x] - 1)* 16, 16, 16, 16, 9)

def draw_start(random_L, random_H):
    blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 1
    
    if int(pyxel.mouse_x/17) < 16:
        blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17) + 1] = 1
    
    if int(pyxel.mouse_x/17) < 16 and int(pyxel.mouse_y/17) - 1 < 16:
        blk_list[int(pyxel.mouse_y/17) ][int(pyxel.mouse_x/17) + 1] = 1
    
    if int(pyxel.mouse_x/17) < 16 and int(pyxel.mouse_y/17) - 1 > 0:
        blk_list[int(pyxel.mouse_y/17) - 2][int(pyxel.mouse_x/17) + 1] = 1
    
    if int(pyxel.mouse_x/17) > 0:
        blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17) - 1] = 1
    
    if int(pyxel.mouse_x/17) > 0 and int(pyxel.mouse_y/17) - 1 < 16:
        blk_list[int(pyxel.mouse_y/17)][int(pyxel.mouse_x/17) - 1] = 1
    
    if int(pyxel.mouse_x/17) > 0 and int(pyxel.mouse_y/17) - 1 > 0:
        blk_list[int(pyxel.mouse_y/17) - 2][int(pyxel.mouse_x/17) - 1] = 1
    
    if int(pyxel.mouse_y/17) - 1 < 16:
        blk_list[int(pyxel.mouse_y/17)][int(pyxel.mouse_x/17)] = 1
    
    if int(pyxel.mouse_y/17) - 1 > 0:
        blk_list[int(pyxel.mouse_y/17) - 2][int(pyxel.mouse_x/17)] = 1
    
    for block in range(0, pyxel.rndi(int(random_L), int(random_H))):
        blk_list[pyxel.rndi(0, 15)][pyxel.rndi(0, 15)] = 1

def draw_result(gau_number, my_life, gau_number_1):
    draw_picture(33, 1, 32, 0, 16, 16, 9)
    draw_picture(129, 1, 0, 0, 16, 16, 9)
    
    if my_life == 100:
        result_list[3] = 1
        result_list[4] = 0
        result_list[5] = 0
        for life in range(3, 6):
            draw_picture(16 * life + 1, 1, result_list[life] * 16, 32, 16, 16, 9)
    else:
        result_list[3] = 0
        if my_life >= 10:
            result_list[4] = (my_life) // 10
        else:
            result_list[4] = 0
        result_list[5] = (my_life) % 10
        for life in range(3, 6):
            draw_picture(16 * life + 1, 1, result_list[life] * 16, 32, 16, 16, 9)
    
    result_list[9] = gau_number // 10
    result_list[10] = gau_number % 10
    result_list[11] = 10
    result_list[12] = gau_number_1 // 10
    result_list[13] = gau_number_1 % 10
    
    for gau_number_2 in range(9, 14):
        draw_picture(16 * gau_number_2 + 1, 1, result_list[gau_number_2] * 16, 32, 16, 16, 9)

def draw_set():
    global my_life
    global gau_number
    for set_y in range(4, 6):
        for set_x in range(6, 7):
            if my_life == 100:
                set_list[set_y][set_x] = 2
            else:
                set_list[set_y][set_x] = 1
        for set_x in range(8, 10):
            if my_life == 100:
                set_list[set_y][set_x] = 1
            else:
                set_list[set_y][set_x] = my_life // 10 + 1
        for set_x in range(10, 12):
            if my_life == 100:
                set_list[set_y][set_x] = 1
            else:
                set_list[set_y][set_x] = my_life % 10 + 1
        for set_x_1 in range(3, 6):
            if (set_list[4][set_x_1 * 2] - 1) <= 7:
                draw_picture(34 * set_x_1, 68, (set_list[4][set_x_1 * 2] - 1) * 32, 48, 32, 32, 9)
            elif (set_list[4][set_x_1 * 2] - 1) > 7:
                draw_picture(34 * set_x_1, 68, (set_list[4][set_x_1 * 2] - 9) * 32, 80, 32, 32, 9)
        draw_picture(17 * 2 + 2, 68, 64, 80, 32, 32, 9)
        draw_picture(17 * 12 + 2, 68, 96, 80, 32, 32, 9)
        draw_picture(17 * 4 + 2, 68, 128, 80, 32, 32, 9)
    for set_y in range(8, 10):
        for set_x in range(6, 7):
            if gau_number == 100:
                set_list[set_y][set_x] = 2
            else:
                set_list[set_y][set_x] = 1
        for set_x in range(8, 10):
            if gau_number == 100:
                set_list[set_y][set_x] = 1
            else:
                set_list[set_y][set_x] = gau_number // 10 + 1
        for set_x in range(10, 12):
            if gau_number == 100:
                set_list[set_y][set_x] = 1
            else:
                set_list[set_y][set_x] = gau_number % 10 + 1
        for set_x_1 in range(3, 6):
            if (set_list[8][set_x_1 * 2] - 1) <= 7:
                draw_picture(34 * set_x_1, 136, (set_list[8][set_x_1 * 2] - 1) * 32, 48, 32, 32, 9)
            elif (set_list[8][set_x_1 * 2] - 1) > 7:
                draw_picture(34 * set_x_1, 136, (set_list[8][set_x_1 * 2] - 9) * 32, 80, 32, 32, 9)
        draw_picture(17 * 2 + 2, 136, 64, 80, 32, 32, 9)
        draw_picture(17 * 12 + 2, 136, 96, 80, 32, 32, 9)
        draw_picture(17 * 4 + 2, 136, 160, 80, 32, 32, 9)
    pyxel.rect(17 * 3, 204, 164, 32, 11)
    draw_picture(17 * 3, 204, 192, 80, 32, 32, 9)
    draw_picture(17 * 5, 204, 224, 80, 32, 32, 9)
    draw_picture(17 * 7, 204, 0, 112, 32, 32, 9)
    draw_picture(17 * 9, 204, 32, 112, 32, 32, 9)
    draw_picture(17 * 11, 204, 224, 80, 32, 32, 9)
    pyxel.rectb(17 * 3, 204, 169, 32, 0)

def draw_restart():
    pyxel.rect(17 * 2, 204, 170, 32, 11)
    draw_picture(17 * 2, 204, 32, 112, 64, 32, 9)
    draw_picture(17 * 4, 204, 192, 80, 32, 32, 9)
    draw_picture(17 * 6, 204, 224, 80, 32, 32, 9)
    draw_picture(17 * 8, 204, 0, 112, 32, 32, 9)
    draw_picture(17 * 10, 204, 32, 112, 32, 32, 9)
    draw_picture(17 * 12, 204, 224, 80, 32, 32, 9)
    pyxel.rectb(17 * 2, 204, 203, 32, 0)

def draw_clear():
    pyxel.rect(8, 68, 256, 32, 8)
    pyxel.rectb(8, 68, 256, 32, 0)
    draw_picture(8, 68, 0, 144, 256, 32, 11)
    draw_restart()

def draw_over():
    pyxel.rect(8, 68, 256, 32, 5)
    pyxel.rectb(8, 68, 256, 32, 0)
    draw_picture(8, 68, 0, 176, 256, 32, 11)
    draw_restart()

#=============================================================
while game == True:
    set = True
    start = False
    run = False
    game_clear = False
    game_over = False
    random_L = 20
    random_H = 50
    gau_number = 40
    my_life = 100
    
#初期設定画面==================================================
    set_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#トラちゃんがいる場所===========================================
    gau_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#トラちゃんを押したかの判定======================================
    gau_list_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#ハートがある場所===========================================
    hrt_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#ハートの判定======================================
    hrt_list_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#ブロックを配置する=============================================
    blk_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
#数字を配置する=================================================
    nmb_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
    
    while set == True:
        pyxel.cls(13)
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if pyxel.mouse_x >= 34 and pyxel.mouse_x <= 68 and pyxel.mouse_y >= 68 and pyxel.mouse_y <= 102 and my_life > 0 and my_life > gau_number:
                my_life -= 1
            if pyxel.mouse_x >= 204 and pyxel.mouse_x <= 238 and pyxel.mouse_y >= 68 and pyxel.mouse_y <= 102 and my_life < 100:
                my_life += 1
            if pyxel.mouse_x >= 34 and pyxel.mouse_x <= 68 and pyxel.mouse_y >= 136 and pyxel.mouse_y <= 170 and my_life > 0:
                gau_number -= 1
            if pyxel.mouse_x >= 204 and pyxel.mouse_x <= 238 and pyxel.mouse_y >= 136 and pyxel.mouse_y <= 170 and 99 > gau_number:
                gau_number += 1
            if pyxel.mouse_x >= 54 and pyxel.mouse_x <= 54 + 169 and pyxel.mouse_y >= 204 and pyxel.mouse_y <= 204 + 32:
                start = True
                set = False
        
        gau_number_1 = gau_number
        
        draw_set()
        
        pyxel.flip()
    
    while start == True:
        pyxel.cls(1)
        draw_line()
        draw_block()
        draw_result(gau_number, my_life, gau_number_1)
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pyxel.mouse_x >= 0 and pyxel.mouse_x <= 273 and pyxel.mouse_y >= 17 and pyxel.mouse_y < 290:
            draw_start(random_L, random_H)
            select_gau(gau_number)
            
            start = False
            run = True
        
        pyxel.flip()
    
    while run == True:
        pyxel.cls(1)
        
        draw_gau()
        draw_number()
        draw_line()
        draw_result(gau_number, my_life, gau_number_1)
        
        if my_life == 0 or my_life < gau_number:
            pyxel.mouse(False)
            pyxel.flip()
            time.sleep(2)
            if gau_number == 0:
                game_clear = True
            else:
                game_over = True
            run = False
            break
        elif gau_number == 0:
            pyxel.mouse(False)
            pyxel.flip()
            time.sleep(2)
            game_clear = True
            run = False
            break
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pyxel.mouse_x >= 0 and pyxel.mouse_x <= 273 and pyxel.mouse_y >= 17 and pyxel.mouse_y < 290 and my_life > 0:
            if blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 0:
                my_life -= 1
                blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 1
            elif blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 0:
                blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 0
        
            if gau_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 1:
                if gau_list_1[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 1:
                    gau_number -= 1
                    gau_list_1[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 0
        
            if blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 2:
                blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 0
        
            if hrt_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 1:
                if hrt_list_1[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 1:
                    if my_life != 100:
                        if my_life == 99:
                            my_life += 1
                        elif my_life == 98:
                            my_life += 2
                        elif my_life <= 97:
                            my_life += 3
                        hrt_list_1[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 0
        
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT) and pyxel.mouse_x >= 0 and pyxel.mouse_x <= 273 and pyxel.mouse_y >= 17 and pyxel.mouse_y < 290:
            if blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 0:
                blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 2
            elif blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] == 2:
                blk_list[int(pyxel.mouse_y/17) - 1][int(pyxel.mouse_x/17)] = 0
        
        draw_block()
        
        pyxel.flip()
    
    pyxel.mouse(True)
    
    while game_clear == True:
        pyxel.cls(13)
        draw_clear()
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pyxel.mouse_x >= 17 * 2 and pyxel.mouse_x <= 17 * 2 + 170 and pyxel.mouse_y >= 204 and pyxel.mouse_y < 204 + 32:
            set = True
            game_clear = False
        
        pyxel.flip()
    
    while game_over == True:
        pyxel.cls(13)
        draw_over()
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pyxel.mouse_x >= 17 * 2 and pyxel.mouse_x <= 17 * 2 + 170 and pyxel.mouse_y >= 204 and pyxel.mouse_y < 204 + 32:
            set = True
            game_over = False
        
        pyxel.flip()

pyxel.quit()