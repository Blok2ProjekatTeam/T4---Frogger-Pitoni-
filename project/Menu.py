from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from SimulateMove import *
from PyQt5.QtGui import QIcon

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__init_ui__()

    def __init_ui__(self):
        oImage = QImage("pictures/menuPicture.jpg")

        self.label = QLabel(self)

        self.left = 600
        self.top = 200
        self.width = 600
        self.height = 400

        palette = QPalette()
        sImage = oImage.scaled(QSize(600, 400))
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon('pictures/icon.png'))

        self.setFixedSize(self.size())

        self.setWindowTitle("Frogger")

        self.button1 = QPushButton('PLAY', self)
        self.button1.resize(143, 43)
        self.button1.move(77, 186)
        self.button1.clicked.connect(self.play)
        self.button1.show()

        self.button2 = QPushButton('TOURNAMENT', self)
        self.button2.resize(143, 43)
        self.button2.move(77, 229)
        self.button2.clicked.connect(self.tournament)
        self.button2.show()

        self.button3 = QPushButton('CONTROLS', self)
        self.button3.resize(143, 44)
        self.button3.move(77, 272)
        self.button3.clicked.connect(self.ccontrols)
        self.button3.show()

        self.button4 = QPushButton('QUIT', self)
        self.button4.resize(143, 43)
        self.button4.move(77, 316)
        self.button4.clicked.connect(self.quit)
        self.button4.show()

        self.button5 = QPushButton('BACK', self)
        self.button5.resize(143, 43)
        self.button5.move(450, 50)
        self.button5.clicked.connect(self.back)
        self.button5.hide()

        self.show()

    def play(self):
        self.play = SimMoveDemo()
        self.play.show()
        self.close()

    def tournament(self):
        self.two = SimMoveDemo()
        self.two.show()

    def ccontrols(self):
        self.button1.hide()
        self.button2.hide()
        self.button3.hide()
        self.button4.hide()
        self.button5.show()
        self.controls()

    def controls(self):
        self.setWindowTitle("Frogger - controls")
        oImage1 = QImage("pictures/controls.jpg")

        self.label = QLabel(self)

        self.left = 600
        self.top = 200
        self.width = 600
        self.height = 400

        palette1 = QPalette()
        sImage1 = oImage1.scaled(QSize(600, 400))
        palette1.setBrush(10, QBrush(sImage1))  # 10 = Windowrole
        self.setPalette(palette1)


    def back(self):
        self.button1.show()
        self.button2.show()
        self.button3.show()
        self.button4.show()
        self.button5.hide()
        self.__init_ui__()

    def quit(self):
        sys.exit()
        self.close()