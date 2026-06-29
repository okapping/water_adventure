import pyxel
from collision import *


# リーフクラス
class Leaf:
    # リーフを初期化する
    def __init__(self, game, scene, x, y):
        self.game = game  # ゲームクラス
        self.scene = scene  # シーンクラス
        self.x = x  # X座標
        self.y = y  # Y座標
        self.dx = 0  # X軸方向の移動距離
        self.dy = 0  # Y軸方向の移動距離
        self.direction = -1  # 左右の移動方向
        # self.is_elite = is_elite  # レッドスライムかどうか
        # self.is_waiting = True  # 待ち伏せ中かどうか
        self.alive_count = 0

    # スライムを更新する
    def update(self):
        # 生存時間
        self.alive_count += 1

        if self.alive_count // 15 % 2 == 0:
            self.dx = 0
            return
        if (
            abs(self.scene.player.x - self.x) >= 64
            or abs(self.scene.player.y - self.y) >= 32
        ):  # プレイヤーと一定距離離れている時
            self.dx = 0
            return

        #     # プレイヤーと接近した時
            # self.is_waiting = False
            # return

        self.direction = 1 if self.scene.player.x > self.x else -1
        # # 移動距離を決める
        self.dx = self.direction
        # self.dy = min(self.dy + 1, 3)

        # # 押し戻し処理
        self.x, self.y = push_back(self.x, self.y, self.dx, self.dy)


    # スライムを描画する
    def draw(self):
        # 画像の参照X座標を決める
        # u = pyxel.frame_count // 4 % 2 * 8 + 8  # イメージバンクの参照X座標
        # 4フレーム周期で0と8を繰り返す

        w = 16 if self.direction > 0 else -16
        u = 0 if self.dx == 0 else 16 
        pyxel.blt(self.x, self.y, 0, u, 112, w, 16, 8)
        
        # DEBUG
        pyxel.text(self.x, self.y-20, f"alive_cnt: {self.alive_count}",0)
        pyxel.text(self.x, self.y-10, f"dx: {self.dx}, dy: {self.dy}",0)

        # # 画像を描画する
        # if self.is_elite:  # レッドスライム
        #     pyxel.blt(self.x, self.y, 0, u, 80, 8, 8, 15)
        # else:  # グリーンスライム
        #     pyxel.blt(self.x, self.y, 0, u, 72, 8, 8, 15)
