# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(578, 355)
        font = QtGui.QFont()
        font.setFamily("黑体")
        Home.setFont(font)
        self.label = QtWidgets.QLabel(Home)
        self.label.setGeometry(QtCore.QRect(140, 0, 301, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_3 = QtWidgets.QGroupBox(Home)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 60, 541, 251))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setGeometry(QtCore.QRect(100, 10, 431, 41))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_path = QtWidgets.QLabel(self.groupBox_2)
        self.label_path.setGeometry(QtCore.QRect(10, 10, 54, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_path.setFont(font)
        self.label_path.setObjectName("label_path")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 11, 321, 19))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton.setGeometry(QtCore.QRect(380, 10, 37, 21))
        self.toolButton.setObjectName("toolButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser.setGeometry(QtCore.QRect(100, 50, 431, 181))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 130, 81, 23))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 80, 81, 23))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(40, 193, 51, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 31, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(Home)
        self.label_10.setGeometry(QtCore.QRect(420, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setFixedSize(Home.width(), Home.height())  # 禁止窗口伸缩
        Home.setWindowTitle(_translate("Home", "LabelImg标定辅助工具"))
        self.label.setText(_translate("Home", " LabelImg标定辅助工具"))
        self.label_path.setText(_translate("Home", "工作目录"))
        self.toolButton.setText(_translate("Home", "..."))
        self.pushButton_3.setText(_translate("Home", "挑选有效文件"))
        self.pushButton_4.setText(_translate("Home", "统计有效量"))
        self.label_2.setText(_translate("Home", "Label"))
        self.label_10.setText(_translate("Home", "By JonSon  2018.08.24"))

