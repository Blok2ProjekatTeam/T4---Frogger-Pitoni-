from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Rectangle import *
import time

user32 = ctypes.windll.user32

class Move_Obj(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.woodLarge1 = Rectangle(0, 249, 369, 83, "wood")
        self.woodLarge2 = Rectangle(600, 249, 360, 83, "wood")
        self.woodLarge3 = Rectangle(1200, 249, 360, 83, "wood")
        self.woodLarge4 = Rectangle(1800, 249, 360, 83, "wood")

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

        self.show()

    def _update_position(self):
        # velika debla
        rec1 = self.woodLarge1.GetSize()
        if (rec1[0] > 1920):
            self.woodLarge1.move(rec1[0] - 2280, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')
        else:
            self.woodLarge1.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')

        rec1 = self.woodLarge2.GetSize()
        if (rec1[0] > 1920):
            self.woodLarge2.move(rec1[0] - 2280, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')
        else:
            self.woodLarge2.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')

        rec1 = self.woodLarge3.GetSize()
        if (rec1[0] > 1920):
            self.woodLarge3.move(rec1[0] - 2280, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')
        else:
            self.woodLarge3.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')

        rec1 = self.woodLarge4.GetSize()
        if (rec1[0] > 1920):
            self.woodLarge4.move(rec1[0] - 2280, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')
        else:
            self.woodLarge4.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodLarge.png')

        # srednja debla
        rec1 = self.woodMiddle1.GetSize()
        if (rec1[0] > 1920):
            self.woodMiddle1.move(rec1[0] - 2200, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')
        else:
            self.woodMiddle1.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')

        rec1 = self.woodMiddle2.GetSize()
        if (rec1[0] > 1920):
            self.woodMiddle2.move(rec1[0] - 2200, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')
        else:
            self.woodMiddle2.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')

        rec1 = self.woodMiddle3.GetSize()
        if (rec1[0] > 1920):
            self.woodMiddle3.move(rec1[0] - 2200, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')
        else:
            self.woodMiddle3.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')

        rec1 = self.woodMiddle4.GetSize()
        if (rec1[0] > 1920):
            self.woodMiddle4.move(rec1[0] - 2200, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')
        else:
            self.woodMiddle4.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')

        rec1 = self.woodMiddle5.GetSize()
        if (rec1[0] > 1920):
            self.woodMiddle5.move(rec1[0] - 2200, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')
        else:
            self.woodMiddle5.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodMiddle.png')

        # mala debla
        rec1 = self.woodSmall1.GetSize()
        if (rec1[0] > 1920):
            self.woodSmall1.move(rec1[0] - 2120, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')
        else:
            self.woodSmall1.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')

        rec1 = self.woodSmall2.GetSize()
        if (rec1[0] > 1920):
            self.woodSmall2.move(rec1[0] - 2120, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')
        else:
            self.woodSmall2.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')

        rec1 = self.woodSmall3.GetSize()
        if (rec1[0] > 1920):
            self.woodSmall3.move(rec1[0] - 2120, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')
        else:
            self.woodSmall3.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')

        rec1 = self.woodSmall4.GetSize()
        if (rec1[0] > 1920):
            self.woodSmall4.move(rec1[0] - 2120, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')
        else:
            self.woodSmall4.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')

        rec1 = self.woodSmall5.GetSize()
        if (rec1[0] > 1920):
            self.woodSmall5.move(rec1[0] - 2120, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')
        else:
            self.woodSmall5.move(rec1[0] + Config.speedwood, rec1[1], rec1[2], rec1[3], 'pictures/woodSmall.png')

        # donje kornjace(po 3 komada)
        rec1 = self.turtle21.GetSize()
        if (rec1[0] < -70):
            self.turtle21.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle21.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle22.GetSize()
        if (rec1[0] < -70):
            self.turtle22.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle22.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle23.GetSize()
        if (rec1[0] < -70):
            self.turtle23.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle23.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle24.GetSize()
        if (rec1[0] < -70):
            self.turtle24.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle24.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle25.GetSize()
        if (rec1[0] < -70):
            self.turtle25.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle25.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle26.GetSize()
        if (rec1[0] < -70):
            self.turtle26.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle26.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle27.GetSize()
        if (rec1[0] < -70):
            self.turtle27.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle27.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle28.GetSize()
        if (rec1[0] < -70):
            self.turtle28.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle28.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle29.GetSize()
        if (rec1[0] < -70):
            self.turtle29.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle29.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle210.GetSize()
        if (rec1[0] < -70):
            self.turtle210.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle210.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle211.GetSize()
        if (rec1[0] < -70):
            self.turtle211.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle211.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle212.GetSize()
        if (rec1[0] < -70):
            self.turtle212.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle212.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle213.GetSize()
        if (rec1[0] < -70):
            self.turtle213.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle213.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle214.GetSize()
        if (rec1[0] < -70):
            self.turtle214.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle214.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle215.GetSize()
        if (rec1[0] < -70):
            self.turtle215.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle215.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        # gornje kornjace(po 2 komada)
        rec1 = self.turtle11.GetSize()
        if (rec1[0] < -70):
            self.turtle11.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle11.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle12.GetSize()
        if (rec1[0] < -70):
            self.turtle12.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle12.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle13.GetSize()
        if (rec1[0] < -70):
            self.turtle13.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle13.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle14.GetSize()
        if (rec1[0] < -70):
            self.turtle14.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle14.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle15.GetSize()
        if (rec1[0] < -70):
            self.turtle15.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle15.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle16.GetSize()
        if (rec1[0] < -70):
            self.turtle16.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle16.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle17.GetSize()
        if (rec1[0] < -70):
            self.turtle17.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle17.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle18.GetSize()
        if (rec1[0] < -70):
            self.turtle18.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle18.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle19.GetSize()
        if (rec1[0] < -70):
            self.turtle19.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle19.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle110.GetSize()
        if (rec1[0] < -70):
            self.turtle110.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle110.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle111.GetSize()
        if (rec1[0] < -70):
            self.turtle111.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle111.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

        rec1 = self.turtle112.GetSize()
        if (rec1[0] < -70):
            self.turtle112.move(rec1[0] + 1990, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')
        else:
            self.turtle112.move(rec1[0] - Config.speedturtle, rec1[1], rec1[2], rec1[3], 'pictures/turtle1.png')

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


    def checkWeather(self):
        if Config.vreme == "snow":
            Config.speedwood = 8
            Config.speedturtle = 6
        if Config.vreme == "rain":
            Config.speedwood = 14
            Config.speedturtle = 12
        if Config.vreme == "normal":
            Config.speedwood = 10
            Config.speedturtle = 8


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
