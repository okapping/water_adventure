import pyxel
from input_detector import InputDetector as Input
from collision import *

class Ice:
    def __init__(self, game, player):
        self.game = game
        self.player = player

        self.jumping = False
        # self.starting = 0
    
    def start(self):
        pass

    def update(self):
        player = self.player

        # キー入力に応じて左右に移動する
        if Input.btn(Input.LEFT):
            player.dx = max(player.dx - 0.1, -3)
            # player.dx = -2
            player.direction = -1

        if Input.btn(Input.RIGHT):
            player.dx = min(player.dx + 0.1, 3)
            # player.dx = 2
            player.direction = 1

        if not Input.btn(Input.LEFT) and not Input.btn(Input.RIGHT):
            if player.dx > 0:
                player.dx = max(0, player.dx - 0.05)
            elif player.dx < 0:
                player.dx = min(0, player.dx + 0.05)

        if Input.btnp(Input.A) and is_on_ground(player.x, player.y):
            self.jumping = True
            player.dy = -6
        
        # 進行方向に壁がある場合、dxをゼロにする
        if is_wall_ahead(player.x, player.y, player.direction):
            player.dx = 0

        if self.jumping:
            player.dy += 1
            if player.dy == 0:
                self.jumping = False
        else:
            # 落下判定
            player.dy = min(player.dy+2, 6)

    def draw(self):
        w = 16 if self.player.direction > 0 else -16

        pyxel.blt(self.player.x, self.player.y, 0, 0, 32, w, 16, 4)