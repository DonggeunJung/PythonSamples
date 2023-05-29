import pyautogui as pag

# pag.write('Hello')
# pag.write('Good morning', interval=0.25)

# pag.keyDown('shift')
# pag.write('capital')
# pag.keyUp('shift')

# pag.write('123')
# pag.keyDown('shift')
# pag.press('left')
# pag.press('left')
# pag.press('left')
# pag.press(['left', 'left', 'left'])
# pag.keyUp('shift')
# pag.hotkey('ctrl', 'c') # ctrl + c
# pag.press(['right', 'right', 'right'])
# pag.keyDown('ctrl')
# pag.press('v')
# pag.keyUp('ctrl')

# pag.alert(text='alert message', title='alert box', button='OK')

# result = pag.confirm(text='confirm message', title='confirm box',\
#                      buttons=['OK', 'Cancel'])

result = pag.prompt(text='prompt message', title='prompt box',\
                      default='ID')
print('Result : ' + result)
