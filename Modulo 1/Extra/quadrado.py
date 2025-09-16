import pyautogui

pyautogui.press("win")
pyautogui.sleep(2)
pyautogui.write("paint")
pyautogui.sleep(2)
pyautogui.press("ENTER")
pyautogui.sleep(2)

pyautogui.moveTo(500,500)
pyautogui.dragRel(200,0,duration=4)
pyautogui.dragRel(0,200,duration=4)
pyautogui.dragRel(-200,0,duration=4)
pyautogui.dragRel(0,-200,duration=4)
pyautogui.dragRel(100,200,duration=4)
pyautogui.dragRel(-200,-100,duration=4)
