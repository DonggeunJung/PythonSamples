import pyautogui as pag
import time
import datetime

str_cap_num = pag.prompt(text='Input capture count.', title='Capture count')
int_cap_num = int(str_cap_num)
print(f'Capture count : {int_cap_num}')

def screen_capture(x, y, width, height, filepath) :
    #pag.screenshot('screenshot.png', region=(150, 1230, 1100, 100))
    pag.screenshot(filepath, region=(x, y, width, height))

# screen_capture(150, 1230, 1100, 100, './news/screenshot.png')

for i in range(int_cap_num) :
    now_date = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    file_path = './news/' + now_date + '.png'
    screen_capture(150, 1230, 1100, 100, file_path)
    time.sleep(3)

print('Done')
