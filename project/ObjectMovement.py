from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Rectangle import *
import time
from PyQt5 import QtGui
import  random

user32 = ctypes.windll.user32

class Move_Obj(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.woodLarge1 = Rectangle(0, 249, 369, 83, "wood")
        self.woodLarge2 = Rectangle(600, 249, 360, 83, "wood")
        self.woodLarge3 = Rectangle(1200, 249, 360, 83, "wood")
        self.woodLarge4 = Rectangle(1800, 249, 360, 83, "wood")

        self.font = QtGui.QFont()
        self.font.setFamily("Forte")
        self.font.setPointSize(30)

        self.config = Config()

        self.woodMiddle1 = Rectangle(0, 83, 280, 83, "wood")
        self.woodMiddle2 = Rectangle(450, 83, 280, 83, "wood")
        self.woodMiddle3 = Rectangle(900, 83, 280, 83, "wood")
        self.woodMiddle4 = Rectangle(1350, 83, 280, 83, "wood")
        self.woodMiddle5 = Rectangle(1800, 83, 280, 83, "wood")


        self.woodSmall1 = Rectangle(0, 332, 200, 83, "wood")
        self.woodSmall2 = Rectangle(400, 332, 200, 83, "wood")
        self.woodSmall3 = Rectangle(800, 332, 200, 83, "wood")
        self.woodSmall4 = Rectangle(1200, 332, 200, 83, "wood")
        self.woodSmall5 = Rectangle(1600, 332, 200, 83, "wood")

        self.turtle11 = Rectangle(1850, 166, 70, 83, "turtle")
        self.turtle12 = Rectangle(1780, 166, 70, 83, "turtle")
        self.turtle13 = Rectangle(1530, 166, 70, 83, "turtle")
        self.turtle14 = Rectangle(1460, 166, 70, 83, "turtle")
        self.turtle15 = Rectangle(1210, 166, 70, 83, "turtle")
        self.turtle16 = Rectangle(1140, 166, 70, 83, "turtle")
        self.turtle17 = Rectangle(890, 166, 70, 83, "turtle")
        self.turtle18 = Rectangle(820, 166, 70, 83, "turtle")
        self.turtle19 = Rectangle(570, 166, 70, 83, "turtle")
        self.turtle110 = Rectangle(500, 166, 70, 83, "turtle")
        self.turtle111 = Rectangle(250, 166, 70, 83, "turtle")
        self.turtle112 = Rectangle(180, 166, 70, 83, "turtle")


        self.turtle21 = Rectangle(1850, 415, 70, 83, "turtle")
        self.turtle22 = Rectangle(1780, 415, 70, 83, "turtle")
        self.turtle23 = Rectangle(1710, 415, 70, 83, "turtle")
        self.turtle24 = Rectangle(1460, 415, 70, 83, "turtle")
        self.turtle25 = Rectangle(1390, 415, 70, 83, "turtle")
        self.turtle26 = Rectangle(1320, 415, 70, 83, "turtle")
        self.turtle27 = Rectangle(1070, 415, 70, 83, "turtle")
        self.turtle28 = Rectangle(1000, 415, 70, 83, "turtle")
        self.turtle29 = Rectangle(930, 415, 70, 83, "turtle")
        self.turtle210 = Rectangle(680, 415, 70, 83, "turtle")
        self.turtle211 = Rectangle(610, 415, 70, 83, "turtle")
        self.turtle212 = Rectangle(540, 415, 70, 83, "turtle")
        self.turtle213 = Rectangle(290, 415, 70, 83, "turtle")
        self.turtle214 = Rectangle(220, 415, 70, 83, "turtle")
        self.turtle215 = Rectangle(150, 415, 70, 83, "turtle")

        self.rain = Rectangle(0, -1080, 1920, 1080, "rain")
        self.rain2 = Rectangle(0, -2160, 1920, 1080, "rain")

        self.snow = Rectangle(0, -1080, 1920, 1080, "snow")
        self.snow2 = Rectangle(0, -2160, 1920, 1080, "snow")

        #************************ MILI *******************************
        self.car = Rectangle(user32.GetSystemMetrics(78) - 2000, user32.GetSystemMetrics(79) - 83 * 3, 130, 83, "car")
        self.car1 = Rectangle(user32.GetSystemMetrics(78) - 1700, user32.GetSystemMetrics(79) - 83 * 3, 130, 83, "car")
        self.car2 = Rectangle(user32.GetSystemMetrics(78) - 1000, user32.GetSystemMetrics(79) - 83 * 3, 130, 83, "car")
        self.car3 = Rectangle(user32.GetSystemMetrics(78) - 600, user32.GetSystemMetrics(79) - 83 * 3, 130, 83, "car")

        self.truck = Rectangle(user32.GetSystemMetrics(78), user32.GetSystemMetrics(79) - 83 * 4, 200, 83, "car")
        self.truck1 = Rectangle(user32.GetSystemMetrics(78) - 400, user32.GetSystemMetrics(79) - 83 * 4, 200, 83, "car")
        self.truck2 = Rectangle(user32.GetSystemMetrics(78) - 800, user32.GetSystemMetrics(79) - 83 * 4, 200, 83, "car")

        self.caryellow = Rectangle(user32.GetSystemMetrics(78), user32.GetSystemMetrics(79) - 83 * 2, 170, 83, "car")
        self.caryellow1 = Rectangle(user32.GetSystemMetrics(78) - 300, user32.GetSystemMetrics(79) - 83 * 2, 170, 83, "car")
        self.caryellow2 = Rectangle(user32.GetSystemMetrics(78) - 1300, user32.GetSystemMetrics(79) - 83 * 2, 170, 83, "car")
        self.caryellow3 = Rectangle(user32.GetSystemMetrics(78) - 1500, user32.GetSystemMetrics(79) - 83 * 2, 170, 83, "car")

        self.kamion = Rectangle(user32.GetSystemMetrics(78) - 2100, user32.GetSystemMetrics(79) - 83 * 5, 300, 83, "car")
        self.kamion1 = Rectangle(user32.GetSystemMetrics(78) - 1300, user32.GetSystemMetrics(79) - 83 * 5, 300, 83, "car")
        self.kamion2 = Rectangle(user32.GetSystemMetrics(78) - 900, user32.GetSystemMetrics(79) - 83 * 5, 300, 83, "car")

        self.cargreen = Rectangle(user32.GetSystemMetrics(78), user32.GetSystemMetrics(79) - 83 * 6, 170, 83, "car")
        self.cargreen1 = Rectangle(user32.GetSystemMetrics(78) - 900, user32.GetSystemMetrics(79) - 83 * 6, 170, 83, "car")
        self.cargreen2 = Rectangle(user32.GetSystemMetrics(78) - 1100, user32.GetSystemMetrics(79) - 83 * 6, 170, 83, "car")
        self.cargreen3 = Rectangle(user32.GetSystemMetrics(78) - 1500, user32.GetSystemMetrics(79) - 83 * 6, 170, 83, "car")

        self.config = Config()

        self.vreme = random.choice(self.config.mode)

    def initPosition(self):
        self.woodLarge1.labelSet('pictures/woodLarge.png')
        self.woodLarge2.labelSet('pictures/woodLarge.png')
        self.woodLarge3.labelSet('pictures/woodLarge.png')
        self.woodLarge4.labelSet('pictures/woodLarge.png')

        self.woodMiddle1.labelSet('pictures/woodMiddle.png')
        self.woodMiddle2.labelSet('pictures/woodMiddle.png')
        self.woodMiddle3.labelSet('pictures/woodMiddle.png')
        self.woodMiddle4.labelSet('pictures/woodMiddle.png')
        self.woodMiddle5.labelSet('pictures/woodMiddle.png')

        self.woodSmall1.labelSet('pictures/woodSmall.png')
        self.woodSmall2.labelSet('pictures/woodSmall.png')
        self.woodSmall3.labelSet('pictures/woodSmall.png')
        self.woodSmall4.labelSet('pictures/woodSmall.png')
        self.woodSmall5.labelSet('pictures/woodSmall.png')

        self.turtle11.labelSet('pictures/turtle1.png')
        self.turtle12.labelSet('pictures/turtle1.png')
        self.turtle13.labelSet('pictures/turtle1.png')
        self.turtle14.labelSet('pictures/turtle1.png')
        self.turtle15.labelSet('pictures/turtle1.png')
        self.turtle16.labelSet('pictures/turtle1.png')
        self.turtle17.labelSet('pictures/turtle1.png')
        self.turtle18.labelSet('pictures/turtle1.png')
        self.turtle19.labelSet('pictures/turtle1.png')
        self.turtle110.labelSet('pictures/turtle1.png')
        self.turtle111.labelSet('pictures/turtle1.png')
        self.turtle112.labelSet('pictures/turtle1.png')
        self.turtle21.labelSet('pictures/turtle1.png')
        self.turtle22.labelSet('pictures/turtle1.png')
        self.turtle23.labelSet('pictures/turtle1.png')
        self.turtle24.labelSet('pictures/turtle1.png')
        self.turtle25.labelSet('pictures/turtle1.png')
        self.turtle26.labelSet('pictures/turtle1.png')
        self.turtle27.labelSet('pictures/turtle1.png')
        self.turtle28.labelSet('pictures/turtle1.png')
        self.turtle29.labelSet('pictures/turtle1.png')
        self.turtle210.labelSet('pictures/turtle1.png')
        self.turtle211.labelSet('pictures/turtle1.png')
        self.turtle212.labelSet('pictures/turtle1.png')
        self.turtle213.labelSet('pictures/turtle1.png')
        self.turtle214.labelSet('pictures/turtle1.png')
        self.turtle215.labelSet('pictures/turtle1.png')

        self.rain.labelSet('pictures/rain.png')
        self.rain2.labelSet('pictures/rain.png')

        self.snow.labelSet('pictures/snow.png')
        self.snow2.labelSet('pictures/snow.png')

        #************************ MILI ****************************
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

        self.show()

    def _update_position(self):
        # velika debla
        rec1 = self.woodLarge1.GetSize()
        if (rec1[0] > 1920):
            self.woodLarge1.move(rec1[0] - 2280, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')
        else:
            self.woodLarge1.move(rec1[0] + self.config.speedwood , rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')

        rec1 = self.woodLarge2.GetSize()
        if (rec1[0] > 1920):
            self.woodLarge2.move(rec1[0] - 2280, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')
        else:
            self.woodLarge2.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')

        rec1 = self.woodLarge3.GetSize()
        if (rec1[0] > 1920):
            self.woodLarge3.move(rec1[0] - 2280, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')
        else:
            self.woodLarge3.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')

        rec1 = self.woodLarge4.GetSize()
        if (rec1[0] > 1920):
            self.woodLarge4.move(rec1[0] - 2280, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')
        else:
            self.woodLarge4.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')

        # srednja debla
        rec1 = self.woodMiddle1.GetSize()
        if (rec1[0] > 1920):
            self.woodMiddle1.move(rec1[0] - 2200, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')
        else:
            self.woodMiddle1.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')

        rec1 = self.woodMiddle2.GetSize()
        if (rec1[0] > 1920):
            self.woodMiddle2.move(rec1[0] - 2200, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')
        else:
            self.woodMiddle2.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')

        rec1 = self.woodMiddle3.GetSize()
        if (rec1[0] > 1920):
            self.woodMiddle3.move(rec1[0] - 2200, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')
        else:
            self.woodMiddle3.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')

        rec1 = self.woodMiddle4.GetSize()
        if (rec1[0] > 1920):
            self.woodMiddle4.move(rec1[0] - 2200, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')
        else:
            self.woodMiddle4.move(rec1[0] + self.config.speedwood , rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')

        rec1 = self.woodMiddle5.GetSize()
        if (rec1[0] > 1920):
            self.woodMiddle5.move(rec1[0] - 2200, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')
        else:
            self.woodMiddle5.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')

        # mala debla
        rec1 = self.woodSmall1.GetSize()
        if (rec1[0] > 1920):
            self.woodSmall1.move(rec1[0] - 2120, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')
        else:
            self.woodSmall1.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')

        rec1 = self.woodSmall2.GetSize()
        if (rec1[0] > 1920):
            self.woodSmall2.move(rec1[0] - 2120, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')
        else:
            self.woodSmall2.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')

        rec1 = self.woodSmall3.GetSize()
        if (rec1[0] > 1920):
            self.woodSmall3.move(rec1[0] - 2120, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')
        else:
            self.woodSmall3.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')

        rec1 = self.woodSmall4.GetSize()
        if (rec1[0] > 1920):
            self.woodSmall4.move(rec1[0] - 2120, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')
        else:
            self.woodSmall4.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')

        rec1 = self.woodSmall5.GetSize()
        if (rec1[0] > 1920):
            self.woodSmall5.move(rec1[0] - 2120, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')
        else:
            self.woodSmall5.move(rec1[0] + self.config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')

        # donje kornjace(po 3 komada)
        rec1 = self.turtle21.GetSize()
        if (rec1[0] < -70):
            self.turtle21.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle21.move(rec1[0] -self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle22.GetSize()
        if (rec1[0] < -70):
            self.turtle22.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle22.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle23.GetSize()
        if (rec1[0] < -70):
            self.turtle23.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle23.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle24.GetSize()
        if (rec1[0] < -70):
            self.turtle24.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle24.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle25.GetSize()
        if (rec1[0] < -70):
            self.turtle25.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle25.move(rec1[0] - self.config.speedturtle , rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle26.GetSize()
        if (rec1[0] < -70):
            self.turtle26.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle26.move(rec1[0] - self.config.speedturtle , rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle27.GetSize()
        if (rec1[0] < -70):
            self.turtle27.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle27.move(rec1[0] - self.config.speedturtle , rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle28.GetSize()
        if (rec1[0] < -70):
            self.turtle28.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle28.move(rec1[0] - self.config.speedturtle , rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle29.GetSize()
        if (rec1[0] < -70):
            self.turtle29.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle29.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle210.GetSize()
        if (rec1[0] < -70):
            self.turtle210.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle210.move(rec1[0] - self.config.speedturtle , rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle211.GetSize()
        if (rec1[0] < -70):
            self.turtle211.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle211.move(rec1[0] - self.config.speedturtle , rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle212.GetSize()
        if (rec1[0] < -70):
            self.turtle212.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle212.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle213.GetSize()
        if (rec1[0] < -70):
            self.turtle213.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle213.move(rec1[0] - self.config.speedturtle , rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle214.GetSize()
        if (rec1[0] < -70):
            self.turtle214.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle214.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle215.GetSize()
        if (rec1[0] < -70):
            self.turtle215.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle215.move(rec1[0] - self.config.speedturtle , rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        # gornje kornjace(po 2 komada)
        rec1 = self.turtle11.GetSize()
        if (rec1[0] < -70):
            self.turtle11.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle11.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle12.GetSize()
        if (rec1[0] < -70):
            self.turtle12.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle12.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle13.GetSize()
        if (rec1[0] < -70):
            self.turtle13.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle13.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle14.GetSize()
        if (rec1[0] < -70):
            self.turtle14.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle14.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle15.GetSize()
        if (rec1[0] < -70):
            self.turtle15.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle15.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle16.GetSize()
        if (rec1[0] < -70):
            self.turtle16.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle16.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle17.GetSize()
        if (rec1[0] < -70):
            self.turtle17.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle17.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle18.GetSize()
        if (rec1[0] < -70):
            self.turtle18.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle18.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle19.GetSize()
        if (rec1[0] < -70):
            self.turtle19.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle19.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle110.GetSize()
        if (rec1[0] < -70):
            self.turtle110.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle110.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle111.GetSize()
        if (rec1[0] < -70):
            self.turtle111.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle111.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle112.GetSize()
        if (rec1[0] < -70):
            self.turtle112.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle112.move(rec1[0] - self.config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.snow.GetSize()
        if (Config.vreme == "snow"):
            if (rec1[1] > 1080):
                self.snow.move(rec1[0], -1080, rec1[2], rec1[3], 'pictures/snow.png')
            else:
                self.snow.move(rec1[0], rec1[1] + 5, rec1[2], rec1[3], 'pictures/snow.png')

        rec1 = self.snow2.GetSize()
        if (Config.vreme == "snow"):
            if (rec1[1] > 1080):
                self.snow2.move(rec1[0], -1080, rec1[2], rec1[3], 'pictures/snow.png')
            else:
                self.snow2.move(rec1[0], rec1[1] + 5, rec1[2], rec1[3], 'pictures/snow.png')

        # padanje kise
        rec1 = self.rain.GetSize()
        if (Config.vreme == "rain"):
            if (rec1[1] > 1080):
                self.rain.move(rec1[0], -1080, rec1[2], rec1[3], 'pictures/rain.png')
            else:
                self.rain.move(rec1[0], rec1[1] + 10, rec1[2], rec1[3], 'pictures/rain.png')

        rec1 = self.rain2.GetSize()
        if (Config.vreme == "rain"):
            if (rec1[1] > 1080):
                self.rain2.move(rec1[0], -1080, rec1[2], rec1[3], 'pictures/rain.png')
            else:
                self.rain2.move(rec1[0], rec1[1] + 10, rec1[2], rec1[3], 'pictures/rain.png')

        if (Config.vreme == "normal"):
            self.snow.move(rec1[0], -1080, rec1[2], rec1[3], 'pictures/snow.png')
            self.snow2.move(rec1[0], -2160, rec1[2], rec1[3], 'pictures/snow.png')
            self.rain.move(rec1[0], -1080, rec1[2], rec1[3], 'pictures/rain.png')
            self.rain2.move(rec1[0], -2160, rec1[2], rec1[3], 'pictures/rain.png')

        if (Config.vreme == "rain"):
            self.snow.move(rec1[0], -1080, rec1[2], rec1[3], 'pictures/snow.png')
            self.snow2.move(rec1[0], -2160, rec1[2], rec1[3], 'pictures/snow.png')

        if (Config.vreme == "snow"):
            self.rain.move(rec1[0], -1080, rec1[2], rec1[3], 'pictures/rain.png')
            self.rain2.move(rec1[0], -2160, rec1[2], rec1[3], 'pictures/rain.png')

        #************************* MILI *************************************
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

        self.car.move(rec1[0] + self.config.speedcar, rec1[1], rec1[2], rec1[3], 'pictures/blueCarRight.png')
        self.car1.move(rec0[0] + self.config.speedcar, rec0[1], rec0[2], rec0[3], 'pictures/blueCarRight.png')
        self.car2.move(rec3[0] + self.config.speedcar, rec3[1], rec3[2], rec3[3], 'pictures/blueCarRight.png')
        self.car3.move(rec4[0] + self.config.speedcar, rec4[1], rec4[2], rec4[3], 'pictures/blueCarRight.png')

        self.truck.move(recT0[0] - self.config.speedfireman, recT0[1], recT0[2], recT0[3],
                        'pictures/firemanCarLeft.png')
        self.truck1.move(recT1[0] - self.config.speedfireman, recT1[1], recT1[2], recT1[3],
                         'pictures/firemanCarLeft.png')
        self.truck2.move(recT2[0] - self.config.speedfireman, recT2[1], recT2[2], recT2[3],
                         'pictures/firemanCarLeft.png')

        self.caryellow.move(recY1[0] - self.config.speedyellow, recY1[1], recY1[2], recY1[3],
                            'pictures/yellowCarLeft.png')
        self.caryellow1.move(recY2[0] - self.config.speedyellow, recY2[1], recY2[2], recY2[3],
                             'pictures/yellowCarLeft.png')
        self.caryellow2.move(recY3[0] - self.config.speedyellow, recY3[1], recY3[2], recY3[3],
                             'pictures/yellowCarLeft.png')
        self.caryellow3.move(recY4[0] - self.config.speedyellow, recY4[1], recY4[2], recY4[3],
                             'pictures/yellowCarLeft.png')

        self.kamion.move(recK0[0] + self.config.speedkamion, recK0[1], recK0[2], recK0[3], 'pictures/truckRight.png')
        self.kamion1.move(recK1[0] + self.config.speedkamion, recK1[1], recK1[2], recK1[3], 'pictures/truckRight.png')
        self.kamion2.move(recK2[0] + self.config.speedkamion, recK2[1], recK2[2], recK2[3], 'pictures/truckRight.png')

        self.cargreen.move(recG1[0] - self.config.speedgreen, recG1[1], recG1[2], recG1[3], 'pictures/greenCarLeft.png')
        self.cargreen1.move(recG2[0] - self.config.speedgreen, recG2[1], recG2[2], recG2[3],
                            'pictures/greenCarLeft.png')
        self.cargreen2.move(recG3[0] - self.config.speedgreen, recG3[1], recG3[2], recG3[3],
                            'pictures/greenCarLeft.png')
        self.cargreen3.move(recG4[0] - self.config.speedgreen, recG4[1], recG4[2], recG4[3],
                            'pictures/greenCarLeft.png')

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
            self.caryellow3.move(recY4[0] + 2210, recY4[1], recY4[2], recY4[3], 'pictures/yellowCarLeft.png')

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


    def checkWeather(self):
        self.vreme = random.choice(Config.mode)
        Config.vreme = self.vreme
        if Config.vreme == "snow":
            print("sneg")
            print(self.config.speedwood)
            print(Config.speedwood)
            self.config.speedwood  = Config.speedwood - 4
            self.config.speedturtle = Config.speedturtle - 4
            Config.attachSpeedWood = self.config.speedwood
            Config.attachSpeedTurtle = self.config.speedturtle
            Config.speedFrog = 30
            self.config.speedcar = Config.speedcar + 4
            self.config.speedgreen = Config.speedgreen + 5
            self.config.speedkamion = Config.speedkamion + 2
            self.config.speedfireman = Config.speedfireman + 3
            self.config.speedyellow = Config.speedyellow + 5
            print(self.config.speedwood)
            print(Config.speedwood)
        if Config.vreme == "rain":
            print("Kisa")
            print(self.config.speedwood)
            print(Config.speedwood)
            self.config.speedwood = Config.speedwood + 4
            self.config.speedturtle = Config.speedturtle + 4
            Config.attachSpeedWood = self.config.speedwood
            Config.attachSpeedTurtle = self.config.speedturtle
            Config.speedFrog = 70
            self.config.speedcar = Config.speedcar - 4
            self.config.speedgreen = Config.speedgreen - 5
            self.config.speedkamion = Config.speedkamion - 2
            self.config.speedfireman = Config.speedfireman - 3
            self.config.speedyellow = Config.speedyellow - 5
            print(self.config.speedwood)
            print(Config.speedwood)
        if Config.vreme == "normal":
            print("normal")
            print(self.config.speedwood)
            print(Config.speedwood)
            self.config.speedwood = Config.speedwood
            self.config.speedturtle = Config.speedturtle
            Config.attachSpeedWood = self.config.speedwood
            Config.attachSpeedTurtle = self.config.speedturtle
            Config.speedFrog = 50
            self.config.speedcar = Config.speedcar
            self.config.speedgreen = Config.speedgreen
            self.config.speedkamion = Config.speedkamion
            self.config.speedfireman = Config.speedfireman
            self.config.speedyellow = Config.speedyellow
            print(self.config.speedwood)
            print(Config.speedwood)


class ObjectMovement(QObject):

    objMovementSignal = pyqtSignal()

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
            self.objMovementSignal.emit()
            time.sleep(0.05)

class SignalVreme(QObject):

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
            time.sleep(0.3)