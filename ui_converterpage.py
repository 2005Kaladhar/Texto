# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converterpagexoxuWt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 622)
        MainWindow.setMinimumSize(QSize(675, 434))
        icon = QIcon()
        icon.addFile(u"indianFlag.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-image: url(:/newPrefix/5c1d033b0b95a-wallpaper-preview.jpg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-image:None;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(222)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(117, -1, 0, -1)
        self.buttonspeak = QPushButton(self.frame_10)
        self.buttonspeak.setObjectName(u"buttonspeak")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonspeak.sizePolicy().hasHeightForWidth())
        self.buttonspeak.setSizePolicy(sizePolicy)
        self.buttonspeak.setMinimumSize(QSize(136, 48))
        font = QFont()
        font.setFamily(u"Showcard Gothic")
        font.setPointSize(14)
        self.buttonspeak.setFont(font)
        self.buttonspeak.setStyleSheet(u"QPushButton{\n"
"border-radius:22px;\n"
"	background-color: rgb(255, 193, 48);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(54, 161, 0, 200);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.buttonspeak)


        self.gridLayout_2.addWidget(self.frame_10, 2, 0, 1, 1)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setMinimumSize(QSize(597, 0))
        self.frame_11.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-image:None;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(88, 0, 88, 0)
        self.textbox = QLineEdit(self.frame_11)
        self.textbox.setObjectName(u"textbox")
        self.textbox.setMinimumSize(QSize(0, 44))
        font1 = QFont()
        font1.setPointSize(12)
        self.textbox.setFont(font1)
        self.textbox.setStyleSheet(u"QLineEdit{\n"
"border-radius:20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.textbox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.textbox)


        self.gridLayout_2.addWidget(self.frame_11, 1, 0, 1, 2)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setMinimumSize(QSize(113, 150))
        self.frame_7.setStyleSheet(u"border-image:none;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(15)
        self.formLayout_2.setContentsMargins(-1, -1, 15, -1)
        self.DavidButton = QRadioButton(self.frame_7)
        self.DavidButton.setObjectName(u"DavidButton")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.DavidButton.setFont(font2)
        self.DavidButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.DavidButton)

        self.ZiraButton = QRadioButton(self.frame_7)
        self.ZiraButton.setObjectName(u"ZiraButton")
        self.ZiraButton.setFont(font2)
        self.ZiraButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ZiraButton.setChecked(True)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.ZiraButton)


        self.verticalLayout_3.addLayout(self.formLayout_2)


        self.gridLayout_2.addWidget(self.frame_7, 2, 1, 1, 1)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-image:None;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.TitleBar_2 = QFrame(self.frame_8)
        self.TitleBar_2.setObjectName(u"TitleBar_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.TitleBar_2.sizePolicy().hasHeightForWidth())
        self.TitleBar_2.setSizePolicy(sizePolicy3)
        self.TitleBar_2.setMinimumSize(QSize(0, 0))
        self.TitleBar_2.setMaximumSize(QSize(16777215, 30))
        self.TitleBar_2.setStyleSheet(u"QFrame{\n"
"\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 215), stop:1 rgba(11, 15, 50, 194));\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"\n"
"}")
        self.TitleBar_2.setFrameShape(QFrame.StyledPanel)
        self.TitleBar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.TitleBar_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = QFrame(self.TitleBar_2)
        self.TitleBar.setObjectName(u"TitleBar")
        self.TitleBar.setCursor(QCursor(Qt.SizeAllCursor))
        self.TitleBar.setFrameShape(QFrame.StyledPanel)
        self.TitleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.TitleBar)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.TitleBar)

        self.frame_12 = QFrame(self.TitleBar_2)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QSize(0, 25))
        self.frame_12.setMaximumSize(QSize(100, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 0, 0, 0)
        self.Minimizebtn = QPushButton(self.frame_12)
        self.Minimizebtn.setObjectName(u"Minimizebtn")
        sizePolicy.setHeightForWidth(self.Minimizebtn.sizePolicy().hasHeightForWidth())
        self.Minimizebtn.setSizePolicy(sizePolicy)
        self.Minimizebtn.setMaximumSize(QSize(19, 19))
        self.Minimizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 0);\n"
"border-radius:9px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.Minimizebtn)

        self.Maximizebtn = QPushButton(self.frame_12)
        self.Maximizebtn.setObjectName(u"Maximizebtn")
        sizePolicy.setHeightForWidth(self.Maximizebtn.sizePolicy().hasHeightForWidth())
        self.Maximizebtn.setSizePolicy(sizePolicy)
        self.Maximizebtn.setMaximumSize(QSize(19, 19))
        self.Maximizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 0);\n"
"\n"
"border-radius:9px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(85, 170, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.Maximizebtn)

        self.CloseButton = QPushButton(self.frame_12)
        self.CloseButton.setObjectName(u"CloseButton")
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setMaximumSize(QSize(19, 19))
        self.CloseButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 0, 16);\n"
"\n"
"border-radius:9px;\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.CloseButton)


        self.horizontalLayout_5.addWidget(self.frame_12)


        self.verticalLayout_4.addWidget(self.TitleBar_2)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamily(u"Segoe Print")
        font3.setBold(False)
        font3.setWeight(50)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 0, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 128));\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0))\n"
";\n"
"background-color: qlineargradient(spread:pad, x1:0.53195, y1:0.932, x2:0.487, y2:0.0170455, stop:0 rgba(0, 0, 0, 127), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_2)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_9)


        self.gridLayout_2.addWidget(self.frame_8, 0, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setStyleSheet(u"QLabel{\n"
"border-image:None;\n"
"	color: rgb(250, 243, 51);\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.buttonspeak.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>s</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.buttonspeak.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Speak</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.buttonspeak.setText(QCoreApplication.translate("MainWindow", u"Speak", None))
        self.textbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Text Here", None))
        self.DavidButton.setText(QCoreApplication.translate("MainWindow", u"David", None))
        self.ZiraButton.setText(QCoreApplication.translate("MainWindow", u"Zira", None))
#if QT_CONFIG(tooltip)
        self.Minimizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Minimizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.Maximizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Maximizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.CloseButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CloseButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">L</span><span style=\" font-size:28pt;\">ive </span><span style=\" font-size:28pt; font-weight:600;\">T</span><span style=\" font-size:28pt;\">ext </span><span style=\" font-size:28pt; font-weight:600;\">T</span><span style=\" font-size:28pt;\">o </span><span style=\" font-size:28pt; font-weight:600;\">S</span><span style=\" font-size:28pt;\">peech </span><span style=\" font-size:28pt; font-weight:600;\">C</span><span style=\" font-size:28pt;\">onverter</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">M</span>ade in<span style=\" font-weight:600;\"> I</span>ndia, <span style=\" font-weight:600;\">C</span>reated <span style=\" font-weight:600;\">-K</span>aladhar <span style=\" font-weight:600;\">G</span>opal </p></body></html>", None))
    # retranslateUi

