# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../hotkey_add.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addDialog(object):
    def setupUi(self, addDialog):
        addDialog.setObjectName("addDialog")
        addDialog.resize(481, 250)
        addDialog.setMinimumSize(QtCore.QSize(481, 250))
        addDialog.setStyleSheet("font: 8pt \"Microsoft YaHei UI\";")
        self.addDialog_Button = QtWidgets.QDialogButtonBox(addDialog)
        self.addDialog_Button.setGeometry(QtCore.QRect(150, 210, 161, 21))
        self.addDialog_Button.setToolTip("")
        self.addDialog_Button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.addDialog_Button.setObjectName("addDialog_Button")
        self.nameText = QtWidgets.QLabel(addDialog)
        self.nameText.setGeometry(QtCore.QRect(20, 20, 51, 31))
        self.nameText.setStyleSheet("font: 10pt;")
        self.nameText.setObjectName("nameText")
        self.nameWriteText = QtWidgets.QPlainTextEdit(addDialog)
        self.nameWriteText.setGeometry(QtCore.QRect(70, 20, 131, 31))
        self.nameWriteText.setMinimumSize(QtCore.QSize(131, 31))
        self.nameWriteText.setMaximumSize(QtCore.QSize(131, 31))
        self.nameWriteText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.nameWriteText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nameWriteText.setTabChangesFocus(True)
        self.nameWriteText.setObjectName("nameWriteText")
        self.ctrlButton = QtWidgets.QRadioButton(addDialog)
        self.ctrlButton.setGeometry(QtCore.QRect(250, 20, 41, 17))
        self.ctrlButton.setObjectName("ctrlButton")
        self.altButton = QtWidgets.QRadioButton(addDialog)
        self.altButton.setGeometry(QtCore.QRect(250, 50, 41, 17))
        self.altButton.setObjectName("altButton")
        self.plusSign = QtWidgets.QLabel(addDialog)
        self.plusSign.setGeometry(QtCore.QRect(310, 30, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.plusSign.setFont(font)
        self.plusSign.setStyleSheet("font: 25 18pt \"Microsoft YaHei UI\";")
        self.plusSign.setObjectName("plusSign")
        self.hotkeyChar = QtWidgets.QLineEdit(addDialog)
        self.hotkeyChar.setGeometry(QtCore.QRect(350, 20, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.hotkeyChar.setFont(font)
        self.hotkeyChar.setStyleSheet("font: 14pt \"Microsoft YaHei UI\";")
        self.hotkeyChar.setMaxLength(1)
        self.hotkeyChar.setFrame(False)
        self.hotkeyChar.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.hotkeyChar.setAlignment(QtCore.Qt.AlignCenter)
        self.hotkeyChar.setClearButtonEnabled(False)
        self.hotkeyChar.setObjectName("hotkeyChar")
        self.hotkeyDescriptionWrite = QtWidgets.QPlainTextEdit(addDialog)
        self.hotkeyDescriptionWrite.setGeometry(QtCore.QRect(20, 120, 421, 80))
        self.hotkeyDescriptionWrite.setMinimumSize(QtCore.QSize(421, 71))
        self.hotkeyDescriptionWrite.setMaximumSize(QtCore.QSize(421, 80))
        self.hotkeyDescriptionWrite.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.hotkeyDescriptionWrite.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hotkeyDescriptionWrite.setTabChangesFocus(True)
        self.hotkeyDescriptionWrite.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.hotkeyDescriptionWrite.setReadOnly(False)
        self.hotkeyDescriptionWrite.setPlainText("")
        self.hotkeyDescriptionWrite.setObjectName("hotkeyDescriptionWrite")
        self.hotkeyDescription = QtWidgets.QLabel(addDialog)
        self.hotkeyDescription.setGeometry(QtCore.QRect(20, 90, 81, 21))
        self.hotkeyDescription.setStyleSheet("font: 10pt;")
        self.hotkeyDescription.setObjectName("hotkeyDescription")

        self.retranslateUi(addDialog)
        self.addDialog_Button.accepted.connect(addDialog.accept)
        self.addDialog_Button.rejected.connect(addDialog.reject)
        #QtCore.QMetaObject.connectSlotsByName(addDialog)

    def retranslateUi(self, addDialog):
        _translate = QtCore.QCoreApplication.translate
        addDialog.setWindowTitle(_translate("addDialog", "Dialog"))
        self.addDialog_Button.setStatusTip(_translate("addDialog", "Accept new Hotkey"))
        self.nameText.setText(_translate("addDialog", "Name :"))
        self.nameWriteText.setPlaceholderText(_translate("addDialog", "Name of Hotkey"))
        self.ctrlButton.setText(_translate("addDialog", "Ctrl"))
        self.altButton.setText(_translate("addDialog", "Alt"))
        self.plusSign.setText(_translate("addDialog", "+"))
        self.hotkeyDescriptionWrite.setPlaceholderText(_translate("addDialog", "Enter Text"))
        self.hotkeyDescription.setText(_translate("addDialog", "Description :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addDialog = QtWidgets.QDialog()
    ui = Ui_addDialog()
    ui.setupUi(addDialog)
    addDialog.show()
    sys.exit(app.exec_())

