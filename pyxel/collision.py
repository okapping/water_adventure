# 衝突処理モジュール

import pyxel
from constants import TILE_NONE, TILE_TO_TILETYPE, TILE_WALL


# 指定した座標のタイル種別を取得する
def get_tile_type(x, y):
    tile = pyxel.tilemaps[0].pget(x // 8, y // 8)
    return TILE_TO_TILETYPE.get(tile, TILE_NONE)


# 指定した座標が壁と重なっているか判定する
def in_collision(x, y):
    return get_tile_type(x, y) == TILE_WALL


# キャラクターが壁と重なっているか判定する
def is_character_colliding(x, y):
    # キャラクターと重なっているタイル座標の領域を計算する
    x1 = pyxel.floor(x) // 8
    y1 = pyxel.floor(y) // 8
    x2 = (pyxel.ceil(x) + 15) // 8
    y2 = (pyxel.ceil(y) + 15) // 8

    # タイル座標の領域が壁と重なっているかどうかを判定する
    for yi in range(y1, y2 + 1):
        for xi in range(x1, x2 + 1):
            if in_collision(xi * 8, yi * 8):
                return True  # 壁と衝突している

    return False  # 壁と衝突していない


def push_back_re(x, y, dx, dy):
    """これでもできる
    """
    # たて
    # step = max(-0.1, min(0.1, dy))
    # while is_character_colliding(x, y+dy):
    #     dy -= step
    # else:
    #     y += dy
    #----------------------------------
    if is_character_colliding(x, y+dy):
        bottom = y + dy + 16
        tile_y = (int(bottom) // 8) * 8
        y = tile_y -16
    else:
        y += dy
    # y += dy
    
    

    return x, y


# 押し戻した座標を返す
def push_back(x, y, dx, dy):
    # 壁と衝突するまで垂直方向に移動する
    for _ in range(pyxel.ceil(abs(dy))):
        step = max(-1, min(1, dy))# 1もしくは-1がstepに入るみたい
        if is_character_colliding(x, y + step):
            break
        y += step
        dy -= step
    

    # 壁と衝突するまで水平方向に移動する
    for _ in range(pyxel.ceil(abs(dx))):
        step = max(-1, min(1, dx))
        if is_character_colliding(x + step, y):
            break
        x += step
        dx -= step

    return x, y

# 地面と接しているかを判定する
def is_on_ground(x, y):
    """
    地面と接しているかを判定する。
    接している場合はTrue
    x, y = キャラの座標
    """
    y = pyxel.ceil(y) + 16
    for i in range(16):
        if in_collision(x+i, y):
            return True
    return False
        # def is_on_ground(self):
        # for i in range(1, 17):
        #     floor = pyxel.tilemaps[0].pget((self.x+i) // 8, (self.y+17) // 8)
        #     if floor == (0,10):
        #         return True
        # return False

# 進行方向に壁があるかを判定する
def is_wall_ahead(x, y, dir):
    """
    進行方向に壁があるかを判定する。
    接している場合はTrue
    x, y = キャラの座標
    dir = 向き 右:1, 左-1
    """
    if dir == 1: 
        x = pyxel.ceil(x) + 16
    elif dir == -1:
        x = pyxel.floor(x) - 1
    for i in range(16):
        if in_collision(x, y+i):
            return True
    return False
