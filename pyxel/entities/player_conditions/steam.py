import pyxel
from input_detector import InputDetector as Input

class Steam:
    def __init__(self, game, player):
        self.game = game
        self.player = player

        # effect
        self.smokes = []

    def update_effect(self):
        if pyxel.frame_count % 2 == 0:
            x = pyxel.rndi(int(self.player.x)-2, int(self.player.x)+18)
            y = pyxel.rndi(int(self.player.y), int(self.player.y)+20)
            size = 1
            # step = pyxel.rndf(0.5, 2)
            step = 0.2
            self.smokes.append((x, y, size, step))
        
        for i, (x, y, size, step) in enumerate(self.smokes):
            size += step
            self.smokes[i] = (x, y, size, step)

        self.smokes = [ smoke for smoke in self.smokes if smoke[2] < 5]

    def update(self):
        player = self.player
        # キー入力に応じて左右に移動する
        if Input.btn(Input.LEFT):
            player.dx = max(player.dx - 0.2, -1.5)
            player.direction = -1

        if Input.btn(Input.RIGHT):
            player.dx = min(player.dx + 0.2, +1.5)
            player.direction = 1

        if Input.btn(Input.UP):
            player.dy = max(player.dy - 0.2, -1.5)

        if Input.btn(Input.DOWN):
            player.dy = min(player.dy + 0.2, +1.5)

        if not Input.btn(Input.LEFT) and not Input.btn(Input.RIGHT):
            if player.dx > 0:
                player.dx = max(0, player.dx - 0.05)
            elif player.dx < 0:
                player.dx = min(0, player.dx + 0.05)

        if not Input.btn(Input.UP) and not Input.btn(Input.DOWN):
            if player.dy > 0:
                player.dy = max(0, player.dy - 0.05)
            elif player.dy < 0:
                player.dy = min(0, player.dy + 0.05)

        self.update_effect()

    def draw(self):

        # effect
        for x, y, size, step in self.smokes:
            if 3 < size < 4:
                pyxel.dither(0.5)
                pyxel.circ(x, y, size, 7)
                pyxel.dither(1)
            elif 4 < size:
                pyxel.circb(x, y, size, 7)
            else:
                pyxel.circ(x, y, size, 7)

        w = 16 if self.player.direction > 0 else -16

        u = pyxel.frame_count // 2 % 2 * 16 + 16
        pyxel.blt(self.player.x, self.player.y, 0, u, 32, w, 16, 4)
        # self.effect()
