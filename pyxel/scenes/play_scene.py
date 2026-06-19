import pyxel
from .scene import Scene
from entities import Player

class PlayScene:
    def __init__(self, game):
        self.game = game

        game.player = Player(game, 0, 0)

    # プレイ画面を開始する
    def start(self):
        # 変更前のマップに戻す
        # pyxel.tilemaps[0].blt(0, 0, 2, 0, 0, 256, 16)

        # プレイ画面の状態を初期化する
        game = self.game  # ゲームクラス
        game.player = Player(game, 40, 100)  # プレイヤー
        # game.screen_x = 0  # フィールド表示範囲の左端のX座標
        # game.score = 0  # スコア

        # 敵を出現させる
        # self.spawn_enemy(0, 127)

        # BGMを再生する
        # pyxel.stop()
        # pyxel.playm(1, loop=True)

    def update(self):
        # プレイヤーを更新する
        if self.game.player is not None:
            self.game.player.update()

    def draw(self):
        pyxel.cls(12)
        pyxel.text(0, 0, "Scene: play", 6)

        pyxel.bltm(0, 0, 0, 0, 0, 321, 224, 0)

        self.game.player.draw()