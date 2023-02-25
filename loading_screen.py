# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(544, 213)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 521, 191))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgba(91, 91, 91,190);\n"
"border-radius: 5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(40, 80, 431, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"background-color: rgb(148, 148, 148);\n"
"colour:rgba(255, 255, 255,100);\n"
"border-style: none;\n"
"text-allign: center;\n"
"border-radius: 10px;\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.703839 rgba(3, 222, 133, 255), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 10px;\n"
"}")
        self.progressBar.setProperty("value", 20)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(150, 120, 211, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"background-color: rgba(91, 91, 91,0);\n"
"color:rgb(3, 222, 133)\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 30, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color:rgba(148, 148, 148,0);\n"
"color:   rgb(3, 222, 133);\n"
"\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.raise_()
        self.progressBar.raise_()
        self.label_2.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_2.setText(_translate("SplashScreen", "Loading"))
        self.label.setText(_translate("SplashScreen", "<strong>F_R_I_D_A_Y"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())
