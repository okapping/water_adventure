import pyxel
from input_detector import InputDetector as Input
from .player_conditions import Ice, Steam, Water
from collision import *

pattern = [0,1,0,2]

# プレイヤークラス
class Player:
    # プレイヤーを初期化する
    def __init__(self, game, scene, x, y):
        self.game = game  # ゲームクラス
        self.scene = scene  # シーンクラス
        self.x = x  # X座標
        self.y = y  # Y座標
        self.dx = 0  # X軸方向の移動距離
        self.dy = 0  # Y軸方向の移動距離
        self.direction = 1  # 左右の移動方向
        # self.jump_counter = 0  # ジャンプ時間

        self.conditions = [
            Ice(self.game, self),
            Water(self.game, self),
            Steam(self.game, self)
        ]
        # self.active_cond = 0 # 0=水, 1=氷, 2=水, 3=水蒸気
        self.active_cond = 0 # -1=氷, 0=水, 2=水蒸気
        self.changing_smokes = [] # 切り替え時のもくもく
        self.starting = 0 # 切り替え中のフレーム数


        self.test = 0


    # def is_on_ground(self):
    #     for i in range(1, 17):
    #         floor = pyxel.tilemaps[0].pget((self.x+i) // 8, (self.y+17) // 8)
    #         if floor == (0,10):
    #             return True
    #     return False

    # キャラクターが壁と重なっているか判定する
    # def is_character_colliding(x, y):
    #     # キャラクターと重なっているタイル座標の領域を計算する
    #     x1 = pyxel.floor(x) // 8
    #     y1 = pyxel.floor(y) // 8
    #     x2 = (pyxel.ceil(x) + 7) // 8
    #     y2 = (pyxel.ceil(y) + 7) // 8

    #     # タイル座標の領域が壁と重なっているかどうかを判定する
    #     for yi in range(y1, y2 + 1):
    #         for xi in range(x1, x2 + 1):
    #             if pyxel.tilemaps[0].pget(xi * 8 // 8, yi * 8 // 8)
    #             # if in_collision(xi * 8, yi * 8):
    #                 return True  # 壁と衝突している

    #     return False  # 壁と衝突していない

    # def fit_ground(self, x, y, dx, dy):
    #     for i in range(1, 17):
    #         floor = pyxel.tilemaps[0].pget((x+dx+i) // 8, (self.y+17) // 8)
    #         if floor == (0,10):
                

        # return x, y
    def update_effect(self):
        if pyxel.frame_count < self.starting:
            self.changing_smokes.append(
                (
                    pyxel.rndi(-2, 17),# x座標（相対位置）
                    pyxel.rndi(3, 18),# y座標（相対位置）
                    1, # サイズ
                )
            )
        for i, (x, y, size) in enumerate(self.changing_smokes):
            y -= 1
            size += 0.5
            self.changing_smokes[i] = (x, y, size)

        self.changing_smokes = [ smoke for smoke in self.changing_smokes if smoke[2] < 6]

        
    def update(self):

        # キャラ入れ替え
        if Input.btnp(Input.Y) and -1 < self.active_cond:
            self.active_cond -= 1
            self.starting = pyxel.frame_count + 15
            self.conditions[self.active_cond+1].start()
        if Input.btnp(Input.X) and self.active_cond < 1:
            self.active_cond += 1
            self.starting = pyxel.frame_count + 15
            self.conditions[self.active_cond+1].start()
        self.conditions[self.active_cond+1].update()
        # if Input.btnp(Input.Y):
        #     self.active_cond += 1
        # pattern = [0,1,0,2]
        # i = pattern[self.active_cond % 4]
        # self.conditions[i].update()

        # 行動の反映
        # 押し戻し処理
        self.x, self.y = push_back(self.x, self.y, self.dx, self.dy)

        self.update_effect()

        if pyxel.btn(pyxel.KEY_0):
            self.test += 0.1

    # def draw_character(self):
    #     """キャラクターを描画する
    #     """

    #     # キャラクターの向きによって画像の向きを変える
    #     w = 16 if self.direction > 0 else -16
    #     if self.condition in [0, 2]:
    #         # 画像の参照X座標を決める
    #         i = [0, 1, 2, 1]
    #         u = pyxel.frame_count // 4 % 4
    #         u = i[u] * 16
    #         pyxel.blt(self.x, self.y, 0, u, 16, w, 16, 4)

    #         self.water_effect()
    #     elif self.condition == 1:
    #         pyxel.blt(self.x, self.y, 0, 0, 32, w, 16, 4)
    #         self.ice_effect()
    #     elif self.condition == 3:
    #         u = pyxel.frame_count // 2 % 2 * 16 + 16
    #         pyxel.blt(self.x, self.y, 0, u, 32, w, 16, 4)
    #         self.steam_effect()

    def draw(self):
        # キャラのindexを計算
        # pattern = [0,1,0,2]
        # i = pattern[self.active_cond % 4]
        # self.conditions[i].draw()
        self.conditions[self.active_cond+1].draw()
        
        # 能力切り替え時のアニメーション
        for x, y, size in self.changing_smokes:
            pyxel.circ(self.x+x, self.y+y, size, 7)
            # if 3 < size < 4:
            #     pyxel.dither(0.5)
            #     pyxel.circ(x, y, size, 7)
            #     pyxel.dither(1)
            # elif 4 < size:
            #     pyxel.circb(x, y, size, 7)
            # else:
            #     pyxel.circ(x, y, size, 7)

        # if pyxel.frame_count < self.starting:
            # pyxel.rect(self.x, self.y, 16, 16, 7)


        # pyxel.text(self.x, self.y-50,f"in_collision: {in_collision(self.x, self.y+16)}",0)
        pyxel.text(self.x, self.y-50,f"get_tile: {get_tile_type(self.x, self.y)}",0)
        pyxel.text(self.x, self.y-40,f"is_wall_ahead: {is_wall_ahead(self.x, self.y, self.direction)}",0)
        # pyxel.text(self.x, self.y-30,f"is_on_ground: {is_on_ground(self.x, self.y)}",0)
        pyxel.text(self.x, self.y-30,f"enemies cnt: {len(self.scene.enemies)}",0)
        pyxel.text(self.x, self.y-20,f"dx: {self.dx}, dy: {self.dy}",0)
        pyxel.text(self.x, self.y-10,f"x: {self.x}, y: {self.y}",0)
        # pyxel.rectb(self.x, self.y, 16, 16, 10)

        # pyxel.rectb(30, 30, 16, 16, 10)
        # pyxel.pset(30, 30+self.test, 8) 
        # pyxel.text(30, 20, f"test: {self.test}", 1)
