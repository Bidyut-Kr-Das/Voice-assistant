import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from loading_screen import Ui_SplashScreen
##########################################################
counter = 0
class SplashScreen(QMainWindow):
    #################################################################
    ## class First_Window_Class(QmainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
###############################################################################
##it will remove the frame of window==>
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## it will show the gui
        self.show()

        ####################################

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(110)

    def progress(self):

        global counter
        self.ui.progressBar.setValue(counter)


        if counter > 100:
            self.timer.stop()
            self.close()
        
        counter += 1





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())


