import sys
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import ctypes
from objectMovement import ObjectMovement
from Move_Object import Move_Obj

import time

user32 = ctypes.windll.user32

class SimMoveDemo(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.pix1 = QPixmap('pictures/frog1.png')
        self.pix2 = QPixmap('pictures/frog1.png')
        # ****************
        self.pix3 = QPixmap('pictures/woodLarge.png')
        self.pix4 = QPixmap('pictures/woodMiddle.png')
        self.pix5 = QPixmap('pictures/woodSmall.png')
        self.pix6 = QPixmap('pictures/turtle1.png')
        self.pix7 = QPixmap('pictures/turtle2.png')
        self.pix8 = QPixmap('pictures/turtle3.png')
        # ****************
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        # ****************
        self.woodLarge = QLabel(self)
        self.woodLarge2 = QLabel(self)
        self.woodLarge3 = QLabel(self)
        self.woodMiddle = QLabel(self)
        self.woodMiddle2 = QLabel(self)
        self.woodMiddle3 = QLabel(self)
        self.woodMiddle4 = QLabel(self)
        self.woodSmall = QLabel(self)
        self.woodSmall2 = QLabel(self)
        self.woodSmall3 = QLabel(self)
        self.woodSmall4 = QLabel(self)
        self.woodSmall5 = QLabel(self)
        self.turtle11 = QLabel(self)
        self.turtle12 = QLabel(self)
        self.turtle13 = QLabel(self)
        self.turtle14 = QLabel(self)
        self.turtle15 = QLabel(self)
        self.turtle16 = QLabel(self)
        self.turtle17 = QLabel(self)
        self.turtle18 = QLabel(self)
        self.turtle19 = QLabel(self)
        self.turtle110 = QLabel(self)
        self.turtle111 = QLabel(self)
        self.turtle112 = QLabel(self)
        self.turtle21 = QLabel(self)
        self.turtle22 = QLabel(self)
        self.turtle23 = QLabel(self)
        self.turtle24 = QLabel(self)
        self.turtle25 = QLabel(self)
        self.turtle26 = QLabel(self)
        self.turtle31 = QLabel(self)
        self.turtle32 = QLabel(self)
        self.turtle33 = QLabel(self)
        self.turtle34 = QLabel(self)
        self.turtle35 = QLabel(self)
        self.turtle36 = QLabel(self)
        # ****************
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

        # **************************
        self.objectMovement = ObjectMovement()
        self.objectMovement.objMovementSignal.connect(self.move_obj)
        self.objectMovement.start()
        # **************************

    def __init_ui__(self):
        self.label1.setPixmap(self.pix1)
        self.label1.setGeometry(user32.GetSystemMetrics(78) - 450, user32.GetSystemMetrics(79) - 60, 70, 60)

        self.label2.setPixmap(self.pix2)
        self.label2.setGeometry(user32.GetSystemMetrics(78) - 980, user32.GetSystemMetrics(79) - 60, 70, 60)

        # ************************
        self.woodLarge.setPixmap(self.pix3)
        self.woodLarge.setGeometry(1400, 290, 500, 60)

        self.woodLarge2.setPixmap(self.pix3)
        self.woodLarge2.setGeometry(2000, 290, 500, 60)

        self.woodLarge3.setPixmap(self.pix3)
        self.woodLarge3.setGeometry(2600, 290, 500, 60)

        self.woodMiddle.setPixmap(self.pix4)
        self.woodMiddle.setGeometry(1300, 130, 300, 60)

        self.woodMiddle2.setPixmap(self.pix4)
        self.woodMiddle2.setGeometry(1700, 130, 300, 60)

        self.woodMiddle3.setPixmap(self.pix4)
        self.woodMiddle3.setGeometry(2100, 130, 300, 60)

        self.woodMiddle4.setPixmap(self.pix4)
        self.woodMiddle4.setGeometry(2500, 130, 300, 60)

        self.woodSmall.setPixmap(self.pix5)
        self.woodSmall.setGeometry(1200, 370, 300, 60)

        self.woodSmall2.setPixmap(self.pix5)
        self.woodSmall2.setGeometry(1500, 370, 300, 60)

        self.woodSmall3.setPixmap(self.pix5)
        self.woodSmall3.setGeometry(1800, 370, 300, 60)

        self.woodSmall4.setPixmap(self.pix5)
        self.woodSmall4.setGeometry(2100, 370, 300, 60)

        self.woodSmall5.setPixmap(self.pix5)
        self.woodSmall5.setGeometry(2400, 370, 300, 60)

        self.turtle11.setPixmap(self.pix6)  # turtle1 gore
        self.turtle11.setGeometry(0, 210, 200, 60)

        self.turtle12.setPixmap(self.pix6)  # turtle1 gore
        self.turtle12.setGeometry(75, 210, 200, 60)

        self.turtle13.setPixmap(self.pix6)  # turtle1 gore
        self.turtle13.setGeometry(150, 210, 200, 60)

        self.turtle14.setPixmap(self.pix6)  # turtle1 dole
        self.turtle14.setGeometry(0, 450, 200, 60)

        self.turtle15.setPixmap(self.pix6)  # turtle1 dole
        self.turtle15.setGeometry(75, 450, 200, 60)

        self.turtle16.setPixmap(self.pix6)  # turtle1 dole
        self.turtle16.setGeometry(150, 450, 200, 60)

        self.turtle17.setPixmap(self.pix6)  # turtle1 gore, drugi put
        self.turtle17.setGeometry(-300, 210, 200, 60)

        self.turtle18.setPixmap(self.pix6)  # turtle1 gore, drugi put
        self.turtle18.setGeometry(-375, 210, 200, 60)

        self.turtle19.setPixmap(self.pix6)  # turtle1 gore, drugi put
        self.turtle19.setGeometry(-450, 210, 200, 60)

        self.turtle110.setPixmap(self.pix6)  # turtle1 dole, drugi put
        self.turtle110.setGeometry(-300, 450, 200, 60)

        self.turtle111.setPixmap(self.pix6)  # turtle1 dole, drugi put
        self.turtle111.setGeometry(-375, 450, 200, 60)

        self.turtle112.setPixmap(self.pix6)  # turtle1 dole, drugi put
        self.turtle112.setGeometry(-450, 450, 200, 60)

        self.turtle21.setPixmap(self.pix7)
        # self.turtle21.setGeometry(200, 450, 200, 60)

        self.turtle22.setPixmap(self.pix7)
        # self.turtle22.setGeometry(260, 450, 200, 60)

        self.turtle23.setPixmap(self.pix7)
        # self.turtle23.setGeometry(320, 450, 200, 60)

        self.turtle24.setPixmap(self.pix7)  # turtle dole
        # self.turtle21.setGeometry(200, 450, 200, 60)

        self.turtle25.setPixmap(self.pix7)  # turtle dole
        # self.turtle22.setGeometry(260, 450, 200, 60)

        self.turtle26.setPixmap(self.pix7)  # turtle dole
        # self.turtle23.setGeometry(320, 450, 200, 60)

        self.turtle31.setPixmap(self.pix8)
        # self.turtle31.setGeometry(400, 450, 200, 60)

        self.turtle32.setPixmap(self.pix8)
        # self.turtle32.setGeometry(450, 450, 200, 60)

        self.turtle33.setPixmap(self.pix8)
        # self.turtle33.setGeometry(500, 450, 200, 60)

        self.turtle34.setPixmap(self.pix8)
        # self.turtle31.setGeometry(400, 450, 200, 60)

        self.turtle35.setPixmap(self.pix8)
        # self.turtle32.setGeometry(450, 450, 200, 60)

        self.turtle36.setPixmap(self.pix8)
        # self.turtle33.setGeometry(500, 450, 200, 60)
        # ************************
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

    # **************************
    def move_obj(self):
        Move_Obj.moveobj(self)
    # **************************


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
        self.pix = QPixmap('pictures/greenCarLeft.png')
        self.label4 = QLabel(self)

        self.pix2 = QPixmap('pictures/greenCarLeft.png')
        self.label5 = QLabel(self)

        self.pix3 = QPixmap('pictures/blueCarRight.png')
        self.label6 = QLabel(self)

        self.pix4 = QPixmap('pictures/firemanCarLeft.png')
        self.label7 = QLabel(self)

        self.pix5 = QPixmap('pictures/firemanCarLeft.png')
        self.label8 = QLabel(self)

        self.pix6 = QPixmap('pictures/truckRight.png')
        self.label9 = QLabel(self)

        self.pix7 = QPixmap('pictures/truckRight.png')
        self.label10 = QLabel(self)

        self.initPosition()

        self.carMovement = CarMovement()
        self.carMovement.carMovementSignal.connect(self._update_position)
        self.carMovement.start()


    def initPosition(self):
        self.label4.setPixmap(self.pix)
        self.label4.setGeometry(1300, 595, 1400, 60)

        self.label5.setPixmap(self.pix2)
        self.label5.setGeometry(1100, 595, 1400, 60)

        self.label6.setPixmap(self.pix3)
        self.label6.setGeometry(0, 530, 1400, 60)

        self.label7.setPixmap(self.pix4)
        self.label7.setGeometry(1300, 470, 1400, 60)

        self.label8.setPixmap(self.pix5)
        self.label8.setGeometry(1000, 470, 1400, 60)

        self.label9.setPixmap(self.pix6)
        self.label9.setGeometry(0, 410, 1400, 60)

        self.label10.setPixmap(self.pix6)
        self.label10.setGeometry(300, 410, 1400, 60)

        self.show()

    def _update_position(self):
        rec2 = self.label4.geometry()
        rec3 = self.label5.geometry()
        rec4 = self.label6.geometry()
        rec5 = self.label7.geometry()
        rec6 = self.label8.geometry()
        rec7 = self.label9.geometry()
        rec8 = self.label10.geometry()
        self.label4.setGeometry(rec2.x() - 5, rec2.y(), rec2.width(), rec2.height())
        self.label5.setGeometry(rec3.x() - 5, rec3.y(), rec3.width(), rec3.height())
        self.label6.setGeometry(rec4.x() + 8, rec4.y(), rec4.width(), rec4.height())
        self.label7.setGeometry(rec5.x() - 8, rec5.y(), rec5.width(), rec5.height())
        self.label8.setGeometry(rec6.x() - 8, rec6.y(), rec6.width(), rec6.height())
        self.label9.setGeometry(rec7.x() + 3, rec7.y(), rec7.width(), rec7.height())
        self.label10.setGeometry(rec8.x() + 3, rec8.y(), rec8.width(), rec8.height())
        if rec2.x() == 0:
            self.label4.setGeometry(1300, 595, 1400, 60)
        if rec3.x() == 0:
            self.label5.setGeometry(1300, 595, 1400, 60)
        if rec4.x() >= 1300:
            self.label6.setGeometry(0, 530, 1400, 60)
        if rec5.x() <= -70:
            self.label7.setGeometry(1300, 470, 1400, 60)
        if rec6.x() <= -70:
            self.label8.setGeometry(1300, 470, 1400, 60)
        if rec7.x() >= 1400:
            self.label9.setGeometry(0, 410, 1400, 60)
        if rec8.x() >= 1400:
            self.label10.setGeometry(0, 410, 1400, 60)


class CarMovement(QObject):

    carMovementSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

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
            self.carMovementSignal.emit()
            time.sleep(0.05)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = SimMoveDemo()
    sys.exit(app.exec_())
