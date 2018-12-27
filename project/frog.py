import sys
<<<<<<< HEAD

from PyQt5.QtCore import QSize, QObject
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
=======
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage, QPalette, QBrush
>>>>>>> 731677b9519669951070ac1f6a171031518f9995
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

import time

class SimMoveDemo(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.pix1 = QPixmap('frog1.png')
        self.pix2 = QPixmap('frog1.png')
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.setGeometry(100, 100, 646, 559)
        self.setFixedSize(self.size())
        self.showFullScreen()
        oImage = QImage("backGround.png")
        sImage = oImage.scaled(QSize(1920, 1080))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)



        self.label = QLabel('', self)  # test, if it's really backgroundimage
        self.label.setGeometry(50, 50, 200, 50)
        self.__init_ui__()

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

    def __init_ui__(self):

        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(1500, 1000, 60, 60)


        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(300, 1000, 50, 50)

        self.setWindowTitle('Sim Slide')
        self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
        rec1 = self.label1.geometry()
        rec2 = self.label2.geometry()

        if key == Qt.Key_Right:
            self.label1.setGeometry(rec1.x() + 13, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            self.label1.setGeometry(rec1.x(), rec1.y() + 13, rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            self.label1.setGeometry(rec1.x(), rec1.y() - 13, rec1.width(), rec1.height())
        elif key == Qt.Key_Left:
            self.label1.setGeometry(rec1.x() - 13, rec1.y(), rec1.width(), rec1.height())

        if key == Qt.Key_D:
            self.label2.setGeometry(rec2.x() + 13, rec2.y(), rec2.width(), rec2.height())
        elif key == Qt.Key_S:
            self.label2.setGeometry(rec2.x(), rec2.y() + 13, rec2.width(), rec2.height())
        elif key == Qt.Key_W:
            self.label2.setGeometry(rec2.x(), rec2.y() - 13, rec2.width(), rec2.height())
        elif key == Qt.Key_A:
            self.label2.setGeometry(rec2.x() - 13, rec2.y(), rec2.width(), rec2.height())

    def closeEvent(self, event):
        self.key_notifier.die()

class KeyNotifier(QObject):

    key_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.keys = []
        self.is_done = False

        self.thread = QThread()
        # move the Worker object to the Thread object
        # "push" self from the current thread to this thread
        self.moveToThread(self.thread)
        # Connect Thread started signal to Worker operational slot method
        self.thread.started.connect(self.__work__)

    def start(self):
        """
        Start notifications.
        """
        self.thread.start()

    def add_key(self, key):
        self.keys.append(key)

    def rem_key(self, key):
        self.keys.remove(key)

<<<<<<< HEAD
       self.action = QAction(QIcon(), "Down", self)
       self.action.setShortcut("ESC")
       self.action.setShortcutContext(Qt.ApplicationShortcut)
       self.addAction(self.action)

       QObject.connect(self.action, SIGNAL("triggered()"), self.down)
       self.show()
=======
    def die(self):
        """
        End notifications.
        """
        self.is_done = True
        self.thread.quit()

    @pyqtSlot()
    def __work__(self):
        """
        A slot with no params.
        """
        while not self.is_done:
            for k in self.keys:
                self.key_signal.emit(k)
            time.sleep(0.05)
>>>>>>> 731677b9519669951070ac1f6a171031518f9995

    def Exit(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are You Sure to Quit?', QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())
