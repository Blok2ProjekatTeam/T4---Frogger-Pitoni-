from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Rectangle import *
from Config import *
import time
import random

class Car(QWidget):
    def __init__(self,parent):

        super().__init__(parent)
        self.car = Rectangle(user32.GetSystemMetrics(78) - 2000, user32.GetSystemMetrics(79) - 83*3, 130, 83, "car")
        self.car1 = Rectangle(user32.GetSystemMetrics(78) - 1700, user32.GetSystemMetrics(79) - 83*3, 130, 83, "car")
        self.car2 = Rectangle(user32.GetSystemMetrics(78) - 1000, user32.GetSystemMetrics(79) - 83*3, 130, 83, "car")
        self.car3 = Rectangle(user32.GetSystemMetrics(78) - 600, user32.GetSystemMetrics(79) - 83*3, 130, 83, "car")

        self.truck = Rectangle(user32.GetSystemMetrics(78), user32.GetSystemMetrics(79) - 83*4, 200, 83, "car")
        self.truck1 = Rectangle(user32.GetSystemMetrics(78) - 400, user32.GetSystemMetrics(79) - 83*4, 200, 83, "car")
        self.truck2 = Rectangle(user32.GetSystemMetrics(78) - 800, user32.GetSystemMetrics(79) - 83*4, 200, 83, "car")

        self.caryellow = Rectangle(user32.GetSystemMetrics(78) , user32.GetSystemMetrics(79) - 83*2, 170, 83, "car")
        self.caryellow1 = Rectangle(user32.GetSystemMetrics(78) - 300, user32.GetSystemMetrics(79) - 83*2, 170, 83,"car")
        self.caryellow2 = Rectangle(user32.GetSystemMetrics(78) - 1300, user32.GetSystemMetrics(79) - 83 * 2, 170, 83, "car")
        self.caryellow3 = Rectangle(user32.GetSystemMetrics(78) - 1500, user32.GetSystemMetrics(79) - 83 * 2, 170, 83, "car")

        self.kamion = Rectangle(user32.GetSystemMetrics(78) - 2100, user32.GetSystemMetrics(79) - 83 * 5, 300, 83, "car")
        self.kamion1 = Rectangle(user32.GetSystemMetrics(78) - 1300, user32.GetSystemMetrics(79) - 83 * 5, 300, 83,"car")
        self.kamion2 = Rectangle(user32.GetSystemMetrics(78) - 900, user32.GetSystemMetrics(79) - 83 * 5, 300, 83,"car")

        self.cargreen = Rectangle(user32.GetSystemMetrics(78), user32.GetSystemMetrics(79) - 83 * 6, 170, 83, "car")
        self.cargreen1 = Rectangle(user32.GetSystemMetrics(78) - 900, user32.GetSystemMetrics(79) - 83 * 6, 170, 83, "car")
        self.cargreen2 = Rectangle(user32.GetSystemMetrics(78) - 1100, user32.GetSystemMetrics(79) - 83 * 6, 170, 83, "car")
        self.cargreen3 = Rectangle(user32.GetSystemMetrics(78) - 1500, user32.GetSystemMetrics(79) - 83 * 6, 170, 83, "car")

        self.config = Config()

        self.vreme = random.choice(self.config.mode)


    def initPosition(self):

        self.car.labelSet('pictures/blueCarRight.png')
        self.car1.labelSet('pictures/blueCarRight.png')
        self.car2.labelSet('pictures/blueCarRight.png')
        self.car3.labelSet('pictures/blueCarRight.png')

        self.truck.labelSet('pictures/firemanCarLeft.png')
        self.truck1.labelSet('pictures/firemanCarLeft.png')
        self.truck2.labelSet('pictures/firemanCarLeft.png')

        self.caryellow.labelSet('pictures/yellowCarLeft.png')
        self.caryellow1.labelSet('pictures/yellowCarLeft.png')
        self.caryellow2.labelSet('pictures/yellowCarLeft.png')
        self.caryellow3.labelSet('pictures/yellowCarLeft.png')

        self.kamion.labelSet('pictures/truckRight.png')
        self.kamion1.labelSet('pictures/truckRight.png')
        self.kamion2.labelSet('pictures/truckRight.png')

        self.cargreen.labelSet('pictures/greenCarLeft.png')
        self.cargreen1.labelSet('pictures/greenCarLeft.png')
        self.cargreen2.labelSet('pictures/greenCarLeft.png')
        self.cargreen3.labelSet('pictures/greenCarLeft.png')

        self.change_weather()

        self.show()

    def _update_position(self):
        rec1 = self.car.GetSize()
        rec0 = self.car1.GetSize()
        rec3 = self.car2.GetSize()
        rec4 = self.car3.GetSize()


        recT0 = self.truck.GetSize()
        recT1 = self.truck1.GetSize()
        recT2 = self.truck2.GetSize()

        recY1 = self.caryellow.GetSize()
        recY2 = self.caryellow1.GetSize()
        recY3 = self.caryellow2.GetSize()
        recY4 = self.caryellow3.GetSize()

        recK0 = self.kamion.GetSize()
        recK1 = self.kamion1.GetSize()
        recK2 = self.kamion2.GetSize()

        recG1 = self.cargreen.GetSize()
        recG2 = self.cargreen1.GetSize()
        recG3 = self.cargreen2.GetSize()
        recG4 = self.cargreen3.GetSize()


        self.car.move(rec1[0] + self.config.speedcar, rec1[1], rec1[2], rec1[3],'pictures/blueCarRight.png')
        self.car1.move(rec0[0] + self.config.speedcar, rec0[1], rec0[2], rec0[3], 'pictures/blueCarRight.png')
        self.car2.move(rec3[0] + self.config.speedcar, rec3[1], rec3[2], rec3[3], 'pictures/blueCarRight.png')
        self.car3.move(rec4[0] + self.config.speedcar, rec4[1], rec4[2], rec4[3], 'pictures/blueCarRight.png')

        self.truck.move(recT0[0] - self.config.speedfireman , recT0[1], recT0[2], recT0[3], 'pictures/firemanCarLeft.png')
        self.truck1.move(recT1[0] - self.config.speedfireman, recT1[1], recT1[2], recT1[3], 'pictures/firemanCarLeft.png')
        self.truck2.move(recT2[0] - self.config.speedfireman, recT2[1], recT2[2], recT2[3], 'pictures/firemanCarLeft.png')

        self.caryellow.move(recY1[0] - self.config.speedyellow, recY1[1], recY1[2], recY1[3], 'pictures/yellowCarLeft.png')
        self.caryellow1.move(recY2[0] - self.config.speedyellow, recY2[1], recY2[2], recY2[3], 'pictures/yellowCarLeft.png')
        self.caryellow2.move(recY3[0] - self.config.speedyellow, recY3[1], recY3[2], recY3[3], 'pictures/yellowCarLeft.png')
        self.caryellow3.move(recY4[0] - self.config.speedyellow, recY4[1], recY4[2], recY4[3], 'pictures/yellowCarLeft.png')

        self.kamion.move(recK0[0] + self.config.speedkamion, recK0[1], recK0[2], recK0[3], 'pictures/truckRight.png')
        self.kamion1.move(recK1[0] + self.config.speedkamion, recK1[1], recK1[2], recK1[3], 'pictures/truckRight.png')
        self.kamion2.move(recK2[0] + self.config.speedkamion, recK2[1], recK2[2], recK2[3], 'pictures/truckRight.png')

        self.cargreen.move(recG1[0] - self.config.speedgreen, recG1[1], recG1[2], recG1[3], 'pictures/greenCarLeft.png')
        self.cargreen1.move(recG2[0] - self.config.speedgreen, recG2[1], recG2[2], recG2[3], 'pictures/greenCarLeft.png')
        self.cargreen2.move(recG3[0] - self.config.speedgreen, recG3[1], recG3[2], recG3[3], 'pictures/greenCarLeft.png')
        self.cargreen3.move(recG4[0] - self.config.speedgreen, recG4[1], recG4[2], recG4[3], 'pictures/greenCarLeft.png')



        if rec0[0] >= 2000:
            self.car1.move(rec0[0] - 2180, rec0[1], rec0[2], rec0[3], 'pictures/blueCarRight.png')
        if rec1[0] >= 2000:
            self.car.move(rec1[0] - 2180, rec1[1], rec1[2], rec1[3], 'pictures/blueCarRight.png')
        if rec3[0] >= 2000:
            self.car2.move(rec3[0] - 2180, rec3[1], rec3[2], rec3[3], 'pictures/blueCarRight.png')
        if rec4[0] >= 2000:
            self.car3.move(rec4[0] - 2180, rec4[1], rec4[2], rec4[3], 'pictures/blueCarRight.png')

        if recT0[0] <= -200:
            self.truck.move(recT0[0] + 2350, recT0[1], recT0[2], recT0[3], 'pictures/firemanCarLeft.png')
        if recT1[0] <= -200:
            self.truck1.move(recT1[0] + 2350, recT1[1], recT1[2], recT1[3], 'pictures/firemanCarLeft.png')
        if recT2[0] <= -200:
            self.truck2.move(recT2[0] + 2350, recT2[1], recT2[2], recT2[3], 'pictures/firemanCarLeft.png')

        if recY1[0] <= -200:
            self.caryellow.move(recY1[0] + 2210, recY1[1], recY1[2], recY1[3], 'pictures/yellowCarLeft.png')
        if recY2[0] <= -200:
            self.caryellow1.move(recY2[0] + 2210, recY2[1], recY2[2], recY2[3], 'pictures/yellowCarLeft.png')
        if recY3[0] <= -200:
            self.caryellow2.move(recY3[0] + 2210, recY3[1], recY3[2], recY3[3], 'pictures/yellowCarLeft.png')
        if recY4[0] <= -200:
            self.caryellow3.move(recY4[0] +2210, recY4[1], recY4[2], recY4[3], 'pictures/yellowCarLeft.png')


        if recK0[0] >= 2000:
            self.kamion.move(recK0[0] - 2300, recK0[1], recK0[2], recK0[3], 'pictures/truckRight.png')
        if recK1[0] >= 2000:
            self.kamion1.move(recK1[0] - 2300, recK1[1], recK1[2], recK1[3], 'pictures/truckRight.png')
        if recK2[0] >= 2000:
            self.kamion2.move(recK2[0] - 2300, recK2[1], recK2[2], recK2[3], 'pictures/truckRight.png')

        if recG1[0] <= -200:
            self.cargreen.move(recG1[0] + 2210, recG1[1], recG1[2], recG1[3], 'pictures/greenCarLeft.png')
        if recG2[0] <= -200:
            self.cargreen1.move(recG2[0] + 2210, recG2[1], recG2[2], recG2[3], 'pictures/greenCarLeft.png')
        if recG3[0] <= -200:
            self.cargreen2.move(recG3[0] + 2210, recG3[1], recG3[2], recG3[3], 'pictures/greenCarLeft.png')
        if recG4[0] <= -200:
            self.cargreen3.move(recG4[0] + 2210, recG4[1], recG4[2], recG4[3], 'pictures/greenCarLeft.png')


    def change_weather(self):
        self.vreme = random.choice(Config.mode)
        Config.vreme =self.vreme
        if self.vreme == "snow":
            self.config.speedcar = 11
            self.config.speedgreen =25
            self.config.speedkamion =6
            self.config.speedfireman = 10
            self.config.speedyellow = 20
        if self.vreme == "rain":
            self.config.speedcar = 5
            self.config.speedgreen = 8
            self.config.speedkamion = 2
            self.config.speedfireman = 3
            self.config.speedyellow = 7
        if self.vreme == "normal":
            self.config.speedcar = 8
            self.config.speedgreen = 15
            self.config.speedkamion = 3
            self.config.speedfireman = 5
            self.config.speedyellow = 10



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
    def sleepthread(self):
        time.sleep(13)

    @pyqtSlot()
    def __work__(self):
        """
        A slot with no params.
        """
        while not self.is_done:
            self.carMovementSignal.emit()
            time.sleep(0.05)

class VremeSignal(QObject):

    timeSignal = pyqtSignal()

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
            self.timeSignal.emit()
            time.sleep(10)