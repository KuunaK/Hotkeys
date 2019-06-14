# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from hotkey_add import Ui_addDialog
from hotkey_show import Ui_showDialog
from hotkey_script import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 109)
        MainWindow.setMinimumSize(QtCore.QSize(300, 109))
        MainWindow.setMaximumSize(QtCore.QSize(300, 109))
        MainWindow.setStyleSheet("font: 8pt \"Leelawadee UI\";")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.showHotkey = QtWidgets.QPushButton(self.centralwidget)
        self.showHotkey.setGeometry(QtCore.QRect(160, 20, 111, 31))
        self.showHotkey.setToolTipDuration(-2)
        self.showHotkey.setStyleSheet("font: 8pt \"Microsoft YaHei UI\";")
        self.showHotkey.setObjectName("showHotkey")
        self.addHotkey = QtWidgets.QPushButton(self.centralwidget)
        self.addHotkey.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.addHotkey.setToolTipDuration(-2)
        self.addHotkey.setStyleSheet("font: 8pt \"Microsoft YaHei UI\";\n"
"")
        self.addHotkey.setCheckable(False)
        self.addHotkey.setChecked(False)
        self.addHotkey.setObjectName("addHotkey")
        self.hotkeyCount = QtWidgets.QLCDNumber(self.centralwidget)
        self.hotkeyCount.setGeometry(QtCore.QRect(120, 60, 51, 31))
        self.hotkeyCount.setToolTipDuration(-2)
        self.hotkeyCount.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"color: rgb(85, 85, 127);\n"
"font: 14pt;")
        self.hotkeyCount.setFrameShape(QtWidgets.QFrame.Panel)
        self.hotkeyCount.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hotkeyCount.setSmallDecimalPoint(False)
        self.hotkeyCount.setDigitCount(1)
        self.hotkeyCount.setMode(QtWidgets.QLCDNumber.Dec)
        self.hotkeyCount.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.hotkeyCount.setProperty("intValue", 0)
        self.hotkeyCount.setObjectName("hotkeyCount")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.showHotkey, self.addHotkey)

        #button clicked
        self.addHotkey.clicked.connect(self.add_clicked)
        self.showHotkey.clicked.connect(self.show_clicked)


    #Shows "Add Hotkey" window
    def add_clicked(self):
        addDialog = QtWidgets.QDialog()
        ui = Ui_addDialog()
        ui.setupUi(addDialog)
        addDialog.show()
        MainWindow.hide()
        thingy = addDialog.exec_()
        

        if thingy == QtWidgets.QDialog.Accepted:
            MainWindow.show()
            addDialog.hide()
            print("Seig fuck")
        else:
            MainWindow.show()
            addDialog.hide()
            print("Nope")



    #Shows "Show Hotkeys" window
    def show_clicked(self):
        showDialog = QtWidgets.QDialog()
        ui = Ui_showDialog()
        ui.setupUi(showDialog)
        showDialog.show()
        MainWindow.hide()
        thingy = showDialog.exec_()
        

        if thingy == QtWidgets.QDialog.Accepted:
            MainWindow.show()
            showDialog.hide()
            print("Seig fuck")
        else:
            MainWindow.show()
            showDialog.hide()
            print("Nope")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KuunaK\'s Hotkeys"))
        self.showHotkey.setToolTip(_translate("MainWindow", "List available Hotkeys"))
        self.showHotkey.setStatusTip(_translate("MainWindow", "Show Hotkeys"))
        self.showHotkey.setText(_translate("MainWindow", "Show Hotkeys"))
        self.addHotkey.setToolTip(_translate("MainWindow", "Adds a new hotkey"))
        self.addHotkey.setStatusTip(_translate("MainWindow", "Add Hotkey"))
        self.addHotkey.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Press to add new Hotkey</p></body></html>"))
        self.addHotkey.setText(_translate("MainWindow", "Add Hotkey"))
        self.hotkeyCount.setToolTip(_translate("MainWindow", "Shows count of Hotkeys created"))
        self.hotkeyCount.setStatusTip(_translate("MainWindow", "Hotkey Count"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

