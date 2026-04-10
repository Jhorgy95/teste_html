import pyautogui as pg 
import time 

for i in range(10000):
    pg.click()
    time.sleep(0.1)
    pg.press('down')
    time.sleep(0.1)
    pg.press('enter')
    time.sleep(0.1)
    pg.press('down')
    time.sleep(0.1)
    pg.press('enter')
    time.sleep(0.1)
    pg.press('down')
    time.sleep(60)