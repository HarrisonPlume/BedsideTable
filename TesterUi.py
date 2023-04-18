# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:27:04 2021

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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg 
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from subprocess import run
from functools import partial

import serial

import numpy as np

import time
import json

import os

os.chdir("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable")
# os.chdir("C:\BedsideTableUpgrade\CodeBase\BedsideTable")

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_ylabel('Temperature (°C)')
        self.axes.set_xlabel('Mins Ago')
        fig.subplots_adjust(left = 0.28, bottom = 0.20, right = 0.90, top = 0.90)
        plt.rc('axes',edgecolor="#979797")
        plt.rcParams["text.color"] = "#979797"
        plt.rcParams["axes.labelcolor"] = "#979797"
        fig.set_facecolor("#FFFFFF")
        self.axes.tick_params(axis='x', colors="#979797")
        self.axes.tick_params(axis='y', colors="#979797")
        super(MplCanvas, self).__init__(fig)


import asyncio

#import pyfirmata
#from pyfirmata import util

Home_Ui = "TableUi.ui"
HomeWindow, QtBaseClass = uic.loadUiType(Home_Ui)

LightWindow,  QtBaseClass = uic.loadUiType("LightUi.ui")

AlarmWindow, QtBaseClass = uic.loadUiType("AlarmUi.ui")

WeatherWindow, QtBaseClass = uic.loadUiType("WeatherUi.ui")

BlindWindow, QtBaseClass = uic.loadUiType("BlindUi.ui")

class MainWindow(QtWidgets.QMainWindow, HomeWindow):
    Stopped = False    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.SetupHomeUi()
        
        self.ClockThread = Clock()
        self.ClockThread.alarm.connect(self.AlarmFunc)
        self.ClockThread.onCountChanged.connect(self.ClockFunc)
        self.ClockThread.TemperatureData.connect(self.TempFunc)
        self.ClockThread.TemperatureList.connect(self.TemperaturePlot)
        self.ClockThread.start()        

            
    

        
    def SetupHomeUi(self):
        HomeWindow.__init__(self)
        self.setupUi(self)
        
        #Set previously stored alarm time
        f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r")
        # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r")
        data = json.load(f)
        for i in data["Settings"]:
            if i["Name"] == "Alarm":
                if i["Enable"] == "True":
                    self.AlarmButton.setText("Alarm ON \n"+str(i["Time"]))
                else:
                    self.AlarmButton.setText("Alarm Off")
                    self.AlarmButton.setStyleSheet("font: 63 22pt 'Assistant SemiBold';border-style: solid;border-width: 0px; padding:5px;border-radius: 20; \nbackground-color: rgb(138, 138, 138);")
            if i["Name"] == "Light":
                if i["LightEnable"] == "True":
                    self.LightButton.setStyleSheet('color: #FFAE0D;\nfont: 63 22pt "Assistant SemiBold";border-style: solid;border-width: 0px; padding:5px;border-radius: 20; \nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 223, 158, 255), stop:0.2 rgba(255, 247, 232, 255));\n')
                    self.LightButton.setText("Lamp - On")
                else:
                    self.LightButton.setStyleSheet("background-color : #2f2f2f; border-radius:20; font: 63 22pt 'Assistant SemiBold'")
                    self.LightButton.setText("Lamp - Off")
                             
        f.close()
        # Toolbar
        self.Alarm.pressed.connect(self.LoadAlarmUi)
        self.Exit.pressed.connect(self.PressExit)
        self.Light.clicked.connect(self.PressLightMenu)
        self.Weather.pressed.connect(self.LoadWeatherUi)
        self.Blind.pressed.connect(self.LoadBlindUi)
        #Setup Light button on home screen
        self.LightButton.setCheckable(True)
        
        self.LightButton.pressed.connect(self.PressLightRelay)
        
        
        #Setup Alarm Functionality
        self.AlarmButton.clicked.connect(self.LoadAlarmUi)
        
        self.SleepButton.setCheckable(True)
        
        self.SleepButton.clicked.connect(self.SleepMode)
        
    def TempFunc(self, Temp, Hum):
        try:
            self.TemperatureButton.setText("Temperature: "+Temp+" C\nHumidity: "+Hum+" %")
        except:
            try:
                self.TemperatureLine.setText(Temp)
                self.HumidityLine.setText(Hum)
            except:
                pass            
        
        
        
    def PressExit(self):
        self.close()
        
    def ClockFunc(self, text):
        try:
            self.ClockLabel.setText(text)
        except:
            pass
        
    def SleepMode(self):
        if self.SleepButton.isChecked():
            #Turn off the backlight
            run('vcgencmd display_power 0', shell=True)
        else:
            run('vcgencmd display_power 1', shell=True)
            
    def AlarmFunc(self):
        f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r+")
        # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r+")
        data = json.load(f)
        for i in data["Settings"]:
            if i["Name"] == "Alarm":
                if i["Enable"] == "True":
                    i["Enable"] = "False"
        f.seek(0)
        f.truncate(0)
        json.dump(data,f)
        f.close()
        self.BlindUpFunc()
                
                                    
    def PressLightRelay(self):
        try:
            if self.LightButton.isChecked():
                f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r+")
                # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r+")
                data = json.load(f)
                for i in data["Settings"]:
                    if i["Name"] == "Light":
                        if i["LightEnable"] == "False":
                            i["LightEnable"] = "True"
                f.seek(0)
                f.truncate(0)
                json.dump(data,f)
                f.close()
                self.LightButton.setStyleSheet('color: #FFAE0D;\nfont: 63 22pt "Assistant SemiBold";border-style: solid;border-width: 0px; padding:5px;border-radius: 20; \nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 223, 158, 255), stop:0.2 rgba(255, 247, 232, 255));\n')
                self.LightButton.setText("Lamp - On")
            else:
                f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r+")
                # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r+")
                data = json.load(f)
                for i in data["Settings"]:
                    if i["Name"] == "Light":
                        if i["LightEnable"] == "True":
                            i["LightEnable"] = "False"
                f.seek(0)
                f.truncate(0)
                json.dump(data,f)
                f.close()
                self.LightButton.setStyleSheet("background-color : #2f2f2f; border-radius:20; font: 63 22pt 'Assistant SemiBold'")
                self.LightButton.setText("Lamp - Off")                
        except:
            print("Arduino not connected")
        
    def closeEvent(self, event):
        MainWindow.Stopped = True
        try:
            self.serial.close()
        except:
            pass 
        event.accept()


    def LoadBlindUi(self):
        self.setupUi(self)
        BlindWindow.__init__(self)
        BlindWindow.setupUi(self, self)
        BlindWindow.retranslateUi(self, self)
        
        self.Home.pressed.connect(self.SetupHomeUi)
        self.Alarm.pressed.connect(self.LoadAlarmUi)
        self.Weather.pressed.connect(self.LoadWeatherUi)
        self.Light.pressed.connect(self.PressLightMenu)
        self.Exit.pressed.connect(self.PressExit)

        self.BlindUp.pressed.connect(self.BlindUpFunc)
        self.BlindDown.pressed.connect(self.BlindDownFunc)


    def BlindUpFunc(self):
        f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r+")
        # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r+")
        data = json.load(f)
        for i in data["Settings"]:
            if i["Name"] == "Blind":
                if i["Status"] == "None":
                    i["Status"] = "Up"

        f.seek(0)
        f.truncate(0)
        json.dump(data,f)
        f.close()

        time.sleep(0.6)

        f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r+")
        # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r+")
        data = json.load(f)
        for i in data["Settings"]:
            if i["Name"] == "Blind":
                if i["Status"] == "Up":
                    i["Status"] = "None"

        f.seek(0)
        f.truncate(0)
        json.dump(data,f)
        f.close()

    def BlindDownFunc(self):
        f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r+")
        # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r+")
        data = json.load(f)
        for i in data["Settings"]:
            if i["Name"] == "Blind":
                if i["Status"] == "None":
                    i["Status"] = "Down"
        f.seek(0)
        f.truncate(0)
        json.dump(data,f)
        f.close()

        time.sleep(0.6)

        f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r+")
        # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r+")
        data = json.load(f)
        for i in data["Settings"]:
            if i["Name"] == "Blind":
                if i["Status"] == "Down":
                    i["Status"] = "None"

        f.seek(0)
        f.truncate(0)
        json.dump(data,f)
        f.close()
                    
        
        
    def PressLightMenu(self):
        self.LoadLightUi()
        
    def LoadLightUi(self):
        self.setupUi(self)
        LightWindow.__init__(self)
        LightWindow.setupUi(self, self)
        LightWindow.retranslateUi(self, self)
        
        self.Home.pressed.connect(self.SetupHomeUi)
        self.Alarm.pressed.connect(self.LoadAlarmUi)
        self.Weather.pressed.connect(self.LoadWeatherUi)
        self.Exit.pressed.connect(self.PressExit)
        self.LightButton.setCheckable(True)
        self.LightButton.clicked.connect(self.PressLightRelay)
        self.Blind.pressed.connect(self.LoadBlindUi)
            
        f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r")
        # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r")
        data = json.load(f)
        for i in data["Settings"]:
            if i["Name"] == "Light":
                if i["LightEnable"] == "False":
                    self.LightButton.setStyleSheet("background-color : #2f2f2f; border-radius:20; font: 63 22pt 'Assistant SemiBold'")
                    self.LightButton.setText("Lamp - Off")
                else:
                    self.LightButton.setStyleSheet('color: #FFAE0D;\nfont: 63 22pt "Assistant SemiBold";border-style: solid;border-width: 0px; padding:5px;border-radius: 20; \nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 223, 158, 255), stop:0.2 rgba(255, 247, 232, 255));\n')
                    self.LightButton.setText("Lamp - On")
        f.close()
        
        
    def LoadWeatherUi(self):
        self.setupUi(self)
        WeatherWindow.__init__(self)
        WeatherWindow.setupUi(self, self)
        WeatherWindow.retranslateUi(self, self)
        
        self.Light.pressed.connect(self.PressLightMenu)
        self.Home.pressed.connect(self.SetupHomeUi)
        self.Exit.pressed.connect(self.PressExit)
        self.Alarm.pressed.connect(self.LoadAlarmUi)
        self.Blind.pressed.connect(self.LoadBlindUi)
        
        layout = QVBoxLayout()
        
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        try:
            self.sc.axes.set_xlim(len(self.TemperatureList)-1,-1)
            self.sc.axes.plot(list(np.arange(len(self.TemperatureList),-1,-1)[1:]),self.TemperatureList)
            
            
        except:
            pass
        layout.addWidget(self.sc)
        self.Graph.setLayout(layout)
        
        
    def TemperaturePlot(self, Data):
        self.TemperatureList = Data
        try:
            self.sc.axes.set_xlim(len(self.TemperatureList)-1,-1)
            self.sc.axes.plot(list(np.arange(len(self.TemperatureList),-1,-1)[1:]),self.TemperatureList)
        except:
            pass
        
        
    def LoadAlarmUi(self):
        self.setupUi(self)
        AlarmWindow.__init__(self)
        AlarmWindow.setupUi(self, self)
        AlarmWindow.retranslateUi(self, self)
        
        self.Light.pressed.connect(self.PressLightMenu)
        self.Home.pressed.connect(self.SetupHomeUi)
        self.Exit.pressed.connect(self.PressExit)
        self.Weather.pressed.connect(self.LoadWeatherUi)
        self.Blind.pressed.connect(self.LoadBlindUi)
        
        f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r")
        # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r")
        data = json.load(f)
        for i in data["Settings"]:
            if i["Name"] == "Alarm":
                if i["Enable"] == "True":
                    self.Enable.setText("Disable")
                    self.Enable.setStyleSheet("font: 63 30pt 'Assistant SemiBold';border-style: solid;border-width: 0px; padding:5px;border-radius: 20;background-color: #00cc00;color: #006600;")
                else:
                    self.Enable.setText("Enable")
                    self.Enable.setStyleSheet("font: 63 30pt 'Assistant SemiBold';border-style: solid;border-width: 0px; padding:5px;border-radius: 20;background-color: rgb(138, 138, 138);")
                self.AlarmSetTime.setText(i["Time"])
        f.close()
        
        #Set Checkable Buttons
        self.Enable.setCheckable(True)
        self.AlarmCounter = 0
        
        button_one = partial(self.PressAlarmButton, 1)
        button_two = partial(self.PressAlarmButton, 2)
        button_three = partial(self.PressAlarmButton, 3)
        button_four = partial(self.PressAlarmButton, 4)
        button_five = partial(self.PressAlarmButton, 5)
        button_six = partial(self.PressAlarmButton, 6)
        button_seven = partial(self.PressAlarmButton, 7)
        button_eight = partial(self.PressAlarmButton, 8)
        button_nine = partial(self.PressAlarmButton, 9)
        button_zero = partial(self.PressAlarmButton, 0)
        button_clear = partial(self.PressAlarmButton, "CL")
        button_EN = partial(self.PressAlarmButton, "EN")
        
        self.One.pressed.connect(button_one)
        self.Two.pressed.connect(button_two)
        self.Three.pressed.connect(button_three)
        self.Four.pressed.connect(button_four)
        self.Five.pressed.connect(button_five)
        self.Six.pressed.connect(button_six)
        self.Seven.pressed.connect(button_seven)
        self.Eight.pressed.connect(button_eight)
        self.Nine.pressed.connect(button_nine)
        self.Zero.pressed.connect(button_zero)
        self.Clear.pressed.connect(button_clear)
        self.Enable.pressed.connect(button_EN)
        
        if self.Enable.isChecked():
            self.Enable.setText("Disable")
            self.Enable.setStyleSheet("font: 63 30pt 'Assistant SemiBold';border-style: solid;border-width: 0px; padding:5px;border-radius: 20;background-color: #00cc00;color: #006600;")
        
        
    def PressAlarmButton(self,Button):        
        if Button == "EN":
            if self.Enable.isChecked():
                self.Enable.setText("Enable")
                self.Enable.setStyleSheet("font: 63 30pt 'Assistant SemiBold';border-style: solid;border-width: 0px; padding:5px;border-radius: 20;background-color: rgb(138, 138, 138);")
                f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r+")
                # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r+")
                data = json.load(f)
                for i in data["Settings"]:
                    if i["Name"] == "Alarm":
                        if i["Enable"] == "True":
                            i["Enable"] = "False"
                f.seek(0)
                f.truncate(0)
                json.dump(data,f)
                f.close()
            else:
                if len(self.AlarmSetTime.text())>3:
                    self.Enable.setText("Disable")
                    self.Enable.setStyleSheet("font: 63 30pt 'Assistant SemiBold';border-style: solid;border-width: 0px; padding:5px;border-radius: 20;background-color: #00cc00;color: #006600;")
                    f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r+")
                    # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r+")
                    data = json.load(f)
                    for i in data["Settings"]:
                        if i["Name"] == "Alarm":
                            if i["Enable"] == "False":
                                i["Enable"] = "True"
                            if i["Time"] != self.AlarmSetTime.text():
                                i["Time"] = self.AlarmSetTime.text()
                    f.seek(0)
                    f.truncate(0)
                    json.dump(data,f)
                    f.close()
                else:
                    self.Enable.setChecked(False)
        elif Button == "CL":
            self.AlarmSetTime.clear()
            self.AlarmCounter = 0
        else:
            
            if self.AlarmCounter == 0:
                if Button > 2:
                    Button = 2
                self.AlarmSetTime.clear()
                self.AlarmSetTime.setText(str(Button))
                self.AlarmCounter = 1
            elif self.AlarmCounter == 1:
                CurrentAlarm = self.AlarmSetTime.text()
                if int(CurrentAlarm) == 2:
                    if Button > 4:
                        Button = 4
                self.AlarmSetTime.setText(CurrentAlarm+str(Button)+":")
                self.AlarmCounter += 1
            elif self.AlarmCounter == 2:
                if Button > 5:
                    Button = 5
                CurrentAlarm = self.AlarmSetTime.text()
                self.AlarmSetTime.setText(CurrentAlarm+str(Button))
                self.AlarmCounter += 1
            elif self.AlarmCounter == 3:
                CurrentAlarm = self.AlarmSetTime.text()
                self.AlarmSetTime.setText(CurrentAlarm+str(Button))
                self.AlarmCounter += 1
            else:
                self.AlarmCounter = 0
                if Button > 2:
                    Button = 2
                self.AlarmSetTime.clear()
                self.AlarmSetTime.setText(str(Button))
                self.AlarmCounter = 1    
                
    
class Clock(QThread):
    onCountChanged = pyqtSignal(str)
    alarm = pyqtSignal()
    TemperatureData = pyqtSignal(str, str)
    TemperatureList = pyqtSignal(list)
    TempList = []
    def run(self):
        oldtime = "0"
        try:
            ArduinoSerial = serial.Serial("/dev/ttyACM0", 9600)
            print("Arduino connected Successfully")
        except:
            print("Arduino Connection failed")
        
        while MainWindow.Stopped == False:
            currenttime = time.localtime(time.time())
            currenttimemins = time.strftime("%H:%M", currenttime)
            currenttime = time.strftime("%H:%M:%S", currenttime)
            self.onCountChanged.emit(currenttime)
            
            #Temperature and humidity handeling
            try:
                SerialData = ArduinoSerial.readline().decode("utf-8")
                Temperature = SerialData.split(",")[1][:4]
                Humidity = SerialData.split(",")[3][:4]
                self.TemperatureData.emit(Temperature, Humidity)
                if oldtime != currenttimemins:
                    if len(self.TempList) > 720:
                        self.TempList = self.TempList[1:]
                    self.TempList.append(float(Temperature))
                    self.TemperatureList.emit(self.TempList)
                    
            except:
                pass            
            f = open("/home/pi/Desktop/WeldingPressureTester2021/BedsideTable/Config.json","r")
            # f = open("C:\BedsideTableUpgrade\CodeBase\BedsideTable\Config.json","r+")
            data = json.load(f)
            for i in data["Settings"]:
                if i["Name"] == "Alarm":
                    if i["Enable"] == "True":
                        if i["Time"] == currenttimemins:
                            print("ALARM")
                            #Turn On Screen
                            run('vcgencmd display_power 1', shell=True)
                            self.alarm.emit()
                if i["Name"] == "Light":
                    if i["LightEnable"] == "True":
                        on = "1".encode("utf-8")
                        try:
                            ArduinoSerial.write(on)
                        except:
                            pass
                    else:
                        off = "2".encode("utf-8")
                        try:
                            ArduinoSerial.write(off)
                        except:
                            pass
                if i["Name"] == "Blind":
                    if i["Status"] == "Up":
                        up = "3".encode("utf-8")
                        print("Blind_up")
                        try:
                            ArduinoSerial.write(up)
                        except:
                            pass
                    elif i["Status"] == "Down":
                        down = "4".encode("utf-8")
                        print("Blind_down")
                        try:
                            ArduinoSerial.write(down)
                        except:
                            pass

            f.close()
            oldtime = currenttimemins
            time.sleep(0.5)
        ArduinoSerial.close()        
            
            

if not QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication(sys.argv)
else:
    app = QtWidgets.QApplication.instance() 
main = MainWindow()
main.show()
QtWidgets.QApplication.setQuitOnLastWindowClosed(True)
app.exec_()