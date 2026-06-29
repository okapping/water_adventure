import pyxel
from input_detector import InputDetector as Input
from collision import *

class Water:
    def __init__(self, game, player):
        self.game = game
        self.player = player

        self.jumping = False

        # self.starting = 0

    def start(self):
        pass
        # self.starting = pyxel.frame_count+15

    def update(self):
        player = self.player

        if Input.btn(Input.LEFT):
            player.dx = max(player.dx - 1.5, -3)
            player.direction = -1

        if Input.btn(Input.RIGHT):
            player.dx = min(player.dx + 1.5, 3)
            player.direction = 1
        
        if not Input.btn(Input.LEFT) and not Input.btn(Input.RIGHT):
            if player.dx > 0:
                player.dx = max(0, player.dx - 0.5)
            elif player.dx < 0:
                player.dx = min(0, player.dx + 0.5)

        # is_character_colliding
        # if Input.btnp(Input.A) and (in_collision(player.x, player.y + 17) or in_collision(player.x + 15, player.y + 17)):
        if Input.btnp(Input.A) and is_on_ground(player.x, player.y):
            self.jumping = True
            player.dy = -8
         
        if self.jumping:
            player.dy += 1
            if player.dy == 0:
                self.jumping = False
        else:
            # 落下判定
            # if self.player.is_on_ground():
            #     player.dy = 0
            # else:
            #     player.dy = min(player.dy+1, 6)
            player.dy = min(player.dy+1, 6)

        # push_back(player.x, player.y)


    def draw(self):

        if not is_on_ground(self.player.x, self.player.y):
            # 空中にいる場合
            w = 16 if self.player.direction > 0 else -16
            pyxel.blt(self.player.x, self.player.y, 0, 96, 16, w, 16, 4)
        else:
            if abs(self.player.dx) >= 1:
                # 走っている場合
                w = 18 if self.player.direction > 0 else -18
                x = self.player.x if self.player.direction > 0 else self.player.x-2
                u = pyxel.frame_count // 3 % 2
                u = 48 + (24 * u)
                # 48, 72
                pyxel.blt(x, self.player.y, 0, u, 16, w, 16, 4)
            else:
                # 止まっている場合
                w = 16 if self.player.direction > 0 else -16
                # 画像の参照X座標を決める
                i = [0, 1, 2, 1]
                u = pyxel.frame_count // 4 % 4
                u = i[u] * 16
                pyxel.blt(self.player.x, self.player.y, 0, u, 16, w, 16, 4)
            