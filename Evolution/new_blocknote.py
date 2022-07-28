import pygame as pg
import numpy as np

def draw_ship(edges=False):
    bstr_dots_int = np.rint(bstr_dots[:, :2]).astype("int32")
    if edges:
        for edge in bstr_edges:
            xy1 = bstr_dots_int[edge[0]]
            xy2 = bstr_dots_int[edge[1]]
            pg.draw.line(screen, color_lns, xy1, xy2, wdt)
    for xy in bstr_dots_int:
        pg.draw.circle(screen, color_dts, xy, rad_dot)


def translocation(dx, dy, dz):
    trans_matrix = np.array([[ 1,  0,  0, 0],
                             [ 0,  1,  0, 0],
                             [ 0,  0,  1, 0],
                             [dx, dy, dz, 1]])
    np.dot(bstr_dots, trans_matrix, bstr_dots)

def rotation_x(a):
    ar = a * 3.1415 / 180
    c = np.cos(ar)
    s = np.sin(ar)
    rotate_matrix = np.array([[1,  0, 0, 0],
                              [0, c, -s, 0],
                              [0, s,  c, 0],
                              [0, 0,  0, 1]])
    np.dot(bstr_dots, rotate_matrix, bstr_dots)

def rotation_y(a):
    global z
    ar = a * 3.1415 / 180
    c = np.cos(ar)
    s = np.sin(ar)
    rotate_matrix = np.array([[ c, 0, s, 0],
                              [ 0, 1, 0, 0],
                              [-s, 0, c, 0],
                              [ 0, 0, 0, 1]])
    np.dot(bstr_dots, rotate_matrix, bstr_dots)

def rotation_z(a):
    ar = a * 3.1415 / 180
    c = np.cos(ar)
    s = np.sin(ar)
    rotate_matrix = np.array([[ c, -s, 0, 0],
                              [ s,  c, 0, 0],
                              [ 0,  0, 1, 0],
                              [ 0,  0, 0, 1]])
    np.dot(bstr_dots, rotate_matrix, bstr_dots)

def scale(sx, sy, sz):
    scale_matrix = np.array([[sx,  0,  0, 0],
                             [ 0, sy,  0, 0],
                             [ 0,  0, sz, 0],
                             [ 0,  0,  0, 1]])
    np.dot(bstr_dots, scale_matrix, bstr_dots)

bstr_dots = np.array([[0, 0, 0], #0
                      [2, 0, 0],
                      [4, 0, 3],
                      [5, 0, 11],
                      [8, 0, 14],
                      [8, 0, 18],
                      [9, 0, 18],
                      [9, 0, 23],
                      [8, 0, 23],
                      [7, 0, 25],
                      [7, 0, 27],#10
                      [6, 0, 28],
                      [-4, 0, 28],
                      [-5, 0, 27],
                      [-5, 0, 25],
                      [-6, 0, 23],
                      [-7, 0, 23],
                      [-7, 0, 18],
                      [-6, 0, 18],
                      [-6, 0, 14],
                      [-3, 0, 11],#20
                      [-2, 0, 3], # korp lvl 1
                      [0, -2, 2],
                      [2, -2, 2],
                      [3, -2, 4],
                      [4, -2, 12],
                      [7, -2, 15],
                      [7, -2, 18],
                      [8, -2, 18],
                      [8, -2, 23],
                      [7, -2, 23],
                      [6, -2, 25],#40
                      [6, -2, 27],
                      [5, -2, 28],
                      [-3, -2, 28],
                      [-4, -2, 27],
                      [-4, -2, 25],
                      [-5, -2, 23],
                      [-6, -2, 23],
                      [-6, -2, 18],
                      [-5, -2, 18],#50
                      [-5, -2, 15],
                      [-2, -2, 12],
                      [-1, -2, 4], # korp lvl 2
                      [0, 1, 2],
                      [2, 1, 2],
                      [3, 1, 11],
                      [8, 1, 16],
                      [8, 1, 23],
                      [5, 1, 27],
                      [3, 1, 28], #60
                      [-1, 1, 28],
                      [-3, 1, 27],
                      [-6, 1, 23],
                      [-6, 1, 16],
                      [-1, 1, 11], # korp lvl 0
                      [10, -2, 15],
                      [12, -2, 15],
                      [12, -2, 25],
                      [10, -2, 25],
                      [11, -2, 18], #70
                      [11, -2, 23], # dvig lvl 2
                      [10, -1, 15],
                      [12, -1, 15],
                      [12, -1, 25],
                      [10, -1, 25],
                      [9, -1, 15],
                      [13, -1, 15],
                      [13, -1, 25],
                      [9, -1, 25], # dvig lvl 1.5
                      [9, 1, 15], #80
                      [13, 1, 15],
                      [13, 1, 25],
                      [9, 1, 25],
                      [10, 1, 15],
                      [12, 1, 15],
                      [12, 1, 25],
                      [10, 1, 25], # dvig lvl 0
                      [10, 2, 15],
                      [12, 2, 15],
                      [12, 2, 25], #90
                      [10, 2, 25], # dvig lvl -1
                      [-8, -2, 15],
                      [-10, -2, 15],
                      [-10, -2, 25],
                      [-8, -2, 25],
                      [-9, -2, 18],
                      [-9, -2, 23], # dvig2 lvl 2
                      [-8, -1, 15],
                      [-10, -1, 15],
                      [-10, -1, 25], #100
                      [-8, -1, 25],
                      [-7, -1, 15],
                      [-11, -1, 15],
                      [-11, -1, 25],
                      [-7, -1, 25], # dvig2 lvl 1.5
                      [-7, 1, 15],
                      [-11, 1, 15],
                      [-11, 1, 25],
                      [-7, 1, 25],
                      [-8, 1, 15],#110
                      [-10, 1, 15],
                      [-10, 1, 25],
                      [-8, 1, 25], # dvig2 lvl 0
                      [-8, 2, 15],
                      [-10, 2, 15],
                      [-10, 2, 25],
                      [-8, 2, 25] # dvig2 lvl -1
                      ])#117 dots!!!

bstr_edges = np.array([[0, 1],
                       [1, 2],
                       [2, 3],
                       [3, 4],
                       [4, 5],
                       [5, 6],
                       [6, 7],
                       [7, 8],
                       [8, 9],
                       [9, 10],
                       [10, 11],
                       [12, 13],
                       [13, 14],
                       [14, 15],
                       [15, 16],
                       [16, 17],
                       [17, 18],
                       [18, 19],
                       [19, 20],
                       [20, 21],
                       [21, 0], # korp lvl 1
                       [5, 8],
                       [15, 18], # korp stz lvl 1
                       [22, 23],
                       [23, 24],
                       [24, 25],
                       [25, 26],
                       [26, 27],
                       [27, 28],
                       [28, 29],
                       [29, 30],
                       [30, 31],
                       [31, 32],
                       [32, 33],
                       [33, 34],
                       [34, 35],
                       [35, 36],
                       [36, 37],
                       [37, 38],
                       [38, 39],
                       [39, 40],
                       [40, 41],
                       [41, 42],
                       [42, 43],
                       [43, 22], # korp lvl 2
                       [0, 22],
                       [23, 1],
                       [24, 2],
                       [25, 3],
                       [26, 4],
                       [27, 5],
                       [27, 30],
                       [30, 8],
                       [31, 9],
                       [32, 10],
                       [33, 11],
                       [34, 12],
                       [35, 13],
                       [36, 14],
                       [37, 15],
                       [37, 40],
                       [40, 18],
                       [41, 19],
                       [42, 20],
                       [43, 21], # korp stz lvl  2
                       [44, 45],
                       [45, 46],
                       [46, 47],
                       [47, 48],
                       [48, 49],
                       [49, 50],
                       [50, 51],
                       [51, 52],
                       [52, 53],
                       [53, 54],
                       [54, 55],
                       [55, 44], # korp lvl 0
                       [44, 0],
                       [44, 21],
                       [45, 1],
                       [45, 2],
                       [46, 3],
                       [47, 4],
                       [47, 5],
                       [48, 8],
                       [49, 9],
                       [49, 10],
                       [49, 11],
                       [50, 11],
                       [51, 12],
                       [52, 12],
                       [52, 13],
                       [52, 14],
                       [53, 15],
                       [54, 18],
                       [54, 19],
                       [55, 20], # korp stz lvl 0
                       [56, 57],
                       [57, 58],
                       [59, 56],
                       [60, 61],
                       [62, 63],
                       [63, 75],
                       [75, 74],
                       [74, 62],
                       [64, 65],
                       [65, 77],
                       [77, 76],
                       [76, 64],
                       [77, 65],
                       [67, 68],
                       [57, 67],
                       [67, 71],
                       [71, 79],
                       [79, 78],
                       [78, 70],
                       [70, 66],
                       [66, 56],
                       [71, 72],
                       [79, 80],
                       [78, 81],
                       [70, 73],
                       [66, 69],
                       [71, 79],
                       [73, 69],
                       [69, 59],
                       [59, 58],
                       [58, 68],
                       [68, 72],
                       [72, 80],
                       [80, 81],
                       [81, 73],
                       [28, 60],
                       [61, 29], # dvig stz
                       [82, 83],
                       [83, 84],
                       [85, 95],
                       [86, 87],
                       [88, 89],
                       [89, 101],
                       [101, 100],
                       [100, 88],
                       [90, 91],
                       [91, 103],
                       [103, 102],
                       [102, 90],
                       [103, 91],
                       [93, 94],
                       [83, 93],
                       [93, 97],
                       [97, 105],
                       [105, 104],
                       [104, 96],
                       [96, 92],
                       [92, 82],
                       [97, 98],
                       [105, 106],
                       [104, 107],
                       [96, 99],
                       [92, 95],
                       [97, 105],
                       [99, 95],
                       [95, 85],
                       [85, 84],
                       [84, 94],
                       [94, 98],
                       [98, 106],
                       [106, 107],
                       [107, 99],
                       [38, 87],
                       [86, 39] # dvig2 stz
                       ]) # 170 elements!!!

bstr_dots = np.hstack((bstr_dots, np.ones((len(bstr_dots), 1))))

ww, wh = 1000, 800
color_bkg = [5, 5, 15]
color_dts = [200, 200, 200]
color_lns = [220, 100, 60]
alpha = 1
sc = 1.01
wdt = 5
rad_dot = 2
edges = False

x, y, z = np.mean(bstr_dots[:, 0]), np.mean(bstr_dots[:, 1]), np.mean(bstr_dots[:, 2])
x0, y0, z0 = ww//2, wh//2, 100
sx, sy, sz = 16, 16, 16

translocation(-x, -y, -z)
scale(sx, sy, sz)
translocation(x0, y0, z0)
x, y, z = x0, y0, z0

pg.init()
screen = pg.display.set_mode((ww, wh))
pg.display.set_caption("FTL_Kestrel")
key_press = []

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_KP8:
                key_press += [event.key]
            elif event.key == pg.K_KP5:
                key_press += [event.key]
            elif event.key == pg.K_KP4:
                key_press += [event.key]
            elif event.key == pg.K_KP6:
                key_press += [event.key]
            elif event.key == pg.K_KP7:
                key_press += [event.key]
            elif event.key == pg.K_KP9:
                key_press += [event.key]
            elif event.key == pg.K_KP_MINUS:
                key_press += [event.key]
            elif event.key == pg.K_KP_PLUS:
                key_press += [event.key]
            elif event.key == pg.K_KP_DIVIDE:
                key_press += [event.key]
        if event.type == pg.KEYUP:
            if event.key in key_press:
                key_press.remove(event.key)
            else: pass
    if pg.K_KP8 in key_press:
        translocation(-x, -y, -z)
        rotation_x(alpha)
        translocation(x, y, z)
    if pg.K_KP5 in key_press:
        translocation(-x, -y, -z)
        rotation_x(-alpha)
        translocation(x, y, z)
    if pg.K_KP4 in key_press:
        translocation(-x, -y, -z)
        rotation_y(alpha)
        translocation(x, y, z)
    if pg.K_KP6 in key_press:
        translocation(-x, -y, -z)
        rotation_y(-alpha)
        translocation(x, y, z)
    if pg.K_KP7 in key_press:
        translocation(-x, -y, -z)
        rotation_z(alpha)
        translocation(x, y, z)
    if pg.K_KP9 in key_press:
        translocation(-x, -y, -z)
        rotation_z(-alpha)
        translocation(x, y, z)
    if pg.K_KP_MINUS in key_press:
        translocation(-x, -y, -z)
        scale(1 / sc, 1 / sc, 1/ sc)
        translocation(x, y, z)
    if pg.K_KP_PLUS in key_press:
        translocation(-x, -y, -z)
        scale(sc, sc, sc)
        translocation(x, y, z)
    if pg.K_KP_DIVIDE in key_press:
        if edges == True:
            edges = False
        elif edges == False:
            edges = True
        key_press.remove(pg.K_KP_DIVIDE)
    screen.fill(color_bkg)
    draw_ship(edges)
    pg.display.flip()
pg.quit()