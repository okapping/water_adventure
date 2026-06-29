import pyxel
from .scene import Scene
from entities import Player, Leaf
from collision import *
from constants import *

SCROLL_BORDER_X = 110

class PlayScene:
    def __init__(self, game):
        self.game = game

        self.player = None

        self.scroll_x = 0
        self.scroll_y = 0

        self.enemies = []

        self.cond_index = 64

    # プレイ画面を開始する
    def start(self):
        # 変更前のマップに戻す
        # pyxel.tilemaps[0].blt(0, 0, 2, 0, 0, 256, 16)
        # pyxel.bltm(0, 0, 0, self.scroll_x, 0, 256, 224, 0)

        # プレイ画面の状態を初期化する
        game = self.game  # ゲームクラス
        self.player = Player(game, self, 40, 100)  # プレイヤー
        game.scroll_x = 0  # フィールド表示範囲の左端のX座標
        # game.score = 0  # スコア

        # 敵を出現させる
        self.spawn_enemy(0, 256)

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

    # 敵を出現させる
    def spawn_enemy(self, left_x, right_x):
        game = self.game
        enemies = self.enemies

        # 判定範囲のタイルを計算する
        left_x = pyxel.ceil(left_x / 8)
        right_x = pyxel.floor(right_x / 8)

        # 判定範囲のタイルに応じて敵を出現させる
        for tx in range(left_x, right_x + 1):
            for ty in range(28):
                x = tx * 8
                y = ty * 8
                tile_type = get_tile_type(x, y)

                if tile_type == TILE_LEAF:
                    enemies.append(Leaf(game, self, x, y))
                # if tile_type == TILE_SLIME1_POINT:  # グリーンスライムの出現位置の時
                #     enemies.append(Slime(game, x, y, False))
                # elif tile_type == TILE_SLIME2_POINT:  # レッドスライムの出現位置の時
                #     enemies.append(Slime(game, x, y, True))
                # elif tile_type == TILE_MUMMY_POINT:  # マミーの出現位置の時
                #     enemies.append(Mummy(game, x, y))
                # elif tile_type == TILE_FLOWER_POINT:  # フラワーの出現位置の時
                #     enemies.append(Flower(game, x, y))
                else:
                    continue

                # 出現位置タイルを消す
                pyxel.tilemaps[0].pset(tx, ty, (0, 0))

    def update(self):
        # プレイヤーを更新する
        if self.player is not None:
            self.player.update()

        # プレイヤーの移動範囲を制限する
        self.player.x = min(max(self.player.x, self.scroll_x), 2040)
        self.player.y = max(self.player.y, 0)

        # プレイヤーがスクロール境界を越えたら画面をスクロールする
        # 左端
        last_scroll_x = self.scroll_x
        if self.player.x < self.scroll_x+SCROLL_BORDER_X:
            dx = self.player.x-(self.scroll_x+SCROLL_BORDER_X)
            self.scroll_x = self.scroll_x+dx
        # 右端
        if self.player.x > self.scroll_x+pyxel.width-SCROLL_BORDER_X-16:
            dx = self.player.x-(self.scroll_x+pyxel.width-SCROLL_BORDER_X-16)
            self.scroll_x = self.scroll_x+dx

        # ステージの枠外を表示しないようにする
        self.scroll_x = max(0, min(300, self.scroll_x))
        
        # スクロールした幅に応じて敵を出現させる
        self.spawn_enemy(last_scroll_x+256, self.scroll_x + 255)

        # 敵を更新する
        for enemy in self.enemies.copy():
            enemy.update()

        self.update_cond_index()
    def draw(self):
        pyxel.cls(12)
        pyxel.text(0, 0, "Scene: play", 6)


        pyxel.bltm(0, 0, 0, self.scroll_x, 0, 256, 224, 0)

        pyxel.camera(self.scroll_x, 0)
        self.player.draw()

        # 敵を更新する
        for enemy in self.enemies:
            enemy.draw()

        pyxel.camera()

        # 画面固定情報
        pyxel.blt(pyxel.width - 42, 10, 0, 16, 48, 16, 16, 8)
        pyxel.blt(pyxel.width - 26, 10, 0, 0, self.cond_index, 16, 16, 0)