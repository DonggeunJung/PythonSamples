import pyautogui as pag
import time

# print(pag.size())
# time.sleep(1)
# print(pag.position())
# pag.moveTo(100, 200)
# pag.moveTo(100, 400, 3)
# pag.move(0, 200)
# pag.move(100, 200)
# pag.move(100, 200, 3)
# pag.moveTo(100, 50)
# pag.dragTo(200, 50, 2, button='left')
# pag.drag(-100, 0, 2, button='left')
# pag.moveTo(400, 170)
# pag.click()
# pag.click(x=100, y=200) # mouse click absolute axis
# pag.click(button='right') # mouse right click
# pag.click(clicks=2) # mouse double click
# pag.click(clicks=2, interval=0.25) # double click with interval 0.25 second
# pag.doubleClick() # mouse double click
pag.mouseDown() # mouse left button down
pag.mouseUp() # mouse left button up
pag.mouseDown(button='right') # mouse right button down
pag.mouseUp(button='right', x=200, y=300) # mouse right button up
