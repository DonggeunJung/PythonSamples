import pyautogui as pag
import matplotlib.pyplot as plt

# image1 = pag.screenshot()
# print(image1)

# image2 = pag.screenshot('screenshot.png')

# image3 = pag.screenshot(region=(0. 0. 300, 400))
# print(image3)
# plt.imshow(image3)


# btn_loc = pag.locateOnScreen('./images/pycharm_trash.png')

btn_loc = pag.locateOnScreen('./images/pycharm_trash.png', grayscale=True)
print(btn_loc)
