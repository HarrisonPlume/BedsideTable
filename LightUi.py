# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\WeldingPressureTester2021\LightUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(22)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#FFFFFF;color:#565656")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 65))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Home = QtWidgets.QPushButton(self.widget)
        self.Home.setMinimumSize(QtCore.QSize(0, 40))
        self.Home.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily("Assistant")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Home.setFont(font)
        self.Home.setStyleSheet("border-style: solid;border-width: 0px;border-radius:0;background-color: #FFFFFF; padding:5px; color:#979797;font: 22pt \"Assistant\";")
        self.Home.setObjectName("Home")
        self.horizontalLayout.addWidget(self.Home)
        self.Light = QtWidgets.QPushButton(self.widget)
        self.Light.setMinimumSize(QtCore.QSize(0, 40))
        self.Light.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily("Assistant")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Light.setFont(font)
        self.Light.setStyleSheet("border-style: solid;border-width: 0px;border-radius:0;background-color: #FFFFFF; padding:5px;font: 22pt \"Assistant\";")
        self.Light.setObjectName("Light")
        self.horizontalLayout.addWidget(self.Light)
        self.Music = QtWidgets.QPushButton(self.widget)
        self.Music.setMinimumSize(QtCore.QSize(0, 40))
        self.Music.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily("Assistant")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Music.setFont(font)
        self.Music.setStyleSheet("border-style: solid;border-width: 0px;border-radius:0;background-color: #FFFFFF; padding:5px; color:#979797;font: 22pt \"Assistant\";")
        self.Music.setObjectName("Music")
        self.horizontalLayout.addWidget(self.Music)
        self.Weather = QtWidgets.QPushButton(self.widget)
        self.Weather.setMinimumSize(QtCore.QSize(0, 40))
        self.Weather.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily("Assistant")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Weather.setFont(font)
        self.Weather.setStyleSheet("border-style: solid;border-width: 0px;border-radius:0;background-color: #FFFFFF; padding:5px; color:#979797;font: 22pt \"Assistant\";")
        self.Weather.setObjectName("Weather")
        self.horizontalLayout.addWidget(self.Weather)
        self.Settings = QtWidgets.QPushButton(self.widget)
        self.Settings.setMinimumSize(QtCore.QSize(0, 40))
        self.Settings.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily("Assistant")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Settings.setFont(font)
        self.Settings.setStyleSheet("border-style: solid;border-width: 0px;border-radius:0;background-color: #FFFFFF; padding:5px; color:#979797;font: 22pt \"Assistant\";")
        self.Settings.setObjectName("Settings")
        self.horizontalLayout.addWidget(self.Settings)
        self.Exit = QtWidgets.QPushButton(self.widget)
        self.Exit.setMinimumSize(QtCore.QSize(0, 40))
        self.Exit.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily("Assistant")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Exit.setFont(font)
        self.Exit.setStyleSheet("border-style: solid;border-width: 0px;border-radius:0;background-color: #FFFFFF; padding:5px; color:#979797;font: 22pt \"Assistant\";")
        self.Exit.setObjectName("Exit")
        self.horizontalLayout.addWidget(self.Exit)
        self.ClockLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ClockLabel.setFont(font)
        self.ClockLabel.setStyleSheet("border-style: solid;border-width: 0px;border-radius:0;background-color: #FFFFFF; padding:5px;font: 22pt \"Courier\";")
        self.ClockLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ClockLabel.setObjectName("ClockLabel")
        self.horizontalLayout.addWidget(self.ClockLabel)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 5)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton_2.setStyleSheet("color: #FFAE0D;\n"
"font: 63 22pt \"Assistant SemiBold\";border-style: solid;border-width: 0px; padding:5px;border-radius: 20; \n"
"background-color:rgba(255, 223, 158, 255)\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(self.widget_2)
        self.verticalSlider.setMinimumSize(QtCore.QSize(100, 0))
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setSliderPosition(10)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_2.addWidget(self.verticalSlider, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Home.setText(_translate("MainWindow", "Home"))
        self.Light.setText(_translate("MainWindow", "Light"))
        self.Music.setText(_translate("MainWindow", "Music"))
        self.Weather.setText(_translate("MainWindow", "Weather"))
        self.Settings.setText(_translate("MainWindow", "Settings"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.ClockLabel.setText(_translate("MainWindow", "10:30:00"))
        self.pushButton_2.setText(_translate("MainWindow", "On "))
import Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())