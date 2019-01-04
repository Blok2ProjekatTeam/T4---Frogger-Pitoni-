from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

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