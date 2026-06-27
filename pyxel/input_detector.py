import pyxel

class InputDetector():
  # 上方向の入力
  UP = [
    pyxel.KEY_UP,
    pyxel.GAMEPAD1_BUTTON_DPAD_UP,
    pyxel.KEY_W,
  ]

  # 下方向の入力
  DOWN = [
    pyxel.KEY_DOWN,
    pyxel.GAMEPAD1_BUTTON_DPAD_DOWN,
    pyxel.KEY_S,
  ]

  # 左方向の入力
  LEFT = [
    pyxel.KEY_LEFT,
    pyxel.GAMEPAD1_BUTTON_DPAD_LEFT,
    pyxel.KEY_A,
  ]

  # 右方向の入力
  RIGHT = [
    pyxel.KEY_RIGHT,
    pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT,
    pyxel.KEY_D,
  ]

  A = [
    pyxel.KEY_L,
    pyxel.KEY_SPACE,
    pyxel.KEY_RETURN,
    pyxel.GAMEPAD1_BUTTON_A
  ]

  B = [
    pyxel.KEY_K,
    pyxel.KEY_ESCAPE,
    pyxel.KEY_BACKSPACE,
    pyxel.GAMEPAD1_BUTTON_B
  ]

  X = [
    pyxel.KEY_I,
    pyxel.KEY_X,
    pyxel.GAMEPAD1_BUTTON_X
  ]
  
  Y = [
    pyxel.KEY_J,
    pyxel.KEY_Y,
    pyxel.GAMEPAD1_BUTTON_Y
  ]

  # 上で定義した配列を代入し、その中に該当する入力があればTrueを返す
  def btnp(key:list[int]) -> bool:
    for k in key:
      if pyxel.btnp(k):
        return True
    return False

  def btn(key:list[int]) -> bool:
    for k in key:
      if pyxel.btn(k):
        return True
    return False

  #こちらはキーを離した場合のための関数
  def btnr(key:list[int]) -> bool:
    for k in key:
      if pyxel.btnr(k):
        return True
    return False

