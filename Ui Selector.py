# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 07:39:51 2021

@author: Harrison
"""

#Ui selector Program
import sys
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

import time

from TableUi import Ui_MainWindow
#import LightUi



Home_ui = "TableUi.ui"
Home_MainWindow, QtBaseClass = uic.loadUiType(Home_ui)

Light_ui = "LightUi.ui"
Light_MainWindow, QtBaseClass = uic.loadUiType(Light_ui)


class MainWindow(QtWidgets.QMainWindow):
    Setupbool = 0
    def __init__(self):
        self.Setup_Home_Ui()

        
    def Setup_Home_Ui(self):
        QtWidgets.QMainWindow.__init__(self)
        Home_MainWindow.__init__(self)
        Home_MainWindow.setupUi(self, self)
        
        """
        Add Text
        """
        SleepText = 'Sleep Mode: Off'
        self.SleepButton.setText(SleepText)
        
        
        """
        Connect Signals
        """
        self.Light.pressed.connect(self.PressLight)
        self.LightButton.pressed.connect(self.PressLight)
        self.label.clicked.connect(self.Labelfn)
        
    def labelfn(self):
        print("Loshi")
        
        
    def Setup_Light_Ui(self):
        print("Hello")
        Light_MainWindow.__init__(self)
        Light_MainWindow.setupUi(self, self)
        
    def PressLight(self):
        self.Setup_Light_Ui()
    
    def retranslateUi(self, MainWindow):
        "sets up the top searchbar"
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Home.setText(_translate("MainWindow", "Home"))
        self.Light.setText(_translate("MainWindow", "Light"))
        self.Music.setText(_translate("MainWindow", "Music"))
        self.Weather.setText(_translate("MainWindow", "Weather"))
        self.Settings.setText(_translate("MainWindow", "Settings"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.ClockLabel.setText(_translate("MainWindow", "10:30:00"))

        

    
    
    
    
    
if not QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication(sys.argv)
else:
    app = QtWidgets.QApplication.instance() 
main = MainWindow()
main.show()
QtWidgets.QApplication.setQuitOnLastWindowClosed(True)
app.exec_()