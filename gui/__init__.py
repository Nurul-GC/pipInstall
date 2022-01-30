from os import path
from random import randint
from time import sleep
import webbrowser

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from sys import argv, exit
from requests import request
from core import genlist, installnew, updpackages
from gui.pi import PiGUI


class PI:
    def __init__(self):
        self.gc = QApplication(argv)
        QFontDatabase.addApplicationFont("fonts/Kranky.ttf")
        # *****************************************
        img = QPixmap("favicons/favicon-512x512.png")
        self.align = int(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignAbsolute)

        self.init = QSplashScreen(img)
        self.init.setStyleSheet(theme)
        self.init.show()
        self.iniciar()

    def iniciar(self):
        load = 0
        while load < 100:
            self.init.showMessage(f"Loading the Program Modules: {load}%", self.align, Qt.GlobalColor.black)
            load += randint(1, 10)
            sleep(0.5)
        self.init.close()
        PiGUI().ferramentas.show()


if __name__ == '__main__':
    theme = open("themes/pi.qss").read().strip()
    app = PI()
    app.gc.exec()
