# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../hotkey_show.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_showDialog(object):
    def setupUi(self, showDialog):
        showDialog.setObjectName("showDialog")
        showDialog.resize(481, 250)
        showDialog.setMinimumSize(QtCore.QSize(481, 250))
        showDialog.setMaximumSize(QtCore.QSize(481, 16777215))
        self.label = QtWidgets.QLabel(showDialog)
        self.label.setGeometry(QtCore.QRect(230, 30, 81, 21))
        self.label.setText("")
        self.label.setObjectName("label")
        self.hotkeyShortcut = QtWidgets.QLabel(showDialog)
        self.hotkeyShortcut.setGeometry(QtCore.QRect(160, 30, 51, 19))
        self.hotkeyShortcut.setStyleSheet("font: 10pt;")
        self.hotkeyShortcut.setObjectName("hotkeyShortcut")
        self.showDesciption = QtWidgets.QLabel(showDialog)
        self.showDesciption.setGeometry(QtCore.QRect(110, 80, 331, 91))
        self.showDesciption.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.showDesciption.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.showDesciption.setText("")
        self.showDesciption.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.showDesciption.setObjectName("showDesciption")
        self.hotkeyDescription = QtWidgets.QLabel(showDialog)
        self.hotkeyDescription.setGeometry(QtCore.QRect(20, 70, 81, 21))
        self.hotkeyDescription.setStyleSheet("font: 10pt;")
        self.hotkeyDescription.setObjectName("hotkeyDescription")
        self.showDialog_Button = QtWidgets.QDialogButtonBox(showDialog)
        self.showDialog_Button.setGeometry(QtCore.QRect(150, 210, 161, 21))
        self.showDialog_Button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.showDialog_Button.setObjectName("showDialog_Button")
        self.nameOfHotkeys = QtWidgets.QComboBox(showDialog)
        self.nameOfHotkeys.setGeometry(QtCore.QRect(20, 30, 121, 21))
        self.nameOfHotkeys.setObjectName("nameOfHotkeys")

        self.retranslateUi(showDialog)
        self.showDialog_Button.accepted.connect(showDialog.accept)
        self.showDialog_Button.rejected.connect(showDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(showDialog)

    def retranslateUi(self, showDialog):
        _translate = QtCore.QCoreApplication.translate
        showDialog.setWindowTitle(_translate("showDialog", "Dialog"))
        self.hotkeyShortcut.setText(_translate("showDialog", "Hotkey :"))
        self.hotkeyDescription.setText(_translate("showDialog", "Description :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    showDialog = QtWidgets.QDialog()
    ui = Ui_showDialog()
    ui.setupUi(showDialog)
    showDialog.show()
    sys.exit(app.exec_())

