import sys
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import ctypes

import time

user32 = ctypes.windll.user32

class SimMoveDemo(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.pix1 = QPixmap('pictures/frog1.png')
        self.pix2 = QPixmap('pictures/frog1.png')
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.setGeometry(100, 100, 646, 559)
        self.setFixedSize(self.size())
        self.showFullScreen()
        oImage = QImage("pictures/backGround.png")
        sImage = oImage.scaled(QSize(user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        self.car_move = CarMove(self)

        self.label = QLabel('', self)  # test, if it's really backgroundimage
        self.label.setGeometry(50, 50, 200, 50)
        self.__init_ui__()

        self.key_notifier = KeyNotifier()

        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

    def __init_ui__(self):
        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(user32.GetSystemMetrics(78) - 450, user32.GetSystemMetrics(79) - 60, 70, 60)

        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(user32.GetSystemMetrics(78) - 980, user32.GetSystemMetrics(79) - 60, 70, 60)

        self.setWindowTitle('Sim Slide')
        self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())
        self.pix3 = QPixmap('pictures/frog1.png')
        self.label1.setPixmap(self.pix3)

    def __update_position__(self, key):
        rec1 = self.label1.geometry()
        rec2 = self.label2.geometry()
        if key == Qt.Key_Right:
            if((rec1.x() + 20) < (user32.GetSystemMetrics(78)-50)):
                self.pix3 = QPixmap('pictures/frogRight.png')
                self.label1.setPixmap(self.pix3)
                self.label1.setGeometry(rec1.x() + 20, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            if ((rec1.y() + 58) < user32.GetSystemMetrics(79) - 50):
                self.pix3 = QPixmap('pictures/frogDown.png')
                self.label1.setPixmap(self.pix3)
                self.label1.setGeometry(rec1.x(), rec1.y() + 58, rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            if ((rec1.y() + 58) > 50):
                self.pix3 = QPixmap('pictures/frogUp.png')
                self.label1.setPixmap(self.pix3)
                self.label1.setGeometry(rec1.x(), rec1.y() - 58, rec1.width(), rec1.height())
        elif key == Qt.Key_Left:
            if ((rec1.x() + 20) > (user32.GetSystemMetrics(78) - 1345)):
                self.pix3 = QPixmap('pictures/frogLeft.png')
                self.label1.setPixmap(self.pix3)
                self.label1.setGeometry(rec1.x() - 20, rec1.y(), rec1.width(), rec1.height())

        if key == Qt.Key_D:
            if((rec2.x() + 13) < (user32.GetSystemMetrics(78)-50)):
                self.label2.setGeometry(rec2.x() + 13, rec2.y(), rec2.width(), rec2.height())
        elif key == Qt.Key_S:
            if ((rec2.y() + 58) < user32.GetSystemMetrics(79) - 50):
                self.label2.setGeometry(rec2.x(), rec2.y() + 58, rec2.width(), rec2.height())
        elif key == Qt.Key_W:
            if ((rec2.y() + 58) > 30):
                self.label2.setGeometry(rec2.x(), rec2.y() - 58, rec2.width(), rec2.height())
        elif key == Qt.Key_A:
            if ((rec2.x() + 13) > (user32.GetSystemMetrics(78) - 1345)):
                self.label2.setGeometry(rec2.x() - 13, rec2.y(), rec2.width(), rec2.height())

        if key == Qt.Key_Escape:
            sys.exit(app.exec_())

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


class CarMove(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.pix = QPixmap('greenCarLeft.png')
        self.label4 = QLabel(self)
        self.initPosition()

    def initPosition(self):
        self.label4.setPixmap(self.pix)
        self.label4.setGeometry(70, 595, 140, 60)

        self.show()

    def _update_position(self, key):
        rec2 = self.label4.geometry()


        while True:
            self.label4.setGeometry(rec2.x() + 1, rec2.y(), rec2.width(), rec2.height())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())
