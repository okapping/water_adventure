import pyxel
from input_detector import InputDetector as Input
from .player_conditions import Ice, Steam, Water

# プレイヤークラス
class Player:
    # プレイヤーを初期化する
    def __init__(self, game, x, y):
        self.game = game  # ゲームクラス
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

    def is_on_ground(self):
        for i in range(1, 17):
            floor = pyxel.tilemaps[0].pget((self.x+i) // 8, (self.y+17) // 8)
            if floor == (0,10):
                return True
        return False

    def update(self):
        # # キー入力に応じて左右に移動する
        # if Input.btn(Input.LEFT):
        #     self.dx = -2
        #     self.direction = -1

        # if Input.btn(Input.RIGHT):
        #     self.dx = 2
        #     self.direction = 1

        if Input.btnp(Input.Y):
            self.active_cond += 1
            # if self.condition == 3:
            #     self.condition = 0
            # else:
            #     self.condition += 1

        pattern = [0,1,0,2]
        i = pattern[self.active_cond % 4]
        self.conditions[i].update()

        self.x += self.dx
        self.y += self.dy

        # self.dx = 0
        # self.dy = 0


    def water_effect(self):
        pass
    def ice_effect(self):
        pass
    def steam_effect(self):
        pass
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
        