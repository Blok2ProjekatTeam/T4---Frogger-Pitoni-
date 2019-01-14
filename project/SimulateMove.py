import sys
from ObjectMovement import *
from Car import *
from KeyNotifier import *
import ctypes
from Rectangle import *
from Config import *
from Score import *
from PyQt5 import QtGui
from Suprise import *
from multiprocessing import Queue, Process
from Lives import funkcija

user32 = ctypes.windll.user32

class SimMoveDemo(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        Config.window = self
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)

        self.font = QtGui.QFont()
        self.font.setFamily("Forte")
        self.font.setPointSize(30)
        self.levelLabel = QLabel(self)
        self.scoreLabel1 = QLabel(self)
        self.scoreLabel2 = QLabel(self)
        self.liveLabel1 = QLabel(self)
        self.liveLabel2 = QLabel(self)
        self.levelLabel = QLabel(self)
        self.modeLabel = QLabel(self)
        self.gameOverLabel = QLabel(self) ############################################################################################################

        self.setGeometry(100, 100, 646, 559)
        self.setFixedSize(self.size())
        self.showFullScreen()

        oImage = QImage("pictures/backGround.png")
        sImage = oImage.scaled(QSize(user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        # Car Move
        # self.car_move = Car(self)
        # self.car_move.initPosition()
        # self.car_move.carMovement = CarMovement()
        # self.car_move.carMovement.carMovementSignal.connect(self.car_move._update_position)
        # self.car_move.vremeSignal = VremeSignal()
        # self.car_move.vremeSignal.timeSignal.connect(self.car_move.change_weather)
        # self.car_move.vremeSignal.start()
        # self.car_move.carMovement.start()
        # self.car_move.__init__(self)

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

        self.suprise = Suprise(self)
        self.suprise.supriseSign = SupriseSignal()
        self.suprise.supriseSign.supriseSig.connect(self.suprise.initPosition)
        self.suprise.supriseSign.start()

        self.queue = Queue()
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.process = Process(target=funkcija, args=[self.queue, self.queue1, self.queue2])
        self.process.start()

      #  self.car_move = CarMove(self)

        self.frog1 = Rectangle(user32.GetSystemMetrics(78) - 750, user32.GetSystemMetrics(79) - 75, 70, 60, "frog")
        self.frog2 = Rectangle(user32.GetSystemMetrics(78) - 1380, user32.GetSystemMetrics(79) - 75, 70, 60, "frog")

        self.label = QLabel('', self)  # test, if it's really backgroundimage
        self.label.setGeometry(50, 50, 200, 50)

        self.__init_ui__()

        self.key_notifier = KeyNotifier()

        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

    def __init_ui__(self):
        self.frog1.labelSet('pictures/frog1.png')

        self.frog2.labelSet('pictures/frog1.png')

        self.score1 = Score()
        self.score2 = Score()

        self.scoreLabel1.setFont(self.font)
        self.scoreLabel1.setText('Score: ' + str(self.score1.score))
        self.scoreLabel1.setGeometry(1450, -10, 500, 100)

        self.scoreLabel2.setFont(self.font)
        self.scoreLabel2.setText('Score: ' + str(self.score2.score))
        self.scoreLabel2.setGeometry(280, -10, 500, 100)

        self.liveLabel1.setFont(self.font)
        self.liveLabel1.setText('Lives: ' + str(self.score1.lives))
        self.liveLabel1.setGeometry(1770, -10, 500, 100)

        self.liveLabel2.setFont(self.font)
        self.liveLabel2.setText('Lives: ' + str(self.score2.lives))
        self.liveLabel2.setGeometry(10, -10, 500, 100)

        self.levelLabel.setFont(self.font)
        self.levelLabel.setText('Level: ' + str(self.score1.level))
        self.levelLabel.setGeometry(670, -10, 500, 100)

        self.modeLabel.setFont(self.font)
        self.modeLabel.setText('Mode: ')
        self.modeLabel.setGeometry(1020, -10, 500, 100)

        self.setWindowTitle('Frogger')
        self.show()

    def keyPressEvent(self, event):
        if not event.isAutoRepeat():
            self.key_notifier.add_key(event.key())

    def __check_position__(self):

        if(not Config.flowerOne and not Config.flowerTwo and not Config.flowerThree and not Config.flowerFour and not Config.flowerFive):
            self.frog1.refresh()
            self.frog2.refresh()
            Config.flowerOne = True
            Config.flowerTwo = True
            Config.flowerThree = True
            Config.flowerFour = True
            Config.flowerFive = True
            self.frog1.x = user32.GetSystemMetrics(78) - 750
            self.frog1.y = user32.GetSystemMetrics(79) - 75
            self.frog1.labelSet('pictures/frog1.png')
            self.frog2.x = user32.GetSystemMetrics(78) - 1380
            self.frog2.y = user32.GetSystemMetrics(79) - 75
            self.frog2.labelSet('pictures/frog1.png')
            ############################################################################################################
            if(self.score1.lives != 0):
                self.score1.lives = 3
                self.liveLabel1.setText('Lives: ' + str(self.score1.lives))
                self.liveLabel1.setGeometry(1770, -10, 500, 100)
            if(self.score2.lives != 0):
                self.score2.lives = 3
                self.liveLabel2.setFont(self.font)
                self.liveLabel2.setText('Lives: ' + str(self.score2.lives))
                self.liveLabel2.setGeometry(10, -10, 500, 100)
            ############################################################################################################
            self.score1.level += 1
            self.score2.level += 1
            self.levelLabel.setFont(self.font)
            self.levelLabel.setText('Level: ' + str(self.score1.level))
            self.levelLabel.setGeometry(670, -10, 500, 100)
            self.score1.y = 1005
            self.score2.y = 1005
            Config.speedcar += self.score1.level
            Config.speedfireman += self.score1.level
            Config.speedyellow += self.score1.level
            Config.speedkamion += self.score1.level
            Config.speedgreen += self.score1.level
            Config.speedwood += self.score1.level
            Config.attachSpeedTurtle += self.score1.level
            Config.attachSpeedWood += self.score1.level
            Config.speedturtle += self.score1.level
        ############################################################################################################
        if (not self.queue.empty()):
            x = self.queue.get()
            if (x == 1):
                self.font.setPointSize(80)
                self.gameOverLabel.setFont(self.font)
                if(self.score1.score > self.score2.score):
                    self.gameOverLabel.setText('GAME OVER! \nPlayer 1 wins! \nPress ESC to exit. ')
                    self.gameOverLabel.setGeometry(500, 280, 1000, 500)
                elif(self.score1.score < self.score2.score):
                    self.gameOverLabel.setText('GAME OVER! \nPlayer 2 wins! \nPress ESC to exit. ')
                    self.gameOverLabel.setGeometry(500, 280, 1000, 500)
                else:
                    self.gameOverLabel.setText('GAME OVER! \nDraw! \nPress ESC to exit. ')
                    self.gameOverLabel.setGeometry(500, 280, 1000, 500)
        ############################################################################################################
        self.font.setPointSize(30)
        if(Config.vreme == "snow"):
            self.modeLabel.setFont(self.font)
            self.modeLabel.setText('Mode: Snow')
            self.modeLabel.setGeometry(1020, -10, 500, 100)
        elif (Config.vreme == "rain"):
            self.modeLabel.setFont(self.font)
            self.modeLabel.setText('Mode: Rain')
            self.modeLabel.setGeometry(1020, -10, 500, 100)
        elif (Config.vreme == "normal"):
            self.modeLabel.setFont(self.font)
            self.modeLabel.setText('Mode: Normal')
            self.modeLabel.setGeometry(1020, -10, 500, 100)

        ############################################################################################################
        if (self.score1.lives != 0):
            self.frog1.labelSet('pictures/frog1.png')
        elif (self.score1.lives == 0):
            self.frog1.x = user32.GetSystemMetrics(78) - 8000
            self.frog1.y = user32.GetSystemMetrics(79) - 8000
            self.frog1.labelSet('pictures/frog1.png')

        if (self.score2.lives != 0):
            self.frog2.labelSet('pictures/frog1.png')
        elif (self.score2.lives == 0):
            self.frog2.x = user32.GetSystemMetrics(78) - 8000
            self.frog2.y = user32.GetSystemMetrics(79) - 8000
            self.frog2.labelSet('pictures/frog1.png')
        ############################################################################################################
        if (self.frog1.y > 498):
            if (not self.frog1.intersectsCars()):
                if (self.score1.lives == 1):
                    self.frog1.labelSet('pictures/skull.png')
                    self.score1.lives -= 1
                    self.queue1.put(0)
                    self.liveLabel1.setFont(self.font)
                    self.liveLabel1.setText('Lives: ' + str(self.score1.lives))
                    self.liveLabel1.setGeometry(1770, -10, 500, 100)
                else:
                    self.frog1.x = user32.GetSystemMetrics(78) - 750
                    self.frog1.y = user32.GetSystemMetrics(79) - 75
                    self.frog1.labelSet('pictures/frog1.png')
                    self.score1.lives -= 1
                    self.liveLabel1.setFont(self.font)
                    self.liveLabel1.setText('Lives: ' + str(self.score1.lives))
                    self.liveLabel1.setGeometry(1770, -10, 500, 100)

            if (not self.frog1.intersectsFly()):
                if(self.suprise.hideFly() == 0):
                    self.score1.lives += 1
                    self.liveLabel1.setFont(self.font)
                    self.liveLabel1.setText('Lives: ' + str(self.score1.lives))
                    self.liveLabel1.setGeometry(1770, -10, 500, 100)
                else:
                    self.score1.lives -= 1
                    self.liveLabel1.setFont(self.font)
                    self.liveLabel1.setText('Lives: ' + str(self.score1.lives))
                    self.liveLabel1.setGeometry(1770, -10, 500, 100)

        elif(92 <= self.frog1.y <= 498):
            if (self.frog1.intersectsWood()):
                if (self.score1.lives == 1):
                    self.frog1.labelSet('pictures/skull.png')
                    self.score1.lives -= 1
                    self.queue1.put(0)
                    self.liveLabel1.setFont(self.font)
                    self.liveLabel1.setText('Lives: ' + str(self.score1.lives))
                    self.liveLabel1.setGeometry(1770, -10, 500, 100)
                else:
                    self.frog1.x = user32.GetSystemMetrics(78) - 750
                    self.frog1.y = user32.GetSystemMetrics(79) - 75
                    self.frog1.labelSet('pictures/frog1.png')
                    self.score1.lives -= 1
                    self.liveLabel1.setFont(self.font)
                    self.liveLabel1.setText('Lives: ' + str(self.score1.lives))
                    self.liveLabel1.setGeometry(1770, -10, 500, 100)
        elif(self.score1.lives > 0):
            self.frog1.x = user32.GetSystemMetrics(78) - 750
            self.frog1.y = user32.GetSystemMetrics(79) - 75
            self.frog1.labelSet('pictures/frog1.png')
            self.score1.y = 1005

        if (self.frog2.y > 498):
            if (not self.frog2.intersectsCars()):
                if (self.score2.lives == 1):
                    self.frog2.labelSet('pictures/skull.png')
                    self.score2.lives -= 1
                    self.queue2.put(0)
                    self.liveLabel2.setFont(self.font)
                    self.liveLabel2.setText('Lives: ' + str(self.score2.lives))
                    self.liveLabel2.setGeometry(10, -10, 500, 100)
                else:
                    self.frog2.x = user32.GetSystemMetrics(78) - 1380
                    self.frog2.y = user32.GetSystemMetrics(79) - 75
                    self.frog2.labelSet('pictures/frog1.png')
                    self.score2.lives -= 1
                    self.liveLabel2.setFont(self.font)
                    self.liveLabel2.setText('Lives: ' + str(self.score2.lives))
                    self.liveLabel2.setGeometry(10, -10, 500, 100)

            if (not self.frog2.intersectsFly()):
                if(self.suprise.hideFly() == 0):
                    self.score2.lives += 1
                    self.liveLabel2.setFont(self.font)
                    self.liveLabel2.setText('Lives: ' + str(self.score2.lives))
                    self.liveLabel2.setGeometry(10, -10, 500, 100)
                else:
                    self.score2.lives -= 1
                    self.liveLabel2.setFont(self.font)
                    self.liveLabel2.setText('Lives: ' + str(self.score2.lives))
                    self.liveLabel2.setGeometry(10, -10, 500, 100)

        elif(92 <= self.frog2.y <= 498):
            if (self.frog2.intersectsWood()):
                if (self.score2.lives == 1):
                    self.frog2.labelSet('pictures/skull.png')
                    self.score2.lives -= 1
                    self.queue2.put(0)
                    self.liveLabel2.setFont(self.font)
                    self.liveLabel2.setText('Lives: ' + str(self.score2.lives))
                    self.liveLabel2.setGeometry(10, -10, 500, 100)
                else:
                    self.frog2.x = user32.GetSystemMetrics(78) - 1380
                    self.frog2.y = user32.GetSystemMetrics(79) - 75
                    self.frog2.labelSet('pictures/frog1.png')
                    self.score2.lives -= 1
                    self.liveLabel2.setFont(self.font)
                    self.liveLabel2.setText('Lives: ' + str(self.score2.lives))
                    self.liveLabel2.setGeometry(10, -10, 500, 100)
        elif(self.score2.lives > 0):
            self.frog2.x = user32.GetSystemMetrics(78) - 1380
            self.frog2.y = user32.GetSystemMetrics(79) - 75
            self.frog2.labelSet('pictures/frog1.png')
            self.score2.y = 1005

    def __update_position__(self, key):
        rec1 = self.frog1.GetPosition()
        rec2 = self.frog2.GetPosition()

        if key == Qt.Key_Right:
            if((rec1[0] + 50) < (user32.GetSystemMetrics(78)-50) and self.frog1.isEmpty(50,0,1)):
                self.frog1.move(rec1[0] + Config.speedFrog, rec1[1], self.frog1.w, self.frog1.h, 'pictures/frogRight.png')
        elif key == Qt.Key_Down:
            if ((rec1[1] + 83) < user32.GetSystemMetrics(79) - 50 and self.frog1.isEmpty(0,83,1)):
                self.frog1.move(rec1[0], rec1[1] + 83,self.frog1.w, self.frog1.h,'pictures/frogDown.png')
        elif key == Qt.Key_Up:
            if ((rec1[1] - 83) > 0 and self.frog1.isEmpty(0,83,0) and self.frog1.final()):
                self.frog1.move(rec1[0], rec1[1] -83,self.frog1.w, self.frog1.h, 'pictures/frogUp.png')
                if(self.frog1.y < self.score1.y):
                    self.score1.y = self.frog1.y
                    if(self.score1.y == 9):
                        self.score1.score += 100 * self.score1.level
                    else:
                        self.score1.score += 10
                    self.scoreLabel1.setFont(self.font)
                    self.scoreLabel1.setText('Score: ' + str(self.score1.score))
                    self.scoreLabel1.setGeometry(1420, -10, 500, 100)
        elif key == Qt.Key_Left:
            if ((rec1[0] - 50) > 0 and self.frog1.isEmpty(50,0,0)):
                self.frog1.move(rec1[0]- Config.speedFrog, rec1[1],self.frog1.w, self.frog1.h, 'pictures/frogLeft.png')

        if key == Qt.Key_D:
            if((rec2[0] + 50) < (user32.GetSystemMetrics(78)-50) and self.frog2.isEmpty(50,0,1)):
                self.frog2.move(rec2[0] + Config.speedFrog, rec2[1], self.frog2.w, self.frog2.h, 'pictures/frogRight.png')
        elif key == Qt.Key_S:
            if ((rec2[1] + 83) < user32.GetSystemMetrics(79) - 50 and self.frog2.isEmpty(0,83,1)):
                self.frog2.move(rec2[0], rec2[1] + 83, self.frog2.w, self.frog2.h, 'pictures/frogDown.png')
        elif key == Qt.Key_W:
            if ((rec2[1] - 83) > 0 and self.frog2.isEmpty(0,83,0) and self.frog2.final()):
                self.frog2.move(rec2[0], rec2[1] - 83, self.frog2.w, self.frog2.h, 'pictures/frogUp.png')
                if (self.frog2.y < self.score2.y):
                    self.score2.y = self.frog2.y
                    if (self.score2.y == 9):
                        self.score2.score += 100 * self.score2.level
                    else:
                        self.score2.score += 10
                    self.scoreLabel2.setFont(self.font)
                    self.scoreLabel2.setText('Score: ' + str(self.score2.score))
                    self.scoreLabel2.setGeometry(280, -10, 500, 100)
        elif key == Qt.Key_A:
            if ((rec2[0] - 50) > 0 and self.frog2.isEmpty(50,0,0)):
                self.frog2.move(rec2[0] - Config.speedFrog, rec2[1], self.frog2.w, self.frog2.h, 'pictures/frogLeft.png')

        if key == Qt.Key_Escape:
            #self.car_move.carMovement.die()
            self.objectMovement.ObjectMovement.die()
            self.refresh.die()
            #self.car_move.vremeSignal.die()
            self.objectMovement.vremeSignal.die()
            self.suprise.supriseSign.die()
            self.process.terminate()
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