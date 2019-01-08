from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from SimulateMove import *

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

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

        self.__init_ui__()

    def __init_ui__(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setWindowIcon(QtGui.QIcon('pictures/icon.png'))

        self.setWindowTitle("Frogger")

        button1 = QPushButton('PLAY', self)
        button1.resize(143, 43)
        button1.move(77, 186)
        button1.clicked.connect(self.play)

        button2 = QPushButton('TOURNAMENT', self)
        button2.resize(143, 43)
        button2.move(77, 229)
        button2.clicked.connect(self.tournament)

        button3 = QPushButton('CONTROLS', self)
        button3.resize(143, 44)
        button3.move(77, 272)

        button3.clicked.connect(self.controls)

        button4 = QPushButton('QUIT', self)
        button4.resize(143, 43)
        button4.move(77, 316)
        button4.clicked.connect(self.quit)

        self.show()

    def play(self):
        self.play = SimMoveDemo()
        self.play.show()
        self.close()

    def tournament(self):
        self.two = SimMoveDemo()
        self.two.show()

    def controls(self):
        self.close()

    def quit(self):
        sys.exit()
        self.close()