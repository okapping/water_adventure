import pyxel
from scenes import Scene, TitleScene, PlayScene
from entities import Player

class Game:
    def __init__(self):
        pyxel.init(width=256, height=224 ,title="water_adventure")
        pyxel.mouse(True)
        pyxel.load("asset.pyxres")
        
        self.player = None

        self.scroll_x = 0
        self.scroll_y = 0

        self.scenes = {
            Scene.TITLE: TitleScene(self),
            Scene.PLAY: PlayScene(self),
        }
        self.active_scene = None  # 現在のシーン

        self.change_scene(Scene.TITLE)

        pyxel.run(self.update, self.draw)

    # シーンを変更する
    def change_scene(self, scene):
        self.active_scene = scene
        self.scenes[self.active_scene].start()

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # 現在のシーンを更新する
        self.scenes[self.active_scene].update()
        # if pyxel.btn(pyxel.KEY_RIGHT):
        #     self.scroll_x -= 2
        # if pyxel.btn(pyxel.KEY_LEFT):
        #     self.scroll_x += 2

    def draw(self):

        # 現在のシーンを描画する
        self.scenes[self.active_scene].draw()

        # pyxel.cls(0)
        # pyxel.camera()
        # pyxel.bltm(0, 0, 0, self.scroll_x, self.scroll_y, pyxel.width, pyxel.height)
        # pyxel.camera(self.scroll_x, self.scroll_y)
        # pyxel.text(4, 4, "test", 1)
        # pyxel.blt(self.player_x, self.player_y, 0, 16, 0, 16, 16, 6)

Game()