# -coding:utf-8
from PyQt5.QtCore import Qt, QThread,QMutex,QMutexLocker
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
import PyQt5.sip  # 得加这个不然用pyinstaller打包exe时会出现 no module name pyqt5.sip的问题
import api
import sys,time,os,shutil
from subprocess import run
import win32con
import ctypes
import ctypes.wintypes
import threading
from home import Ui_Home

RUN = False

class Hotkey(QThread):  #创建一个Thread.threading的扩展类
    trigger = QtCore.pyqtSignal(str)
    def __init__(self,ui):
        super(Hotkey, self).__init__()

    def run(self):
        user32 = ctypes.windll.user32  # 加载user32.dll
        id1 = 105  # 注册热键的唯一id，用来区分热键
        id2 = 106
        id3 = 107
        id4 = 108
        id5 = 109
        id7 = 111
        id8 = 112
        id9 = 113
        w=[]
        s = []
        a = []
        d = []
        xx = []
        percent = []
        labename =""
        starts = []
        num = ""
        ends =[]

        if not user32.RegisterHotKey(None, id1, 4, win32con.VK_W):
            print("Unable to register id", id1) # 返回一个错误信息

        if not user32.RegisterHotKey(None, id2, 4, win32con.VK_A):
            print("Unable to register id", id2)

        if not user32.RegisterHotKey(None, id3, 4, win32con.VK_S):
            print("Unable to register id", id3) # 返回一个错误信息

        if not user32.RegisterHotKey(None, id4, 4, win32con.VK_D):
            print("Unable to register id", id4)
        if not user32.RegisterHotKey(None, id5, 0, win32con.VK_F2):
            print("Unable to register id", id5)
        if not user32.RegisterHotKey(None, id7, 4, win32con.VK_Q):
            print("Unable to register id", id7)
        if not user32.RegisterHotKey(None, id8, 0, win32con.VK_TAB):
            print("Unable to register id", id8)
        if not user32.RegisterHotKey(None, id9, 0, win32con.VK_F3):
            print("Unable to register id", id9)


        #以下为检测热键是否被按下，并在最后释放快捷键
        try:
            msg = ctypes.wintypes.MSG()

            while True:
                if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:



                    if msg.message == win32con.WM_HOTKEY:
                        if msg.wParam == id1 :
                            w = api.getPosition()


                        elif msg.wParam == id2:

                            a = api.getPosition()

                        elif msg.wParam == id3:
                            s = api.getPosition()


                        elif msg.wParam == id4:

                            d = api.getPosition()

                        elif msg.wParam == id5:

                            percent= api.getPosition()
                            self.trigger.emit("percent坐标:" + str(xx))


                        elif msg.wParam == id9:

                            xx = api.getPosition()
                            self.trigger.emit("create坐标:"+str(xx))

                        elif msg.wParam == id7:
                            if w != [] and s != [] and a != [] and d != []:

                                start_x = a[0]
                                start_y = w[1]
                                end_x = d[0]
                                end_y = s[1]
                                start = [start_x, start_y]
                                end = [end_x, end_y]
                                if  len(starts) ==0:
                                    starts.append(start)
                                    ends.append(end)
                                    self.trigger.emit("保存第"+str(len(starts))+"个坐标")
                                    self.trigger.emit("start:"+str(start)+",end:"+str(end))
                                elif len(start)>=1:
                                    if start!=starts[len(starts)-1] and end != ends[len(ends)-1]:
                                        starts.append(start)
                                        ends.append(end)
                                        self.trigger.emit("保存第" + str(len(starts)) + "个坐标")
                                        self.trigger.emit("start:" + str(start) + ",end:" + str(end))
                                    else:
                                        self.trigger.emit("坐标与上一个坐标相同，请重新选择坐标")

                        elif msg.wParam == id8:
                            if xx == []:
                                self.trigger.emit("请确定create坐标")
                            elif percent == []:
                                self.trigger.emit("请确定percent坐标")
                            elif starts !=[] and window.lineEdit.text()!="":
                                num = api.gettext(percent)

                                if labename == window.lineEdit.text():
                                    first = False
                                else:
                                    first = True
                                self.trigger.emit("标定坐标")
                                for i in range(len(ends)):
                                    self.trigger.emit("start:"+str(starts[i])+",end:"+str(ends[i]))
                                api.doWork(window.lineEdit.text(), int(num),starts,ends,xx,first)
                                labename = window.lineEdit.text()
                                starts = []
                                ends = []



                    user32.TranslateMessage(ctypes.byref(msg))
                    user32.DispatchMessageA(ctypes.byref(msg))

        finally:
            user32.UnregisterHotKey(None, id1)#必须得释放热键，否则下次就会注册失败，所以当程序异常退出，没有释放热键，
                                              #那么下次很可能就没办法注册成功了，这时可以换一个热键测试
            user32.UnregisterHotKey(None, id2)



class checkThread(QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, UI):
        super(checkThread, self).__init__()
        self.path = UI.lineEdit_2.text()

    def run(self):
        if self.path != "":
            if self.path[len(self.path)-1]=="/":
                self.path = self.path[:-1]
            num = 0
            self.files = api.fileList(self.path,2)
            for i in range(0,len(self.files)):
                if self.files[i][len(self.files[i])-3:len(self.files[i])] == "xml":
                    f = open(self.path+"/"+self.files[i], 'r+')
                    a = f.readlines()
                    f.close()
                    if  "\t<object>\n" in a:
                        num +=1
                    else:
                        os.remove(self.path+"/"+self.files[i])

            self.trigger.emit("有效量："+str(num))


        else:
            self.trigger.emit("请选择工作目录")

class pickThread(QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, UI):
        super(pickThread, self).__init__()
        self.path = UI.lineEdit_2.text()

    def run(self):
        if self.path != "":
            if self.path[len(self.path)-1]=="/":
                self.path = self.path[:-1]
            self.path = self.path.replace("/","\\")
            print(self.path)
            api.mkdir(self.path+"_out/")
            self.files = api.fileList(self.path,2)
            for i in range(0,len(self.files)):
                if self.files[i][len(self.files[i])-3:len(self.files[i])] == "xml":
                    f = open(self.path+"/"+self.files[i], 'r+')
                    a = f.readlines()
                    f.close()
                    if  "\t<object>\n" in a:
                        #os.system("copy "+self.path+"\\"+self.files[i][0:len(self.files[i])-4]+"* "+self.path+"_out\\")
                        run("copy \""+self.path+"\\"+self.files[i][0:len(self.files[i])-4]+"*\" \""+self.path+"_out\\\"", shell=True)
                        self.trigger.emit("已复制："+str(self.files[i][0:len(self.files[i])-4]))

                    else:
                        os.remove(self.path+"/"+self.files[i])
            self.trigger.emit("挑选完成")



        else:
            self.trigger.emit("请选择工作目录")


class mywindow(QtWidgets.QWidget, Ui_Home):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon/1.ico"))
        self.toolButton.clicked.connect(self.choseDir)
        self.pushButton_3.clicked.connect(self.pick)
        self.pushButton_4.clicked.connect(self.check)
        self.hotkey = Hotkey(self)
        self.hotkey.trigger.connect(self.update_text)
        self.hotkey.start()
        self.update_text("热键开启")
    def choseDir(self):
        self.path = QtWidgets.QFileDialog.getExistingDirectory(self, "浏览", "")
        self.lineEdit_2.setText(self.path)

    def update_text(self, message):
        self.textBrowser.append(message)

    def check(self):
        self.checkthread = checkThread(self)
        self.checkthread.trigger.connect(self.update_text)
        self.checkthread.start()

    def pick(self):
        self.pickthread = pickThread(self)
        self.pickthread.trigger.connect(self.update_text)
        self.pickthread.start()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
