from os import path
from time import sleep

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from sys import argv, exit
from requests import request
from core import genlist, installnew, updpackages


class PI:
    def __init__(self):
        self.gc = QApplication(argv)
        # *****************************************
        self.ferramentas = QWidget()
        self.ferramentas.setWindowTitle('GC - PipInstall.py')
        self.ferramentas.show()

        # hasconnection = request('GET', 'https://pypi.org').status_code
        self.principal()

    def principal(self):
        def genlistaction():
            logbox.clear()
            logbox.setText("Generating the list with all packages installed in your virtual environment..")
            sleep(0.2)
            logbox.setText("This may take a few minutes, please wait..")
            logbox.setText(genlist())

        def updpackagesaction():
            logbox.clear()
            logbox.setText(updpackages())

        mainlayout = QFormLayout()

        label = QLabel('<h1>GC - PipInstall.py</h1>'
                       '<hr>'
                       '<small>python 3rd-party packages easily/auto updater!</small>'
                       '<br>')
        label.setStyleSheet('margin-bottom:10px;')
        label.setAlignment(Qt.AlignmentFlag.AlignRight)
        mainlayout.addRow(label)

        btnlayout = QHBoxLayout()
        genlistbtn = QPushButton('Generate Packages List')
        genlistbtn.clicked.connect(genlistaction)
        btnlayout.addWidget(genlistbtn)
        # *****************************************
        updpackbtn = QPushButton('Update Packages')
        updpackbtn.clicked.connect(updpackagesaction)
        btnlayout.addWidget(updpackbtn)
        # *****************************************
        inspackbtn = QPushButton('Install New Package')
        btnlayout.addWidget(inspackbtn)
        mainlayout.addRow(btnlayout)

        logbox = QTextEdit()
        logbox.setReadOnly(True)
        logbox.setStyleSheet('background-color:black;'
                             'color:white;')
        mainlayout.addRow(logbox)

        delogbox = QPushButton('Reset Log')
        viewpackages = QPushButton('View Packages List')
        if not path.exists('list/packages.txt'):
            viewpackages.setDisabled(True)
        mainlayout.addRow(delogbox, viewpackages)

        self.ferramentas.setLayout(mainlayout)


if __name__ == '__main__':
    app = PI()
    app.gc.exec()
