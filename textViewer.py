# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textViewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(946, 461)
        Form.setMinimumSize(QtCore.QSize(946, 461))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet("#Form{\n"
"    background-image: url(:/imgs/imgs/WhatsApp Image 2023-05-11 at 14.12.52.jpg);\n"
"\n"
"}\n"
"#textBrowser{\n"
"    background-image: url(:/imgs/imgs/WhatsApp Image 2023-05-11 at 14.12.52.jpg);\n"
"    color: rgba(255, 255, 255, 180)\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
