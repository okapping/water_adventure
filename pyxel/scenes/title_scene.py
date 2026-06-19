import pyxel
from .scene import Scene

class TitleScene:
    def __init__(self, game):
        self.game = game

    def start(self):
        pass

    def update(self):
        # キー入力をチェックする
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(
            pyxel.GAMEPAD1_BUTTON_B
        ):  # EnterキーまたはゲームパッドのBボタンが押された時
            # 画面の透明度を不透明にする
            pyxel.dither(1.0)

            # プレイ画面に切り替える
            self.game.change_scene(Scene.PLAY)


    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, "Scene: title", 6)