import pyxel
from .scene import Scene
from entities import Player

SCROLL_BORDER_X = 110

class PlayScene:
    def __init__(self, game):
        self.game = game

        self.player = None

        self.scroll_x = 0
        self.scroll_y = 0

        self.cond_index = 64

    # プレイ画面を開始する
    def start(self):
        # 変更前のマップに戻す
        # pyxel.tilemaps[0].blt(0, 0, 2, 0, 0, 256, 16)

        # プレイ画面の状態を初期化する
        game = self.game  # ゲームクラス
        self.player = Player(game, self, 40, 100)  # プレイヤー
        game.scroll_x = 0  # フィールド表示範囲の左端のX座標
        # game.score = 0  # スコア

        # 敵を出現させる
        # self.spawn_enemy(0, 127)

        # BGMを再生する
        # pyxel.stop()
        # pyxel.playm(1, loop=True)

    def update_cond_index(self):
        # 80, 64, 48         -1, 0, 1
        goal_index = 80 - 16 * (self.player.active_cond + 1)
        # goal_index = 16 * (self.player.active_cond + 1)
        # goal_index = 16 * (self.player.active_cond + 1)
        if self.cond_index < goal_index:
            self.cond_index += 2
        elif self.cond_index > goal_index:
            self.cond_index -= 2

    def update(self):
        # プレイヤーを更新する
        if self.player is not None:
            self.player.update()

        # プレイヤーの移動範囲を制限する
        self.player.x = min(max(self.player.x, self.scroll_x), 2040)
        self.player.y = max(self.player.y, 0)

        # プレイヤーがスクロール境界を越えたら画面をスクロールする
        # 左端
        if self.player.x < self.scroll_x+SCROLL_BORDER_X:
            d = self.player.x-(self.scroll_x+SCROLL_BORDER_X)
            self.scroll_x = self.scroll_x+d
        # 右端
        if self.player.x > self.scroll_x+pyxel.width-SCROLL_BORDER_X-16:
            d = self.player.x-(self.scroll_x+pyxel.width-SCROLL_BORDER_X-16)
            self.scroll_x = self.scroll_x+d

        # ステージの枠外を表示しないようにする
        self.scroll_x = max(0, self.scroll_x)

            # スクロールした幅に応じて敵を出現させる
            # self.spawn_enemy(last_screen_x + 128, self.scroll_x + 127)

        self.update_cond_index()
    def draw(self):
        pyxel.cls(12)
        pyxel.text(0, 0, "Scene: play", 6)


        pyxel.bltm(0, 0, 0, self.scroll_x, 0, 256, 224, 0)

        pyxel.camera(self.scroll_x, 0)
        self.player.draw()
        pyxel.camera()

        # 画面固定情報
        pyxel.blt(pyxel.width - 42, 10, 0, 16, 48, 16, 16, 8)
        pyxel.blt(pyxel.width - 26, 10, 0, 0, self.cond_index, 16, 16, 8)