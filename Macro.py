################
#Macro "Flexer"#                           
################
#Макрос "Flexer#                           
################
#Макрос "Flexer#                           
################

import keyboard as keyb
import time
import mouse

time1 = 0

#Variables with hot coavishes
#Переменные с горячими клавишами
#Змінні з горячими клавішами
hk_0 = 'w + r'
hk_1 = 'f + r'
hk_2 = 'm + l'
hk_3 = 'f + h'

#Cycle
#Цикл
#Цикл
while True:
    #combo W
    #комбо W
    #комбо W
    if keyb.is_pressed(hk_0):
        while True:
            keyb.press('w')
            time.sleep(0.1)
            keyb.release('w')
    #clamp W
    #зажим W
    #затиск W        
    if keyb.is_pressed(hk_1):
        while True:
            keyb.press('w')
    
    #clicker
    #кликер
    #клікер
    if keyb.is_pressed(hk_2):
        while True:
            if mouse.is_pressed(button = 'left'):
                while True:
                    time.sleep(0.1)
                    mouse.double_click(button = 'left')
                    if mouse.is_pressed(button = 'right'):
                        break

    #quit
    #выход
    #вихід
    if keyb.is_pressed(hk_3):
        while True:
            quit()
