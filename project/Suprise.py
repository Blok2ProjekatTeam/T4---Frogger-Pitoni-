from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Rectangle import *
from Config import *
import time
import random

class Suprise(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.suprise = Rectangle(user32.GetSystemMetrics(78) - random.randint(0,1920), user32.GetSystemMetrics(79) - 83*random.randint(0,6), 50, 83, "suprise")

    def initPosition(self):
        self.suprise.labelSet('pictures/fly.png')

        self.show()

    def hideFly(self):
        self.suprise.x = 0
        self.suprise.y = 0



class SupriseSignal(QObject):

    supriseSig = pyqtSignal()

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
            time.sleep(4)
            self.supriseSig.emit()
