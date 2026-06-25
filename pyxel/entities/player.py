import pyxel
from input_detector import InputDetector as Input
from .player_conditions import Ice, Steam, Water
from collision import *

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
        self.jump_counter = 0  # ジャンプ時間

        self.conditions = [
            Water(self.game, self), Ice(self.game, self), Steam(self.game, self)
        ]
        self.active_cond = 0 # 0=水, 1=氷, 2=水, 3=水蒸気

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
    def update(self):

        # キャラ入れ替え
        if Input.btnp(Input.Y):
            self.active_cond += 1
        pattern = [0,1,0,2]
        i = pattern[self.active_cond % 4]
        self.conditions[i].update()

        # 行動の反映
        # self.x = max(0, self.x + self.dx)
                # 押し戻し処理
        self.x, self.y = push_back(self.x, self.y, self.dx, self.dy)

        # self.x += self.dx
        # self.y += self.dy
        
        # self.scene.scroll_x = max(0, self.scene.scroll_x + self.dx)
        # self.scene.scroll_y -= self.dy

        # self.dx = 0
        # self.dy = 0
        if pyxel.btn(pyxel.KEY_0):
            self.test += 0.1

    def draw_character(self):
        """キャラクターを描画する
        """

        # キャラクターの向きによって画像の向きを変える
        w = 16 if self.direction > 0 else -16
        if self.condition in [0, 2]:
            # 画像の参照X座標を決める
            i = [0, 1, 2, 1]
            u = pyxel.frame_count // 4 % 4
            u = i[u] * 16
            pyxel.blt(self.x, self.y, 0, u, 16, w, 16, 4)

            self.water_effect()
        elif self.condition == 1:
            pyxel.blt(self.x, self.y, 0, 0, 32, w, 16, 4)
            self.ice_effect()
        elif self.condition == 3:
            u = pyxel.frame_count // 2 % 2 * 16 + 16
            pyxel.blt(self.x, self.y, 0, u, 32, w, 16, 4)
            self.steam_effect()

    def draw(self):
        pass
        # self.draw_character()
        # キャラのindexを計算
        pattern = [0,1,0,2]
        i = pattern[self.active_cond % 4]
        self.conditions[i].draw()
        
        pyxel.text(self.x, self.y-50,f"in_collision: {in_collision(self.x, self.y+16)}",0)
        pyxel.text(self.x, self.y-40,f"is_wall_ahead: {is_wall_ahead(self.x, self.y, self.direction)}",0)
        pyxel.text(self.x, self.y-30,f"is_on_ground: {is_on_ground(self.x, self.y)}",0)
        pyxel.text(self.x, self.y-20,f"dx: {self.dx}, dy: {self.dy}",0)
        pyxel.text(self.x, self.y-10,f"x: {self.x}, y: {self.y}",0)
        pyxel.rectb(self.x, self.y, 16, 16, 10)

        # pyxel.rectb(30, 30, 16, 16, 10)
        # pyxel.pset(30, 30+self.test, 8) 
        # pyxel.text(30, 20, f"test: {self.test}", 1)
