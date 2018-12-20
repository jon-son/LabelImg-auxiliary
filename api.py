#-coding:utf-8
import os,time
import pyautogui as pag
import pyperclip as ppc
import math


def gettext(pos):
    pag.click(pos[0], pos[1], button='left')
    time.sleep(0.1)
    pag.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pag.hotkey('ctrl', 'c')
    time.sleep(0.1)
    return ppc.paste()

def paste(str):
    pag.typewrite(str)

def shiftDown():
    pag.keyDown('shift')

def shiftUp():
    pag.keyUp('shift')

def fileList(file_dir,type):
    for root, dirs, files in os.walk(file_dir):
        if type == 1:
            return dirs
        if type == 2:
            return files
    return list

def mkdir(dirPath):
    if os.path.exists(dirPath) == False:
        os.makedirs(dirPath)
        return 1
    else:
        return 2

def rmdir(dirPath):
    if os.path.exists(dirPath) == False:
        return 1
    else:
        os.system("rmdir /s/q " + dirPath)
        return 2

def getPosition():
    x, y = pag.position()
    pos=[]
    pos.append(x)
    pos.append(y)
    return pos
def getScreenshot(x,y):
    im = pag.screenshot()
    scr = im.getpixel((x,y))
    return scr

def isScreenshot(x,y,scr):
    flag = pag.pixelMatchesColor(x, y,scr)
    return flag

def doWork(lable,numx,starts,ends,xx,first):
    x = math.floor((int(numx)/100)*30)
    for i in range(0,len(starts)):
        time.sleep(0.1)
        pag.click(xx[0], xx[1], button='left')
        pag.moveTo(starts[i][0], starts[i][1])
        time.sleep(0.1)
        pag.click(starts[i][0], starts[i][1], button='left')
        time.sleep(0.1)
        if first:
            paste(lable)
            time.sleep(0.3)
        pag.hotkey('enter')
        time.sleep(0.1)
        drag_x = starts[i][0]+x
        drag_y = starts[i][1]+x

        pag.moveTo(drag_x,drag_y, duration=0.1)
        time.sleep(0.1)
        pag.dragTo(ends[i][0],ends[i][1], duration=0.1)




