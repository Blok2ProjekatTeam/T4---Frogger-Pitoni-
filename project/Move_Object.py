import ctypes
from objectMovement import ObjectMovement

import time

user32 = ctypes.windll.user32

class Move_Obj:
    def moveobj(self):
        # kretanje debla
        rec3 = self.woodLarge.geometry()
        if (rec3.x() < -400):  # -400
            self.woodLarge.setGeometry(rec3.x() + 1800, rec3.y(), rec3.width(), rec3.height())
        else:
            self.woodLarge.setGeometry(rec3.x() - 5, rec3.y(), rec3.width(), rec3.height())

        rec30 = self.woodLarge2.geometry()
        if (rec30.x() < -400):  # -400
            self.woodLarge2.setGeometry(rec30.x() + 1800, rec30.y(), rec30.width(), rec30.height())
        else:
            self.woodLarge2.setGeometry(rec30.x() - 5, rec30.y(), rec30.width(), rec30.height())

        rec31 = self.woodLarge3.geometry()
        if (rec31.x() < -400):  # -400
            self.woodLarge3.setGeometry(rec31.x() + 1800, rec31.y(), rec31.width(), rec31.height())
        else:
            self.woodLarge3.setGeometry(rec31.x() - 5, rec31.y(), rec31.width(), rec31.height())

        rec4 = self.woodMiddle.geometry()
        if (rec4.x() < -300):
            self.woodMiddle.setGeometry(rec4.x() + 1650, rec4.y(), rec4.width(), rec4.height())
        else:
            self.woodMiddle.setGeometry(rec4.x() - 5, rec4.y(), rec4.width(), rec4.height())

        rec40 = self.woodMiddle2.geometry()
        if (rec40.x() < -300):
            self.woodMiddle2.setGeometry(rec40.x() + 1650, rec40.y(), rec40.width(), rec40.height())
        else:
            self.woodMiddle2.setGeometry(rec40.x() - 5, rec40.y(), rec40.width(), rec40.height())

        rec41 = self.woodMiddle3.geometry()
        if (rec41.x() < -300):
            self.woodMiddle3.setGeometry(rec41.x() + 1650, rec41.y(), rec41.width(), rec41.height())
        else:
            self.woodMiddle3.setGeometry(rec41.x() - 5, rec41.y(), rec41.width(), rec41.height())

        rec42 = self.woodMiddle4.geometry()
        if (rec42.x() < -300):
            self.woodMiddle4.setGeometry(rec42.x() + 1650, rec42.y(), rec42.width(), rec42.height())
        else:
            self.woodMiddle4.setGeometry(rec42.x() - 5, rec42.y(), rec42.width(), rec42.height())

        rec5 = self.woodSmall.geometry()
        if (rec5.x() < -200):
            self.woodSmall.setGeometry(1400, rec5.y(), rec5.width(), rec5.height())
        else:
            self.woodSmall.setGeometry(rec5.x() - 5, rec5.y(), rec5.width(), rec5.height())

        rec50 = self.woodSmall2.geometry()
        if (rec50.x() < -200):
            self.woodSmall2.setGeometry(1400, rec50.y(), rec50.width(), rec50.height())
        else:
            self.woodSmall2.setGeometry(rec50.x() - 5, rec50.y(), rec50.width(), rec50.height())

        rec51 = self.woodSmall3.geometry()
        if (rec51.x() < -200):
            self.woodSmall3.setGeometry(1400, rec51.y(), rec51.width(), rec51.height())
        else:
            self.woodSmall3.setGeometry(rec51.x() - 5, rec51.y(), rec51.width(), rec51.height())

        rec52 = self.woodSmall4.geometry()
        if (rec52.x() < -200):
            self.woodSmall4.setGeometry(1400, rec52.y(), rec52.width(), rec52.height())
        else:
            self.woodSmall4.setGeometry(rec52.x() - 5, rec52.y(), rec52.width(), rec52.height())

        rec53 = self.woodSmall5.geometry()
        if (rec53.x() < -200):
            self.woodSmall5.setGeometry(1400, rec53.y(), rec53.width(), rec53.height())
        else:
            self.woodSmall5.setGeometry(rec53.x() - 5, rec53.y(), rec53.width(), rec53.height())

        # prebacivanje turtle1 u turtle2, gornje kornjace
        rec6 = self.turtle11.geometry()
        if (rec6.x() > 300):
            self.turtle21.setGeometry(rec6.x(), rec6.y(), rec6.width(), rec6.height())
            self.turtle11.setGeometry(-525, rec6.y(), rec6.width(), rec6.height())
        else:
            self.turtle11.setGeometry(rec6.x() + 5, rec6.y(), rec6.width(), rec6.height())

        rec7 = self.turtle12.geometry()
        if (rec7.x() > 375):
            self.turtle22.setGeometry(rec7.x(), rec7.y(), rec7.width(), rec7.height())
            self.turtle12.setGeometry(-450, rec7.y(), rec7.width(), rec7.height())
        else:
            self.turtle12.setGeometry(rec7.x() + 5, rec7.y(), rec7.width(), rec7.height())

        rec8 = self.turtle13.geometry()
        if (rec8.x() > 450):
            self.turtle23.setGeometry(rec8.x(), rec8.y(), rec8.width(), rec8.height())
            self.turtle13.setGeometry(-375, rec8.y(), rec8.width(), rec8.height())
        else:
            self.turtle13.setGeometry(rec8.x() + 5, rec8.y(), rec8.width(), rec8.height())

        # ubacivanje turtle1 drugi put gore
        rec20 = self.turtle17.geometry()
        if (rec20.x() > user32.GetSystemMetrics(0)):
            self.turtle17.setGeometry(-300, rec20.y(), rec20.width(), rec20.height())
        else:
            self.turtle17.setGeometry(rec20.x() + 5, rec20.y(), rec20.width(), rec20.height())

        rec21 = self.turtle18.geometry()
        if (rec21.x() > user32.GetSystemMetrics(0)):
            self.turtle18.setGeometry(-300, rec21.y(), rec21.width(), rec21.height())
        else:
            self.turtle18.setGeometry(rec21.x() + 5, rec21.y(), rec21.width(), rec21.height())

        rec22 = self.turtle19.geometry()
        if (rec22.x() > user32.GetSystemMetrics(0)):
            self.turtle19.setGeometry(-300, rec22.y(), rec22.width(), rec22.height())
        else:
            self.turtle19.setGeometry(rec22.x() + 5, rec22.y(), rec22.width(), rec22.height())

        # prebacivanje iz turtle2 u turtle3
        rec12 = self.turtle21.geometry()
        if (rec12.x() > 600):
            self.turtle31.setGeometry(rec12.x(), rec12.y(), rec12.width(), rec12.height())
            self.turtle21.setGeometry(-1600, rec12.y(), rec12.width(), rec12.height())
        else:
            self.turtle21.setGeometry(rec12.x() + 5, rec12.y(), rec12.width(), rec12.height())
        rec13 = self.turtle22.geometry()
        if (rec13.x() > 675):
            self.turtle32.setGeometry(rec13.x(), rec13.y(), rec13.width(), rec13.height())
            self.turtle22.setGeometry(-1675, rec13.y(), rec13.width(), rec13.height())
        else:
            self.turtle22.setGeometry(rec13.x() + 5, rec13.y(), rec13.width(), rec13.height())

        rec14 = self.turtle23.geometry()
        if (rec14.x() > 750):
            self.turtle33.setGeometry(rec14.x(), rec14.y(), rec14.width(), rec14.height())
            self.turtle23.setGeometry(-1750, rec14.y(), rec14.width(), rec14.height())
        else:
            self.turtle23.setGeometry(rec14.x() + 5, rec14.y(), rec14.width(), rec14.height())

        # kretanje turtle3
        rec9 = self.turtle31.geometry()
        if (rec9.x() > 900):
            self.turtle31.setGeometry(1600, rec9.y(), rec9.width(), rec9.height())
        else:
            self.turtle31.setGeometry(rec9.x() + 5, rec9.y(), rec9.width(), rec9.height())
        rec10 = self.turtle32.geometry()
        if (rec10.x() > 975):
            self.turtle32.setGeometry(1675, rec10.y(), rec10.width(), rec10.height())
        else:
            self.turtle32.setGeometry(rec10.x() + 5, rec10.y(), rec10.width(), rec10.height())
        rec11 = self.turtle33.geometry()
        if (rec11.x() > 1050):
            self.turtle33.setGeometry(1750, rec11.y(), rec11.width(), rec11.height())
        else:
            self.turtle33.setGeometry(rec11.x() + 5, rec11.y(), rec11.width(), rec11.height())

        # donje kornjace ***************************************************************************************
        # prebacivanje turtle1 u turtle2, donje kornjace
        rec6 = self.turtle14.geometry()
        if (rec6.x() > 300):
            self.turtle24.setGeometry(rec6.x(), rec6.y(), rec6.width(), rec6.height())
            self.turtle14.setGeometry(-525, rec6.y(), rec6.width(), rec6.height())
        else:
            self.turtle14.setGeometry(rec6.x() + 5, rec6.y(), rec6.width(), rec6.height())

        rec7 = self.turtle15.geometry()
        if (rec7.x() > 375):
            self.turtle25.setGeometry(rec7.x(), rec7.y(), rec7.width(), rec7.height())
            self.turtle15.setGeometry(-450, rec7.y(), rec7.width(), rec7.height())
        else:
            self.turtle15.setGeometry(rec7.x() + 5, rec7.y(), rec7.width(), rec7.height())

        rec8 = self.turtle16.geometry()
        if (rec8.x() > 450):
            self.turtle26.setGeometry(rec8.x(), rec8.y(), rec8.width(), rec8.height())
            self.turtle16.setGeometry(-375, rec8.y(), rec8.width(), rec8.height())
        else:
            self.turtle16.setGeometry(rec8.x() + 5, rec8.y(), rec8.width(), rec8.height())

        # prebacivanje iz turtle2 u turtle3, donje kornjace
        rec12 = self.turtle24.geometry()
        if (rec12.x() > 600):
            self.turtle34.setGeometry(rec12.x(), rec12.y(), rec12.width(), rec12.height())
            self.turtle24.setGeometry(-1600, rec12.y(), rec12.width(), rec12.height())
        else:
            self.turtle24.setGeometry(rec12.x() + 5, rec12.y(), rec12.width(), rec12.height())

        rec13 = self.turtle25.geometry()
        if (rec13.x() > 675):
            self.turtle35.setGeometry(rec13.x(), rec13.y(), rec13.width(), rec13.height())
            self.turtle25.setGeometry(-1675, rec13.y(), rec13.width(), rec13.height())
        else:
            self.turtle25.setGeometry(rec13.x() + 5, rec13.y(), rec13.width(), rec13.height())

        rec14 = self.turtle26.geometry()
        if (rec14.x() > 750):
            self.turtle36.setGeometry(rec14.x(), rec14.y(), rec14.width(), rec14.height())
            self.turtle26.setGeometry(-1750, rec14.y(), rec14.width(), rec14.height())
        else:
            self.turtle26.setGeometry(rec14.x() + 5, rec14.y(), rec14.width(), rec14.height())

        # kretanje turtle3
        rec9 = self.turtle34.geometry()
        if (rec9.x() > 900):
            self.turtle34.setGeometry(1600, rec9.y(), rec9.width(), rec9.height())
        else:
            self.turtle34.setGeometry(rec9.x() + 5, rec9.y(), rec9.width(), rec9.height())

        rec10 = self.turtle35.geometry()
        if (rec10.x() > 975):
            self.turtle35.setGeometry(1675, rec10.y(), rec10.width(), rec10.height())
        else:
            self.turtle35.setGeometry(rec10.x() + 5, rec10.y(), rec10.width(), rec10.height())

        rec11 = self.turtle36.geometry()
        if (rec11.x() > 1050):
            self.turtle36.setGeometry(1750, rec11.y(), rec11.width(), rec11.height())
        else:
            self.turtle36.setGeometry(rec11.x() + 5, rec11.y(), rec11.width(), rec11.height())

        # ubacivanje turtle1 drugi put dole
        rec20 = self.turtle110.geometry()
        if (rec20.x() > user32.GetSystemMetrics(0)):
            self.turtle110.setGeometry(-300, rec20.y(), rec20.width(), rec20.height())
        else:
            self.turtle110.setGeometry(rec20.x() + 5, rec20.y(), rec20.width(), rec20.height())

        rec21 = self.turtle111.geometry()
        if (rec21.x() > user32.GetSystemMetrics(0)):
            self.turtle111.setGeometry(-300, rec21.y(), rec21.width(), rec21.height())
        else:
            self.turtle111.setGeometry(rec21.x() + 5, rec21.y(), rec21.width(), rec21.height())

        rec22 = self.turtle112.geometry()
        if (rec22.x() > user32.GetSystemMetrics(0)):
            self.turtle112.setGeometry(-300, rec22.y(), rec22.width(), rec22.height())
        else:
            self.turtle112.setGeometry(rec22.x() + 5, rec22.y(), rec22.width(), rec22.height())