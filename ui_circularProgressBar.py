# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'circularProgressBarxqqlrm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 702)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BaseFrame = QFrame(self.centralwidget)
        self.BaseFrame.setObjectName(u"BaseFrame")
        self.BaseFrame.setMinimumSize(QSize(460, 463))
        self.BaseFrame.setMaximumSize(QSize(460, 463))
        self.BaseFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(53, 0, 80,100);\n"
"border-radius:220;\n"
"\n"
"}")
        self.BaseFrame.setFrameShape(QFrame.StyledPanel)
        self.BaseFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.BaseFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ProgressBar = QFrame(self.BaseFrame)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setStyleSheet(u"QFrame{\n"
"border-radius:220px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.747082 rgba(255, 53, 53, 0), stop:0.749027 rgba(255, 245, 53, 255));\n"
"}")
        self.ProgressBar.setFrameShape(QFrame.StyledPanel)
        self.ProgressBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ProgressBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(11, 12, -1, 11)
        self.UppermostFrame = QFrame(self.ProgressBar)
        self.UppermostFrame.setObjectName(u"UppermostFrame")
        self.UppermostFrame.setStyleSheet(u"QFrame{\n"
"border-radius:219px;\n"
"	\n"
"	background-color: rgb(33, 36, 83);\n"
"}")
        self.UppermostFrame.setFrameShape(QFrame.StyledPanel)
        self.UppermostFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.UppermostFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 48, -1, 26)
        self.label_5 = QLabel(self.UppermostFrame)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"QLabel{\n"
"border-radius:10px;\n"
"	\n"
"	color: rgb(88, 96, 221);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)

        self.label_2 = QLabel(self.UppermostFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")

        self.gridLayout.addWidget(self.label_2, 0, 0, 2, 2)

        self.LoadingLabel = QLabel(self.UppermostFrame)
        self.LoadingLabel.setObjectName(u"LoadingLabel")
        font1 = QFont()
        font1.setPointSize(12)
        self.LoadingLabel.setFont(font1)
        self.LoadingLabel.setStyleSheet(u"QLabel{\n"
"border-radius:10px;\n"
"	color: rgb(255, 170, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")

        self.gridLayout.addWidget(self.LoadingLabel, 3, 0, 1, 2)

        self.PercentLabelFrame = QFrame(self.UppermostFrame)
        self.PercentLabelFrame.setObjectName(u"PercentLabelFrame")
        self.PercentLabelFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.PercentLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.PercentLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.PercentLabelFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(7, 0, 0, 0)
        self.PercentLabel = QLabel(self.PercentLabelFrame)
        self.PercentLabel.setObjectName(u"PercentLabel")
        self.PercentLabel.setStyleSheet(u"color: rgb(255, 135, 235);\n"
"\n"
"")
        self.PercentLabel.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_5.addWidget(self.PercentLabel)


        self.gridLayout.addWidget(self.PercentLabelFrame, 2, 0, 1, 2)


        self.horizontalLayout_4.addLayout(self.gridLayout)


        self.horizontalLayout_3.addWidget(self.UppermostFrame)


        self.horizontalLayout_2.addWidget(self.ProgressBar)


        self.horizontalLayout.addWidget(self.BaseFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Created</span><span style=\" font-size:10pt;\"> - Kaladhar Gopal</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">T</span><span style=\" font-size:48pt;\">exto</span></p></body></html>", None))
        self.LoadingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Processing...</p></body></html>", None))
        self.PercentLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600;\">0</span><span style=\" font-size:24pt; vertical-align:super;\">%</span></p></body></html>", None))
    # retranslateUi

