from os import path
from time import sleep
import webbrowser

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from sys import argv, exit
from requests import request
from core import genlist, installnew, updpackages

theme = open("themes/pi.qss").read().strip()


class PiGUI:
    def __init__(self):
        self.ferramentas = QWidget()
        self.ferramentas.setStyleSheet(theme)
        self.ferramentas.setWindowTitle('GC - PipInstall')

        self.principal()

    # **********MENU**********
    def _sair(self):
        return exit(0)

    def _instr(self):
        pass

    def _sobre(self):
        pass

    # **********JANELAS**********
    def principal(self):
        def genlistaction():
            logbox.setText(
                "Generating the list with all packages installed in your virtual environment..\n"
                "This may take a few minutes, please wait.."
                )
            QMessageBox.warning(self.ferramentas, "Generate Packages List", f"{genlist()}")

        def updpackagesaction():
            logbox.clear()
            logbox.setText(updpackages())

        def inspackaction():
            if packname.text() == "" or packname.text().isspace():
                QMessageBox.warning(self.ferramentas, "Install New Package", "Please inform the package's name before to proceed!")
            else:
                logbox.clear()
                logbox.setText(installnew(_package_name=packname.text()))

        def resetaction():
            logbox.clear()

        def viewpackaction():
            logbox.clear()
            with open("list/packages.txt", "r+") as packfile:
                logbox.setText(packfile.read())

        menu = QMenuBar()
        _help = menu.addMenu('Help')
        instr = _help.addAction('Instructions')
        _help.addSeparator()
        sair = _help.addAction('Exit')
        _sobre = menu.addAction('About')

        mainlayout = QFormLayout()
        mainlayout.setMenuBar(menu)

        label = QLabel(
            '<h1>GC - PipInstall.py</h1>'
            '<hr>'
            '<small>python 3rd-party packages easily/auto updater!</small>'
            '<br>'
            )
        label.setStyleSheet('margin-bottom:10px;')
        label.setAlignment(Qt.AlignmentFlag.AlignRight)
        mainlayout.addRow(label)

        genlistbtn = QPushButton('Generate Packages List')
        genlistbtn.setFixedWidth(300)
        genlistbtn.clicked.connect(genlistaction)
        # *****************************************
        updpackbtn = QPushButton('Update Packages')
        updpackbtn.clicked.connect(updpackagesaction)
        mainlayout.addRow(genlistbtn, updpackbtn)
        # *****************************************
        packname = QLineEdit()
        packname.setFixedWidth(300)
        packname.setClearButtonEnabled(True)
        packname.setPlaceholderText('Type here the package name..')
        inspackbtn = QPushButton('Install New Package')
        inspackbtn.clicked.connect(inspackaction)
        mainlayout.addRow(packname, inspackbtn)
        # *****************************************
        mainlayout.addRow(QLabel('<hr>'))

        logbox = QTextEdit()
        logbox.setPlaceholderText("Log Text Box..")
        logbox.setReadOnly(True)
        mainlayout.addRow(logbox)

        delogbox = QPushButton('Reset Log')
        delogbox.clicked.connect(resetaction)
        viewpackages = QPushButton('View Packages List')
        if not path.exists('list/packages.txt'):
            viewpackages.setDisabled(True)
        viewpackages.clicked.connect(viewpackaction)
        mainlayout.addRow(delogbox, viewpackages)
        # *****************************************
        mainlayout.addRow(QLabel('<hr>'))

        link = lambda: webbrowser.open('https://artesgc.home.blog')
        labelTrade = QLabel('<b><a href="#" style="text-decoration:none;">&trade;ArtesGC Inc</a></b>')
        labelTrade.setAlignment(Qt.AlignmentFlag.AlignRight)
        labelTrade.linkActivated.connect(link)
        labelTrade.setToolTip('Open ArtesGC oficial website!')
        mainlayout.addWidget(labelTrade)

        self.ferramentas.setLayout(mainlayout)
