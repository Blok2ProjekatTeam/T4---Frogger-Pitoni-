import sys
from Config import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import ctypes
user32 = ctypes.windll.user32

class Rectangle(QWidget):

    allRectangles = {}

    def __init__(self,left,top,width,hight,type):
        super().__init__()
        self.x = left
        self.y = top
        self.w = width
        self.h = hight
        self.type = type
        self.speed = 0
        self.label1 = QLabel(Config.window)
        self.label2 = QLabel(Config.window)
        self.label3 = QLabel(Config.window)
        self.label4 = QLabel(Config.window)
        self.label5 = QLabel(Config.window)

        if(type == "frog"):
            self.id = Config.frogId + 1
            Config.frogId += 1
        elif(type == "wood"):
            self.id = Config.woodId + 1
            Config.woodId += 1
        elif(type == "car"):
            self.id = Config.carId + 1
            Config.carId += 1

        self.label = QLabel(Config.window)

        self.AddToLayer(type)

    def AddToLayer(self, typeName):
        if not self in self.allRectangles.items():
            if typeName in self.allRectangles.keys():
                self.allRectangles[typeName].append(self)
            else:
                self.allRectangles[typeName] = [self]

    def move(self, left,top, right,bottom,pix):
        self.x = left
        self.y = top
        self.w = right
        self.h = bottom
        self.labelSet(pix)

    def checkAllIntersects(self,x,y,option):
        if (option == 1):
            x = self.x + x
            y = self.y + y
        elif (option == 0):
            x = self.x - x
            y = self.y - y

        left = x
        right = x + self.w
        top = y
        bottom = y + self.h

        for checkForLayer in self.allRectangles.keys():
            if(checkForLayer != "frog"):
                for obj in self.allRectangles[checkForLayer]:
                    oleft, otop, oright, obottom = obj.GetSide()
                    if not (
                        left >= oright or
                        right <= oleft or
                        top >= obottom or
                        bottom <= otop):
                        return False

        return True

    def intersectsCars(self):
        left, top, right, bottom = self.GetSide()
        for checkForLayer in self.allRectangles.keys():
            if(checkForLayer == "car"):
                for obj in self.allRectangles[checkForLayer]:
                    oleft, otop, oright, obottom = obj.GetSide()
                    if not (
                        left >= oright or
                        right <= oleft or
                        top >= obottom or
                        bottom <= otop):
                        return False

        return True

    def intersectsFly(self):
        left, top, right, bottom = self.GetSide()
        for checkForLayer in self.allRectangles.keys():
            if (checkForLayer == "suprise"):
                for obj in self.allRectangles[checkForLayer]:
                    oleft, otop, oright, obottom = obj.GetSide()
                    if not (
                                            left >= oright or
                                            right <= oleft or
                                        top >= obottom or
                                    bottom <= otop):
                        return False

        return True

    def intersectsWood(self):
        left, top, right, bottom = self.GetSide()
        for checkForLayer in self.allRectangles.keys():
            if (checkForLayer == "wood"):
                for obj in self.allRectangles[checkForLayer]:
                    oleft, otop, oright, obottom = obj.GetSide()
                    if not (
                        left >= oright or
                        right <= oleft or
                        top >= obottom or
                        bottom <= otop):
                        self.attachWood(obj)
                        return False
            if (checkForLayer == "turtle"):
                for obj in self.allRectangles[checkForLayer]:
                    oleft, otop, oright, obottom = obj.GetSide()
                    if not (
                        left >= oright or
                        right <= oleft or
                        top >= obottom or
                        bottom <= otop):
                        self.attachTurtle(obj)
                        return False

        return True

    def attachWood(self, obj):
        self.move(self.x + Config.attachSpeedWood, self.y, self.w, self.h, 'pictures/frog1.png')

    def attachTurtle(self, obj):
        self.move(self.x + -Config.attachSpeedTurtle, self.y, self.w, self.h, 'pictures/frog1.png')

    def isEmpty(self,x,y,option):
        if(option == 1):
            x = self.x + x
            y = self.y + y
        elif(option == 0):
            x = self.x - x
            y = self.y - y

        left = x
        right = x + self.w
        top = y
        bottom = y + self.h
        brojac = -1
        for other in self.allRectangles[self.type]:
            brojac += 1
            if(brojac != self.id):
                oleft, otop, oright, obottom = other.GetSide()
                if not (left >= oright or right <= oleft or top >= obottom or bottom <= otop):
                    return False
        return True

    def labelSet(self, pix):
        self.pix1 = QPixmap(pix)
        self.label.setPixmap(self.pix1)
        self.label.setGeometry(self.x, self.y, self.w, self.h)
        self.label.show()

    def GetSide(self):
        left = self.x
        right = self.x + self.w
        top = self.y
        bottom = self.y + self.h
        return(left, top, right, bottom)

    def GetSize(self):
        return(self.x, self.y, self.w, self.h)

    def GetPosition(self):
        return(self.x,self.y)

    def final(self):
        left, top, right, bottom = self.GetSide()
        if(top == 92):
            if(user32.GetSystemMetrics(78) - 1775 <= left and left <= user32.GetSystemMetrics(78) - 1685 and Config.flowerOne == True):
                Config.flowerOne = False
                self.pix1 = QPixmap('pictures/frog1Down.png')
                self.label1.setPixmap(self.pix1)
                self.label1.setGeometry(user32.GetSystemMetrics(78) - 1760, 17, self.w, self.h)
                self.label1.show()
                return True
            elif(user32.GetSystemMetrics(78) - 1390 <= left and left <= user32.GetSystemMetrics(78) - 1300 and Config.flowerTwo == True):
                Config.flowerTwo = False
                self.pix1 = QPixmap('pictures/frog1Down.png')
                self.label2.setPixmap(self.pix1)
                self.label2.setGeometry(user32.GetSystemMetrics(78) - 1380, 17, self.w, self.h)
                self.label2.show()
                return True
            elif (user32.GetSystemMetrics(78) - 1010 <= left and left <= user32.GetSystemMetrics(78) - 920 and Config.flowerThree == True):
                Config.flowerThree = False
                self.pix1 = QPixmap('pictures/frog1Down.png')
                self.label3.setPixmap(self.pix1)
                self.label3.setGeometry(user32.GetSystemMetrics(78) - 1000, 17, self.w, self.h)
                self.label3.show()
                return True
            elif (user32.GetSystemMetrics(78) - 625 <= left and left <= user32.GetSystemMetrics(78) - 535 and Config.flowerFour == True):
                Config.flowerFour = False
                self.pix1 = QPixmap('pictures/frog1Down.png')
                self.label4.setPixmap(self.pix1)
                self.label4.setGeometry(user32.GetSystemMetrics(78) - 610, 17, self.w, self.h)
                self.label4.show()
                return True
            elif (user32.GetSystemMetrics(78) - 245 <= left and left <= user32.GetSystemMetrics(78) - 150 and Config.flowerFive == True):
                Config.flowerFive = False
                self.pix1 = QPixmap('pictures/frog1Down.png')
                self.label5.setPixmap(self.pix1)
                self.label5.setGeometry(user32.GetSystemMetrics(78) - 230, 17, self.w, self.h)
                self.label5.show()
                return True
            elif (user32.GetSystemMetrics(78) - 1775 <= right and right <= user32.GetSystemMetrics(78) - 1685 and Config.flowerOne == True):
                Config.flowerOne = False
                self.pix1 = QPixmap('pictures/frog1Down.png')
                self.label1.setPixmap(self.pix1)
                self.label1.setGeometry(user32.GetSystemMetrics(78) - 1760, 17, self.w, self.h)
                self.label1.show()
                return True
            elif (user32.GetSystemMetrics(78) - 1390 <= right and right <= user32.GetSystemMetrics(78) - 1300 and Config.flowerTwo == True):
                Config.flowerTwo = False
                self.pix1 = QPixmap('pictures/frog1Down.png')
                self.label2.setPixmap(self.pix1)
                self.label2.setGeometry(user32.GetSystemMetrics(78) - 1380, 17, self.w, self.h)
                self.label2.show()
                return True
            elif (user32.GetSystemMetrics(78) - 1010 <= right and right <= user32.GetSystemMetrics(78) - 920 and Config.flowerThree == True):
                Config.flowerThree = False
                self.pix1 = QPixmap('pictures/frog1Down.png')
                self.label3.setPixmap(self.pix1)
                self.label3.setGeometry(user32.GetSystemMetrics(78) - 1000, 17, self.w, self.h)
                self.label3.show()
                return True
            elif (user32.GetSystemMetrics(78) - 625 <= right and right <= user32.GetSystemMetrics(78) - 535 and Config.flowerFour == True):
                Config.flowerFour = False
                self.pix1 = QPixmap('pictures/frog1Down.png')
                self.label4.setPixmap(self.pix1)
                self.label4.setGeometry(user32.GetSystemMetrics(78) - 610, 17, self.w, self.h)
                self.label4.show()
                return True
            elif (user32.GetSystemMetrics(78) - 245 <= right and right <= user32.GetSystemMetrics(78) - 150 and Config.flowerFive == True):
                Config.flowerFive = False
                self.pix1 = QPixmap('pictures/frog1Down.png')
                self.label5.setPixmap(self.pix1)
                self.label5.setGeometry(user32.GetSystemMetrics(78) - 230, 17, self.w, self.h)
                self.label5.show()
                return True

            return False
        else:
            return True

    def refresh(self):
        print(self.id)
        self.label1.setGeometry(user32.GetSystemMetrics(78) - 8000, 8000, self.w, self.h)
        self.label1.show()
        self.label2.setGeometry(user32.GetSystemMetrics(78) - 8000, 8000, self.w, self.h)
        self.label2.show()
        self.label3.setGeometry(user32.GetSystemMetrics(78) - 8000, 8000, self.w, self.h)
        self.label3.show()
        self.label4.setGeometry(user32.GetSystemMetrics(78) - 8000, 8000, self.w, self.h)
        self.label4.show()
        self.label5.setGeometry(user32.GetSystemMetrics(78) - 8000, 8000, self.w, self.h)
        self.label5.show()


