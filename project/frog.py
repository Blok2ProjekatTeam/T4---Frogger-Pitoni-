import sys

from PyQt5.QtCore import QSize, QObject
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
       QWidget.__init__(self)
       self.setGeometry(100,100,646,559)
       self.setFixedSize(self.size())
       self.showFullScreen()
       oImage = QImage("pictures/backGround.png")
       sImage = oImage.scaled(QSize(1366,768))                   # resize Image to widgets size
       palette = QPalette()
       palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
       self.setPalette(palette)

       self.label = QLabel('', self)                        # test, if it's really backgroundimage
       self.label.setGeometry(50,50,200,50)

       self.action = QAction(QIcon(), "Down", self)
       self.action.setShortcut("ESC")
       self.action.setShortcutContext(Qt.ApplicationShortcut)
       self.addAction(self.action)

       QObject.connect(self.action, SIGNAL("triggered()"), self.down)
       self.show()

    def Exit(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are You Sure to Quit?', QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())