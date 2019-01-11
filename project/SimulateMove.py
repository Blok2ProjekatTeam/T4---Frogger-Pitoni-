import sys
from ObjectMovement import *
from Car import *
from KeyNotifier import *
import ctypes
from Rectangle import *
from Config import *
from Suprise import *


user32 = ctypes.windll.user32

class SimMoveDemo(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        Config.window = self

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


        # Car Move
        self.car_move = Car(self)
        self.car_move.initPosition()
        self.car_move.carMovement = CarMovement()
        self.car_move.carMovement.carMovementSignal.connect(self.car_move._update_position)
        self.car_move.vremeSignal = VremeSignal()
        self.car_move.vremeSignal.timeSignal.connect(self.car_move.change_weather)
        self.car_move.vremeSignal.start()
        self.car_move.carMovement.start()
        # self.car_move.__init__(self)

        #FLY
        self.suprise = Suprise(self)
        self.suprise.supriseSign = SupriseSignal()
        self.suprise.supriseSign.supriseSig.connect(self.suprise.initPosition)
        self.suprise.supriseSign.start()


        self.refresh = Refresh()
        self.refresh.refreshSignal.connect(self.__check_position__)
        self.refresh.start()

        # Wood Move
        self.objectMovement = Move_Obj(self)
        # self.objectMovement.__init__(self)
        self.objectMovement.initPosition()
        self.objectMovement.ObjectMovement = ObjectMovement()
        self.objectMovement.ObjectMovement.objMovementSignal.connect(self.objectMovement._update_position)
        self.objectMovement.ObjectMovement.start()

        self.objectMovement.vremeSignal = VremeSignal()
        self.objectMovement.vremeSignal.timeSignal.connect(self.objectMovement.checkWeather)
        self.objectMovement.vremeSignal.start()

      #  self.car_move = CarMove(self)

        self.frog1 = Rectangle(user32.GetSystemMetrics(78) - 750, user32.GetSystemMetrics(79) - 75, 70, 60, "frog")
        self.frog2 = Rectangle(user32.GetSystemMetrics(78) - 1380, user32.GetSystemMetrics(79) - 75, 70, 60, "frog")
        self.pix1 = QPixmap('pictures/frog1.png')
        self.pix2 = QPixmap('pictures/frog1.png')
        self.label = QLabel('', self)  # test, if it's really backgroundimage
        self.label.setGeometry(50, 50, 200, 50)
        self.__init_ui__()

        self.key_notifier = KeyNotifier()

        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

        # **************************
       # self.objectMovement = ObjectMovement()
       # self.objectMovement.objMovementSignal.connect(self.move_obj)
       # self.objectMovement.start()
        # **************************

    def __init_ui__(self):
        self.frog1.labelSet('pictures/frog1.png')

        self.frog2.labelSet('pictures/frog1.png')

        self.setWindowTitle('Frogger')
        self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())
        self.frog1.labelSet('pictures/frog1.png')
        self.frog2.labelSet('pictures/frog1.png')

    def __check_position__(self):
        if(self.frog1.y > 498):
            if (not self.frog1.intersectsCars()):
                self.frog1.x = user32.GetSystemMetrics(78) - 750
                self.frog1.y = user32.GetSystemMetrics(79) - 75
                self.frog1.labelSet('pictures/frog1.png')

            if (not self.frog1.intersectsFly()):
                self.suprise.hideFly()

        else:
            if (self.frog1.intersectsWood()):
                self.frog1.x = user32.GetSystemMetrics(78) - 750
                self.frog1.y = user32.GetSystemMetrics(79) - 75
                self.frog1.labelSet('pictures/frog1.png')

        if (self.frog2.y > 498):
            if (not self.frog2.intersectsCars()):
                self.frog2.x = user32.GetSystemMetrics(78) - 1380
                self.frog2.y = user32.GetSystemMetrics(79) - 75
                self.frog2.labelSet('pictures/frog1.png')
            if (not self.frog2.intersectsFly()):
                self.suprise.hideFly()
        else:
            if (self.frog2.intersectsWood()):
                self.frog2.x = user32.GetSystemMetrics(78) - 1380
                self.frog2.y = user32.GetSystemMetrics(79) - 75
                self.frog2.labelSet('pictures/frog1.png')



    def __update_position__(self, key):
        rec1 = self.frog1.GetPosition()
        rec2 = self.frog2.GetPosition()

        if key == Qt.Key_Right:
            if((rec1[0] + 50) < (user32.GetSystemMetrics(78)-50) and self.frog1.isEmpty(50,0,1)):
                self.frog1.move(rec1[0] + 50, rec1[1], self.frog1.w, self.frog1.h, 'pictures/frogRight.png')
        elif key == Qt.Key_Down:
            if ((rec1[1] + 83) < user32.GetSystemMetrics(79) - 50 and self.frog1.isEmpty(0,83,1)):
                self.frog1.move(rec1[0], rec1[1] + 83,self.frog1.w, self.frog1.h,'pictures/frogDown.png')
        elif key == Qt.Key_Up:
            if ((rec1[1] - 83) > 0 and self.frog1.isEmpty(0,83,0)):
                self.frog1.move(rec1[0], rec1[1] -83,self.frog1.w, self.frog1.h, 'pictures/frogUp.png')
        elif key == Qt.Key_Left:
            if ((rec1[0] - 50) > 0 and self.frog1.isEmpty(50,0,0)):
                self.frog1.move(rec1[0]-50, rec1[1],self.frog1.w, self.frog1.h, 'pictures/frogLeft.png')

        if key == Qt.Key_D:
            if((rec2[0] + 50) < (user32.GetSystemMetrics(78)-50) and self.frog2.isEmpty(50,0,1)):
                self.frog2.move(rec2[0] + 50, rec2[1], self.frog2.w, self.frog2.h, 'pictures/frogRight.png')
        elif key == Qt.Key_S:
            if ((rec2[1] + 83) < user32.GetSystemMetrics(79) - 50 and self.frog2.isEmpty(0,83,1)):
                self.frog2.move(rec2[0], rec2[1] + 83, self.frog2.w, self.frog2.h, 'pictures/frogDown.png')
        elif key == Qt.Key_W:
            if ((rec2[1] - 83) > 0 and self.frog2.isEmpty(0,83,0)):
                self.frog2.move(rec2[0], rec2[1] - 83, self.frog2.w, self.frog2.h, 'pictures/frogUp.png')
        elif key == Qt.Key_A:
            if ((rec2[0] - 50) > 0 and self.frog2.isEmpty(50,0,0)):
                self.frog2.move(rec2[0] - 50, rec2[1], self.frog2.w, self.frog2.h, 'pictures/frogLeft.png')

        if key == Qt.Key_Escape:
            self.car_move.carMovement.die()
            self.objectMovement.ObjectMovement.die()
            self.refresh.die()
            self.car_move.vremeSignal.die()
            self.objectMovement.vremeSignal.die()
            self.suprise.supriseSign.die()
            sys.exit()

    def closeEvent(self, event):
        self.key_notifier.die()

    # **************************
    def move_obj(self):
        Move_Obj.moveobj(self)
    # **************************

class Refresh(QObject):

    refreshSignal = pyqtSignal()

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
            self.refreshSignal.emit()
            time.sleep(0.05)