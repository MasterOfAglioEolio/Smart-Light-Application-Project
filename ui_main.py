# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Render_Time_Calculatoricgnoh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtCore,QtGui
import math
import time

from tensorflow.keras.models import Model,load_model
import pyaudio
import numpy as np
import struct
import librosa
import config

from threading import Thread
import socket
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

HOST = '172.30.1.26'  # all available interfaces
PORT = 1428
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("connect")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 800)
        MainWindow.setMinimumSize(QSize(500, 800))
        MainWindow.setMaximumSize(QSize(605, 800))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(255,255, 255);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
                                      
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"width:295px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-av-timer.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")

        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/32x32/icons/32x32/timer-icon.png);\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)###전체
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(400, 16777215))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_18 = QVBoxLayout(self.page_home)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_div_time_per_frame = QFrame(self.page_home)
        self.frame_div_time_per_frame.setObjectName(u"frame_div_time_per_frame")
        self.frame_div_time_per_frame.setMinimumSize(QSize(0, 140))
        self.frame_div_time_per_frame.setMaximumSize(QSize(390, 200))
        self.frame_div_time_per_frame.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 10px;\n"
"")
        self.frame_div_time_per_frame.setFrameShape(QFrame.NoFrame)
        self.frame_div_time_per_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_div_time_per_frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_2 = QFrame(self.frame_div_time_per_frame)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        font5 = QFont()
        font5.setFamily(u"Roboto Light")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.labelBoxBlenderInstalation_2.setFont(font5)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.labelBoxBlenderInstalation_2)


        self.verticalLayout_10.addWidget(self.frame_title_wid_2)

        ################## 상단 타이틀 인터페이스 ##############

        text = ['우울', '긴장', '편안/안정', '따뜻', '불안', '활동']
        self.pushbutton_emo = []
        self.labelList = []
        self.shadowlist=[]




        self.frame_content_wid_2 = QFrame(self.frame_div_time_per_frame)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_content_wid_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")


        font6 = QFont()
        font6.setFamily(u"Roboto Thin")
        font6.setPointSize(40)

        for i in range(len(text)):
            self.pushbutton_emo.append(QPushButton())
            self.pushbutton_emo[i].setMaximumHeight(50)
            self.pushbutton_emo[i].setMaximumWidth(100)
            self.shadowlist.append(QGraphicsDropShadowEffect())
            self.shadowlist[i].setXOffset(2)
            self.shadowlist[i].setYOffset(2)
            self.shadowlist[i].setBlurRadius(10)
            self.shadowlist[i].setColor(QColor("black"))
            self.pushbutton_emo[i].setGraphicsEffect(self.shadowlist[i])



        icon20=QIcon() #우울

        self.pushbutton_emo[0].setStyleSheet(u"QPushButton {\n"
                                                 "	border: 2px solid rgb(52, 59, 72);\n"
                                                 "	border-radius: 10px;	\n"
                                                 "	background-color: rgb(52, 59, 72);\n"
                                                 "	padding-right: 5px;\n"
                                             
                                        
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-color: rgb(57, 65, 80);\n"
                                                 "	border: 2px solid rgb(61, 70, 86);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {	\n"
                                                 "	background-color: rgb(35, 40, 49);\n"
                                                 "	border: 2px solid rgb(43, 50, 61);\n"
                                                 "}")
        icon20 = QIcon("emotion/우울.png")  # 긴장
        self.pushbutton_emo[0].setIcon(icon20)
        self.pushbutton_emo[0].setIconSize(QSize(40, 40))
        self.pushbutton_emo[0].clicked.connect(lambda: self.emotionClicked(0))
        self.gridLayout_3.addWidget(self.pushbutton_emo[0],0,0)


        # icon21.addFile(u"emotion/긴장.png", QSize(24,24), QIcon.Normal, QIcon.Off)
        self.pushbutton_emo[1].setStyleSheet(u"QPushButton {\n"
                                             "	border: 2px solid rgb(52, 59, 72);\n"
                                             "	border-radius: 10px;	\n"
                                             "	background-color: rgb(52, 59, 72);\n"
                                             "	padding-right: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "	background-color: rgb(57, 65, 80);\n"
                                             "	border: 2px solid rgb(61, 70, 86);\n"
                                             "}\n"
                                             "QPushButton:pressed {	\n"
                                             "	background-color: rgb(35, 40, 49);\n"
                                             "	border: 2px solid rgb(43, 50, 61);\n"
                                             "}")
        icon21 = QIcon("emotion/긴장.png")  # 긴장
        self.pushbutton_emo[1].setIcon(icon21)
        self.pushbutton_emo[1].setIconSize(QSize(40, 40))
        self.pushbutton_emo[1].clicked.connect(lambda: self.emotionClicked(1))
        self.gridLayout_3.addWidget(self.pushbutton_emo[1], 0, 1)

        icon22 = QIcon() #편안/안정
        self.pushbutton_emo[2].setStyleSheet(u"QPushButton {\n"
                                             "	border: 2px solid rgb(52, 59, 72);\n"
                                             "	border-radius: 10px;	\n"
                                             "	background-color: rgb(52, 59, 72);\n"
                                             "	padding-right: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "	background-color: rgb(57, 65, 80);\n"
                                             "	border: 2px solid rgb(61, 70, 86);\n"
                                             "}\n"
                                             "QPushButton:pressed {	\n"
                                             "	background-color: rgb(35, 40, 49);\n"
                                             "	border: 2px solid rgb(43, 50, 61);\n"
                                             "}")
        icon22 = QIcon("emotion/편안.png")  # 편안
        self.pushbutton_emo[2].setIcon(icon22)
        self.pushbutton_emo[2].setIconSize(QSize(40, 40))
        self.pushbutton_emo[2].clicked.connect(lambda: self.emotionClicked(2))
        self.gridLayout_3.addWidget(self.pushbutton_emo[2], 0, 2)

        icon23 = QIcon() #따뜻
        self.pushbutton_emo[3].setStyleSheet(u"QPushButton {\n"
                                             "	border: 2px solid rgb(52, 59, 72);\n"
                                             "	border-radius: 10px;	\n"
                                             "	background-color: rgb(52, 59, 72);\n"
                                             "	padding-right: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "	background-color: rgb(57, 65, 80);\n"
                                             "	border: 2px solid rgb(61, 70, 86);\n"
                                             "}\n"
                                             "QPushButton:pressed {	\n"
                                             "	background-color: rgb(35, 40, 49);\n"
                                             "	border: 2px solid rgb(43, 50, 61);\n"
                                             "}")
        icon23 = QIcon("emotion/따뜻.png")  # 따뜻
        self.pushbutton_emo[3].setIcon(icon23)
        self.pushbutton_emo[3].setIconSize(QSize(40, 40))
        self.pushbutton_emo[3].clicked.connect(lambda: self.emotionClicked(3))
        self.gridLayout_3.addWidget(self.pushbutton_emo[3], 1, 0)

        icon24 = QIcon() #불안
        self.pushbutton_emo[4].setStyleSheet(u"QPushButton {\n"
                                             "	border: 2px solid rgb(52, 59, 72);\n"
                                             "	border-radius: 10px;	\n"
                                             "	background-color: rgb(52, 59, 72);\n"
                                             "	padding-right: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "	background-color: rgb(57, 65, 80);\n"
                                             "	border: 2px solid rgb(61, 70, 86);\n"
                                             "}\n"
                                             "QPushButton:pressed {	\n"
                                             "	background-color: rgb(35, 40, 49);\n"
                                             "	border: 2px solid rgb(43, 50, 61);\n"
                                             "}")
        icon24 = QIcon("emotion/불안.png")  # 긴장
        self.pushbutton_emo[4].setIcon(icon24)
        self.pushbutton_emo[4].setIconSize(QSize(40, 40))
        self.pushbutton_emo[4].clicked.connect(lambda: self.emotionClicked(4))
        self.gridLayout_3.addWidget(self.pushbutton_emo[4], 1, 1)

        icon25 = QIcon() #활기

        self.pushbutton_emo[5].setStyleSheet(u"QPushButton {\n"
                                             "	border: 2px solid rgb(52, 59, 72);\n"
                                             "	border-radius: 10px;	\n"
                                             "	background-color: rgb(52, 59, 72);\n"
                                             "	padding-right: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "	background-color: rgb(57, 65, 80);\n"
                                             "	border: 2px solid rgb(61, 70, 86);\n"
                                             "}\n"
                                             "QPushButton:pressed {	\n"
                                             "	background-color: rgb(35, 40, 49);\n"
                                             "	border: 2px solid rgb(43, 50, 61);\n"
                                             "}")
        icon25 = QIcon("emotion/활기.png")  # 긴장
        self.pushbutton_emo[5].setIcon(icon25)
        self.pushbutton_emo[5].setIconSize(QSize(40, 40))
        self.pushbutton_emo[5].clicked.connect(lambda: self.emotionClicked(5))
        self.gridLayout_3.addWidget(self.pushbutton_emo[5], 1, 2)

        self.verticalLayout_13.addLayout(self.gridLayout_3)


        self.verticalLayout_10.addWidget(self.frame_content_wid_2)


        self.verticalLayout_18.addWidget(self.frame_div_time_per_frame)
        ################## 상단 인터페이스 ##############

        self.frame_div_number_frames = QFrame(self.page_home)
        self.frame_div_number_frames.setObjectName(u"frame_div_number_frames")
        self.frame_div_number_frames.setMinimumSize(QSize(0, 170))
        self.frame_div_number_frames.setMaximumSize(QSize(390, 200))
        self.frame_div_number_frames.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 10px;\n"
"")################## 중단 백그라운드 ##############

        self.frame_div_number_frames.setFrameShape(QFrame.NoFrame)
        self.frame_div_number_frames.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_div_number_frames)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_3 = QFrame(self.frame_div_number_frames)
        self.frame_title_wid_3.setObjectName(u"frame_title_wid_3")
        self.frame_title_wid_3.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_3.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_3.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_title_wid_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_title_wid_3)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setFont(font5)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.labelBoxBlenderInstalation_3)


        self.verticalLayout_14.addWidget(self.frame_title_wid_3)

        self.frame_content_wid_3 = QFrame(self.frame_div_number_frames)
        self.frame_content_wid_3.setObjectName(u"frame_content_wid_3")
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_content_wid_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_machines = QLabel(self.frame_content_wid_3)
        self.label_machines.setObjectName(u"label_machines")
        self.label_machines.setMaximumSize(QSize(16777215, 20))
        self.label_machines.setFont(font2)
        self.label_machines.setStyleSheet(u"")
        self.label_machines.setLineWidth(1)
        self.label_machines.setAlignment(Qt.AlignCenter)

        # self.gridLayout_4.addWidget(self.label_machines, 1, 1, 1, 1) ##################  muchine label ##############

        self.lineEdit_machines = QLineEdit(self.frame_content_wid_3)
        self.shadow1 = QGraphicsDropShadowEffect()
        self.shadow1.setYOffset(2)
        self.shadow1.setXOffset(2)
        self.shadow1.setBlurRadius(10)
        self.shadow1.setColor(QColor("black"))
        self.lineEdit_machines.setGraphicsEffect(self.shadow1)
        self.lineEdit_machines.setObjectName(u"lineEdit_machines")
        self.lineEdit_machines.setMinimumSize(QSize(100, 60))
        self.lineEdit_machines.setFont(font6)
        self.lineEdit_machines.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	padding: 0px;\n"
"	selection-background-color: rgb(85, 170, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(44, 49, 60);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(27, 29, 35);\n"
"}")

        self.lineEdit_machines.setMaxLength(10)
        self.lineEdit_machines.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_machines, 0, 1, 1, 1)
################## muchines 인터페이스 ##############


        self.DialogButton = QPushButton(self.frame_content_wid_3)
        self.shadow2 = QGraphicsDropShadowEffect()
        self.shadow2.setYOffset(2)
        self.shadow2.setXOffset(2)
        self.shadow2.setBlurRadius(10)
        self.shadow2.setColor(QColor("black"))
        self.DialogButton.setGraphicsEffect(self.shadow2)
        self.DialogButton.setObjectName(u"DialogButton")
        self.DialogButton.setMinimumSize(QSize(100, 60))
        self.DialogButton.setFont(font6)
        self.DialogButton.setStyleSheet(u"QPushButton {\n"
                                             "	border: 2px solid rgb(52, 59, 72);\n"
                                             "	border-radius: 10px;	\n"
                                             "	background-color: rgb(52, 59, 72);\n"
                                             "	padding-right: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "	background-color: rgb(57, 65, 80);\n"
                                             "	border: 2px solid rgb(61, 70, 86);\n"
                                             "}\n"
                                             "QPushButton:pressed {	\n"
                                             "	background-color: rgb(35, 40, 49);\n"
                                             "	border: 2px solid rgb(43, 50, 61);\n"
                                             "}")

        self.DialogButton.clicked.connect(self.showColorDlg)
        self.gridLayout_4.addWidget(self.DialogButton, 0, 0, 1, 1)


        self.label_frames = QLabel(self.frame_content_wid_3)
        self.label_frames.setObjectName(u"label_frames")
        self.label_frames.setMaximumSize(QSize(16777215, 20))
        self.label_frames.setFont(font2)
        self.label_frames.setStyleSheet(u"")
        self.label_frames.setLineWidth(1)
        self.label_frames.setAlignment(Qt.AlignCenter)

        # self.gridLayout_4.addWidget(self.label_frames, 1, 0, 1, 1)


        ################## frame 인터페이스 ##############
        self.label_current_render = QLabel(self.frame_content_wid_3)
        self.label_current_render.setObjectName(u"label_current_render")
        self.label_current_render.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"padding-bottom: 7px;\n"
"margin-top: 2px;\n"
"color: rgb(85, 255, 127);")

        self.label_current_render.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_current_render, 2, 0, 1, 2)


        self.verticalLayout_17.addLayout(self.gridLayout_4)


        self.verticalLayout_14.addWidget(self.frame_content_wid_3)


        self.verticalLayout_18.addWidget(self.frame_div_number_frames)
        ################## 중 단##############

        self.frame_div_table_widget = QFrame(self.page_home)
        self.frame_div_table_widget.setObjectName(u"frame_div_table_widget")
        self.frame_div_table_widget.setMinimumSize(QSize(0, 60))

        self.frame_div_table_widget.setStyleSheet(u"background-color: rgb(41, 45, 57);\n"
"border-radius: 10px;\n"
"")################## 버튼라인 백그라운드 ##############
        self.frame_div_table_widget.setFrameShape(QFrame.NoFrame)
        self.frame_div_table_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_div_table_widget)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_4 = QFrame(self.frame_div_table_widget)
        self.frame_title_wid_4.setObjectName(u"frame_title_wid_4")
        self.frame_title_wid_4.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_4.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_4.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_title_wid_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.labelBoxBlenderInstalation_4 = QLabel(self.frame_title_wid_4)
        self.labelBoxBlenderInstalation_4.setObjectName(u"labelBoxBlenderInstalation_4")
        font5 = QFont()
        font5.setFamily(u"Roboto Light")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.labelBoxBlenderInstalation_4.setFont(font5)
        self.labelBoxBlenderInstalation_4.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.labelBoxBlenderInstalation_4)
        self.verticalLayout_20.addWidget(self.frame_title_wid_4)


        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")

        self.lineEdit_color_tem = QLineEdit(self.frame_div_table_widget)

        self.lineEdit_color_tem.setObjectName(u"lineEdit_color_tem")
        self.lineEdit_color_tem.setMaximumSize(QSize(75, 20))

        self.shadow3 = QGraphicsDropShadowEffect()
        self.shadow3.setYOffset(1)
        self.shadow3.setXOffset(1)
        self.shadow3.setBlurRadius(5)
        self.shadow3.setColor(QColor("black"))
        self.lineEdit_color_tem.setGraphicsEffect(self.shadow3)
        self.lineEdit_color_tem.setFont(font5)
        self.lineEdit_color_tem.setStyleSheet(u"QLineEdit {\n"
                                         "	background-color: rgb(52,59, 72);\n"
                                           "	border-radius: 10px;\n"
                                           "	border: 2px solid rgb(52,59, 72);\n"
                                           "	padding: 0px;\n"
                                           "	selection-background-color: rgb(85, 170, 255);\n"
                                           "}\n"
                                           "QLineEdit:hover {\n"
                                           "	border: 2px solid rgb(44, 49, 60);\n"
                                           "}\n"
                                           "QLineEdit:focus {\n"
                                           "	border: 2px solid rgb(85, 170, 255);\n"
                                           "	background-color: rgb(27, 29, 35);\n"
                                           "}")

        self.lineEdit_color_tem.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_color_tem, 0, 1, 1, 1)

        self.horizontalSlider2 = QSlider(self.frame_div_table_widget)
        self.horizontalSlider2.setRange(100,1000)
        self.horizontalSlider2.setObjectName(u"horizontalSlider")
        self.horizontalSlider2.setStyleSheet(u"")
        self.horizontalSlider2.setOrientation(Qt.Horizontal)
        self.horizontalSlider2.setTickInterval(10)
        self.horizontalSlider2.valueChanged.connect(self.changeValue)

        self.gridLayout_6.addWidget(self.horizontalSlider2, 0, 0, 1, 1)

        self.verticalLayout_20.addLayout(self.gridLayout_6)
        self.verticalLayout_18.addWidget(self.frame_div_table_widget)






        ################## 하단##############


        self.frame_div_render_time = QFrame(self.page_home)
        self.frame_div_render_time.setObjectName(u"frame_div_render_time")
        self.frame_div_render_time.setMinimumSize(QSize(0, 60))
        self.frame_div_render_time.setMaximumSize(QSize(390, 170))
        self.frame_div_render_time.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 10px;\n"
"")

        self.frame_div_number_frames.setFrameShape(QFrame.NoFrame)
        self.frame_div_number_frames.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_div_render_time)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_5 = QFrame(self.frame_div_number_frames)
        self.frame_title_wid_5.setObjectName(u"frame_title_wid_4")
        self.frame_title_wid_5.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_5.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_5.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_title_wid_5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_16")
        self.labelBoxBlenderInstalation_5 = QLabel(self.frame_title_wid_3)
        self.labelBoxBlenderInstalation_5.setObjectName(u"labelBoxBlenderInstalation_5")
        self.labelBoxBlenderInstalation_5.setFont(font5)
        self.labelBoxBlenderInstalation_5.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.labelBoxBlenderInstalation_5)

        self.verticalLayout_19.addWidget(self.frame_title_wid_5)

        self.frame_div_render_time.setFrameShape(QFrame.StyledPanel)
        self.frame_div_render_time.setFrameShadow(QFrame.Raised)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_render_time = QLabel(self.frame_div_render_time)
        self.label_render_time.setObjectName(u"label_render_time")
        font8 = QFont()
        font8.setFamily(u"Roboto Thin")
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_render_time.setFont(font8)
        self.label_render_time.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.label_render_time.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_render_time, 0, 0, 1, 2)

        self.MusicButton = QPushButton()
        self.shadow4 = QGraphicsDropShadowEffect()
        self.shadow4.setYOffset(2)
        self.shadow4.setXOffset(2)
        self.shadow4.setBlurRadius(10)
        self.shadow4.setColor(QColor("black"))
        self.MusicButton.setGraphicsEffect(self.shadow4)
        self.MusicButton.setObjectName(u"DialogButton")
        self.MusicButton.setMinimumSize(QSize(100, 60))
        self.MusicButton.setFont(font6)
        self.MusicButton.setStyleSheet(u"QPushButton {\n"
                                        "	border: 2px solid rgb(52, 59, 72);\n"
                                        "	border-radius: 10px;	\n"
                                        "	background-color: rgb(52, 59, 72);\n"
                                        "	padding-right: 5px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(57, 65, 80);\n"
                                        "	border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color: rgb(35, 40, 49);\n"
                                        "	border: 2px solid rgb(43, 50, 61);\n"
                                        "}")

        self.MusicButton.clicked.connect(self.Music_checkClicked)
        self.gridLayout_5.addWidget(self.MusicButton, 0, 0, 2, 0)


################## ESTIMATED RENDER TIME##############


        self.verticalLayout_19.addLayout(self.gridLayout_5)
        self.verticalLayout_18.addWidget(self.frame_div_render_time)
        self.stackedWidget.addWidget(self.page_home)


################## 2페이지 ##############

        self.groupBox=QGroupBox()
        self.grid=QGridLayout()
        self.page_info=QWidget()
        self.page_info.setStyleSheet("border:None")
        self.page_info.setLayout(self.grid)


        text = ['Spring Cherry Blossom', 'Midnight Summer Sea', 'Autumnal Colors', 'Winter Snow Mountains', 'Sunflower', 'Before Sunset']
        sub=['Feel the Midnigt Summer Sea','Feel the Spring Cherry Blossom'
            ,'Feel Spring Cherry Blossom','Feel Spring Cherry Blossom',
             'Feel Spring Cherry Blossom','Feel Spring Cherry Blossom']
        # text = ["", '', '', '', '', '']
        self.pushbtns = []
        self.labelList = []
        self.subList=[]
        self.shadowlist2=[]
        for i in range(len(text)):


            self.pushbtns.append(QPushButton())

            self.labelList.append(QLabel(text[i]))
            self.subList.append(QLabel(sub[i]))

            self.pushbtns[i].setContentsMargins(0, 0, 0,0)



            self.grid.addWidget(self.pushbtns[i],i*3,0)
            self.grid.addWidget(self.labelList[i],i*3+1,0)
            # self.grid.addWidget(self.subList[i],i*3+2,0)



            self.labelList[i].setAlignment(Qt.AlignLeft)
            self.labelList[i].setFont(font3)
            self.subList[i].setAlignment(Qt.AlignLeft)
            self.subList[i].setFont(font2)

            self.subList[i].setStyleSheet(
                                          'background-color:rgb(39, 44, 54);'
                                          'padding:10px;'
                                          )
            self.shadowlist2.append(QGraphicsDropShadowEffect())
            self.shadowlist2[i].setXOffset(0)
            self.shadowlist2[i].setYOffset(10)
            self.shadowlist2[i].setBlurRadius(10)
            self.shadowlist2[i].setColor(QColor(rgb=(39, 44, 54)))
            self.pushbtns[i].setGraphicsEffect(self.shadowlist2[i])


            # self.pushbtns[i].setMaximumHeight(200)
            # self.pushbtns[i].setMaximumWidth(300)
        self.pushbtns[0].setIcon(QtGui.QIcon())
        self.pushbtns[0].setStyleSheet(u"background-image: url(scene/spring.jpg);\n"
                                       "background-position: center;\n"
                                       "background-repeat: no-repeat;\n"
                                       'margin-bottom:5px;')
        self.pushbtns[0].setIconSize(QSize(100, 250))
        self.pushbtns[0].clicked.connect(lambda: self.sceneClicked(0))
        self.labelList[0].setStyleSheet(
            'background-color:rgb(29, 34, 44);'
            'padding:15px;'


        )
        self.pushbtns[1].setIcon(QtGui.QIcon())
        self.pushbtns[1].setStyleSheet(u"background-image: url(scene/summer.jpg);\n"
                                       "background-position: center;\n"
                                       "background-repeat: no-repeat;\n"
                                       "margin-bottom:5px;")
        self.pushbtns[1].setIconSize(QSize(100, 230))
        self.pushbtns[1].clicked.connect(lambda: self.sceneClicked(1))
        self.labelList[1].setStyleSheet(
            'background-color:rgb(29, 34, 44);'
            'padding:15px;'

        )

        self.pushbtns[2].setIcon(QtGui.QIcon())
        self.pushbtns[2].setStyleSheet(u"background-image: url(scene/1920fall2.jpg);\n"
                                       "background-position: center;\n"
                                       "background-repeat: no-repeat;\n"
                                       "margin-bottom:5px;")
        self.pushbtns[2].setIconSize(QSize(100, 240))
        self.pushbtns[2].clicked.connect(lambda: self.sceneClicked(2))
        self.labelList[2].setStyleSheet(
            'background-color:rgb(29, 34, 44);'
            'padding:15px;'

        )
        self.pushbtns[3].setIcon(QtGui.QIcon())
        self.pushbtns[3].setStyleSheet(u"background-image: url(scene/1920winter2.jpg);\n"
                                       "background-position: center;\n"
                                       "background-repeat: no-repeat;\n"
                                       "margin-bottom:5px;")
        self.pushbtns[3].setIconSize(QSize(100, 240))
        self.pushbtns[3].clicked.connect(lambda: self.sceneClicked(3))
        self.labelList[3].setStyleSheet(
            'background-color:rgb(29, 34, 44);'
            'padding:15px;'

        )

        self.pushbtns[4].setIcon(QtGui.QIcon())
        self.pushbtns[4].setStyleSheet(u"background-image: url(scene/1920sunflowe.jpg);\n"
                                       "background-position: center;\n"
                                       "background-repeat: no-repeat;\n"
                                       "margin-bottom:5px;")
        self.pushbtns[4].setIconSize(QSize(100, 240))
        self.pushbtns[4].clicked.connect(lambda: self.sceneClicked(4))
        self.labelList[4].setStyleSheet(
            'background-color:rgb(29, 34, 44);'
            'padding:15px;'

        )

        self.pushbtns[5].setIcon(QtGui.QIcon())
        self.pushbtns[5].setStyleSheet(u"background-image: url(scene/1920노을.jpg);\n"
                                       "background-position: center;\n"
                                       "background-repeat: no-repeat;\n"
                                       "margin-bottom:5px;")
        self.pushbtns[5].setIconSize(QSize(100, 240))
        self.pushbtns[5].clicked.connect(lambda: self.sceneClicked(5))
        self.labelList[5].setStyleSheet(
            'background-color:rgb(29, 34, 44);'
            'padding:15px;'

        )


        self.drawType = 0

        self.groupBox.setLayout(self.grid)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.groupBox)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFixedHeight(650)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scroll)

        self.page_info.setLayout(self.layout)


#######################################################################################

        self.stackedWidget.addWidget(self.page_info)
        self.verticalLayout_9.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.frame_content)
##하단###
        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.DialogButton)
        QWidget.setTabOrder(self.DialogButton, self.lineEdit_machines)
        QWidget.setTabOrder(self.lineEdit_machines, self.horizontalSlider2)
        QWidget.setTabOrder(self.horizontalSlider2,self.lineEdit_color_tem)
        # QWidget.setTabOrder(self.lineEdit_description, self.pushButton_add_render)
        # QWidget.setTabOrder(self.pushButton_add_render, self.tableWidget_renders)
        # QWidget.setTabOrder(self.lineEdit_description,self.tableWidget_renders)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Light Is Right", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"SMART LIGHT 0912", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText("")
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"EMOTION LIGHT", None))


        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("MainWindow", u"COLOR DIALOG", None))
        self.lineEdit_machines.setText(QCoreApplication.translate("MainWindow", u" ", None))
        self.lineEdit_machines.setPlaceholderText(QCoreApplication.translate("MainWindow", u" ", None))
        self.DialogButton.setText("")
        self.labelBoxBlenderInstalation_4.setText(QCoreApplication.translate("MainWindow", u"COLOR TEMPERATURE", None))
        self.lineEdit_color_tem.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1000", None))



        self.labelBoxBlenderInstalation_5.setText(QCoreApplication.translate("MainWindow", u"MUSIC LIGHT", None))

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Ligh IS right", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"2020-10-04", None))

    def emotionClicked(self,i):

          if i == 0:
              Color=QColor('blue')
              self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                                "	background-position: center;\n"
                                                 "	background-repeat: no-reperat;\n"
                                                'background-color:{}'.format(Color.name()))
              self.frame_left_menu.setStyleSheet('background-color: {}'.format(Color.name()))
              self.DialogButton.setStyleSheet('background-color: {}'.format(Color.name()))
              self.lineEdit_machines.setText(Color.name())
              self.hex_to_rgb(Color.name())


          if i== 1:
              Color = QColor('red')
              self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                                 "	background-position: center;\n"
                                                 "	background-repeat: no-reperat;\n"
                                                 'background-color:{}'.format(Color.name()))
              self.frame_left_menu.setStyleSheet('background-color: {}'.format(Color.name()))
              self.DialogButton.setStyleSheet('background-color: {}'.format(Color.name()))
              self.lineEdit_machines.setText(Color.name())
              self.hex_to_rgb(Color.name())
          if i== 2:
              Color = QColor('green')
              self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                                 "	background-position: center;\n"
                                                 "	background-repeat: no-reperat;\n"
                                                 'background-color:{}'.format(Color.name()))
              self.frame_left_menu.setStyleSheet('background-color: {}'.format(Color.name()))
              self.DialogButton.setStyleSheet('background-color: {}'.format(Color.name()))
              self.lineEdit_machines.setText(Color.name())
              self.hex_to_rgb(Color.name())
          if i== 3:
              Color = QColor('yellow')
              self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                                 "	background-position: center;\n"
                                                 "	background-repeat: no-reperat;\n"
                                                 'background-color:{}'.format(Color.name()))
              self.frame_left_menu.setStyleSheet('background-color: {}'.format(Color.name()))
              self.DialogButton.setStyleSheet('background-color: {}'.format(Color.name()))
              self.lineEdit_machines.setText(Color.name())
              self.hex_to_rgb(Color.name())
          if i== 4:
              Color = QColor('purple')
              self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                                 "	background-position: center;\n"
                                                 "	background-repeat: no-reperat;\n"
                                                 'background-color:{}'.format(Color.name()))
              self.frame_left_menu.setStyleSheet('background-color: {}'.format(Color.name()))
              self.DialogButton.setStyleSheet('background-color: {}'.format(Color.name()))
              self.lineEdit_machines.setText(Color.name())
              self.hex_to_rgb(Color.name())
          if i== 5:
              Color = QColor('orange')
              self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                                 "	background-position: center;\n"
                                                 "	background-repeat: no-reperat;\n"
                                                 'background-color:{}'.format(Color.name()))

              self.frame_left_menu.setStyleSheet('background-color: {}'.format(Color.name()))
              self.DialogButton.setStyleSheet('background-color: {}'.format(Color.name()))
              self.lineEdit_machines.setText(Color.name())
              self.hex_to_rgb(Color.name())

          return Color
    def sceneClicked(self,i):
        if i == 0:

            Color1 = QColor(252, 85, 222).name()
            Color1 = Color1.lstrip('#')
            Color1 = tuple(int(Color1[i:i + 2], 16) for i in (0, 2, 4))
            Color2 = QColor(255, 40, 255).name()
            Color2 = Color2.lstrip('#')
            Color2 = tuple(int(Color2[i:i + 2], 16) for i in (0, 2, 4))
            Color3 = QColor(251, 70, 215).name()
            Color3 = Color3.lstrip('#')
            Color3 = tuple(int(Color3[i:i + 2], 16) for i in (0, 2, 4))
            scene1 = self.convert(Color1[0]) + self.convert(Color1[1]) + self.convert(Color1[2])
            scene2 = self.convert(Color2[0]) + self.convert(Color2[1]) + self.convert(Color2[2])
            scene3 = self.convert(Color3[0]) + self.convert(Color3[1]) + self.convert(Color3[2])
            scene = scene1 + scene2 + scene3
            print(scene)
            self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                               "	background-position: center;\n"
                                               "	background-repeat: no-reperat;\n"
                                               "border:None;\n"
                                               'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:0 rgb(252, 85, 222), stop:1 rgb(255, 40, 255),stop:2 rgb(251, 70, 215));')
            self.frame_left_menu.setStyleSheet(
                'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:0 rgb(252, 85, 222), stop:1 rgb(255, 40, 255),stop:2 rgb(251, 70, 215));')

            self.scene_to_rgb(scene)

        if i == 1:
            Color1 = QColor(120, 234, 246).name()
            Color1 = Color1.lstrip('#')
            Color1 = tuple(int(Color1[i:i + 2], 16) for i in (0, 2, 4))
            # Color2 = QColor(87, 226, 245).name()
            Color2 = QColor(25, 175, 200).name()
            Color2 = Color2.lstrip('#')
            Color2 = tuple(int(Color2[i:i + 2], 16) for i in (0, 2, 4))
            Color3 = QColor(87, 226, 247).name()

            Color3 = Color3.lstrip('#')
            Color3 = tuple(int(Color3[i:i + 2], 16) for i in (0, 2, 4))
            scene1 = self.convert(Color1[0]) + self.convert(Color1[1]) + self.convert(Color1[2])
            scene2 = self.convert(Color2[0]) + self.convert(Color2[1]) + self.convert(Color2[2])
            scene3 = self.convert(Color3[0]) + self.convert(Color3[1]) + self.convert(Color3[2])
            scene = scene1 + scene2 + scene3
            print(scene)

            self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                               "	background-position: center;\n"
                                               "	background-repeat: no-reperat;\n"
                                               "border:None;\n"
                                               'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:1 rgb(120, 234, 246), stop:2 rgb(25, 175, 200),stop:3 rgb(87, 226, 247));')
            # self.frame_left_menu.setStyleSheet('background-color: {}'.format(color.name()))
            self.frame_left_menu.setStyleSheet(
                'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:1 rgb(120, 234, 246), stop:2 rgb(25, 175, 200),stop:3 rgb(87, 226, 247));')

            self.scene_to_rgb(scene)
        if i == 2:
            Color1 = QColor(211, 105, 35).name()
            Color1 = Color1.lstrip('#')
            Color1 = tuple(int(Color1[i:i + 2], 16) for i in (0, 2, 4))
            # Color2 = QColor(211, 105, 35).name()
            Color2 = QColor(153, 32, 12).name()
            Color2 = Color2.lstrip('#')
            Color2 = tuple(int(Color2[i:i + 2], 16) for i in (0, 2, 4))
            Color3 = QColor(170, 132, 44).name()
            Color3 = Color3.lstrip('#')
            Color3 = tuple(int(Color3[i:i + 2], 16) for i in (0, 2, 4))
            scene1 = self.convert(Color1[0]) + self.convert(Color1[1]) + self.convert(Color1[2])
            scene2 = self.convert(Color2[0]) + self.convert(Color2[1]) + self.convert(Color2[2])
            scene3 = self.convert(Color3[0]) + self.convert(Color3[1]) + self.convert(Color3[2])
            scene = scene1 + scene2 + scene3
            print(scene)

            self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                               "	background-position: center;\n"
                                               "	background-repeat: no-reperat;\n"
                                               "border:None;\n"
                                               'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:0 rgb(153, 32, 12), stop:1 rgb(211, 105, 35),stop:2 rgb(170, 132, 44));')
            # self.frame_left_menu.setStyleSheet('background-color: {}'.format(color.name()))
            self.frame_left_menu.setStyleSheet(
                'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:0 rgb(153, 32, 12), stop:1 rgb(211, 105, 35),stop:2 rgb(170, 132, 44));')

            self.scene_to_rgb(scene)
        if i == 3:
            Color1 = QColor(158, 164, 174).name()
            Color1 = Color1.lstrip('#')
            Color1 = tuple(int(Color1[i:i + 2], 16) for i in (0, 2, 4))
            Color2 = QColor(38, 65, 108).name()
            Color2 = Color2.lstrip('#')
            Color2 = tuple(int(Color2[i:i + 2], 16) for i in (0, 2, 4))
            Color3 = QColor(22, 22, 22).name()
            Color3 = Color3.lstrip('#')
            Color3 = tuple(int(Color3[i:i + 2], 16) for i in (0, 2, 4))
            scene1 = self.convert(Color1[0]) + self.convert(Color1[1]) + self.convert(Color1[2])
            scene2 = self.convert(Color2[0]) + self.convert(Color2[1]) + self.convert(Color2[2])
            scene3 = self.convert(Color3[0]) + self.convert(Color3[1]) + self.convert(Color3[2])
            scene = scene1 + scene2 + scene3
            print(scene)

            self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                               "	background-position: center;\n"
                                               "	background-repeat: no-reperat;\n"
                                               "border:None;\n"
                                               'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:0 rgb(158, 164, 174), stop:1 rgb(38, 65, 108),stop:2 rgb(22,22, 22));')
            # self.frame_left_menu.setStyleSheet('background-color: {}'.format(color.name()))
            self.frame_left_menu.setStyleSheet(
                'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:0 rgb(158, 164, 174), stop:1 rgb(38, 65, 108),stop:2 rgb(22,22, 22));')

            self.scene_to_rgb(scene)
        if i == 4:
            Color1 = QColor(170, 0, 255).name()
            Color1 = Color1.lstrip('#')
            Color1 = tuple(int(Color1[i:i + 2], 16) for i in (0, 2, 4))
            Color2 = QColor(255, 170, 255).name()
            Color2 = Color2.lstrip('#')
            Color2 = tuple(int(Color2[i:i + 2], 16) for i in (0, 2, 4))
            Color3 = QColor(232, 191, 141).name()
            Color3 = Color3.lstrip('#')
            Color3 = tuple(int(Color3[i:i + 2], 16) for i in (0, 2, 4))
            scene1 = self.convert(Color1[0]) + self.convert(Color1[1]) + self.convert(Color1[2])
            scene2 = self.convert(Color2[0]) + self.convert(Color2[1]) + self.convert(Color2[2])
            scene3 = self.convert(Color3[0]) + self.convert(Color3[1]) + self.convert(Color3[2])
            scene = scene1 + scene2 + scene3
            print(scene)

            self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                               "	background-position: center;\n"
                                               "	background-repeat: no-reperat;\n"
                                               "border:None;\n"
                                               'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:0 rgb(170, 0, 255), stop:1 rgb(255, 170, 255),stop:2 rgb(232, 191, 141));')
            # self.frame_left_menu.setStyleSheet('background-color: {}'.format(color.name()))
            self.frame_left_menu.setStyleSheet(
                'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:0 rgb(170, 0, 255), stop:1 rgb(255, 170, 255),stop:2 rgb(232, 191, 141));')

            self.scene_to_rgb(scene)

        if i == 5:
            Color1 = QColor(72, 97, 145).name()
            Color1 = Color1.lstrip('#')
            Color1 = tuple(int(Color1[i:i + 2], 16) for i in (0, 2, 4))
            Color2 = QColor(222, 202, 175).name()
            Color2 = Color2.lstrip('#')
            Color2 = tuple(int(Color2[i:i + 2], 16) for i in (0, 2, 4))
            Color3 = QColor(70, 32, 14).name()
            Color3 = Color3.lstrip('#')
            Color3 = tuple(int(Color3[i:i + 2], 16) for i in (0, 2, 4))
            scene1 = self.convert(Color1[0]) + self.convert(Color1[1]) + self.convert(Color1[2])
            scene2 = self.convert(Color2[0]) + self.convert(Color2[1]) + self.convert(Color2[2])
            scene3 = self.convert(Color3[0]) + self.convert(Color3[1]) + self.convert(Color3[2])
            scene = scene1 + scene2 + scene3
            print(scene)

            self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                               "	background-position: center;\n"
                                               "	background-repeat: no-reperat;\n"
                                               "border:None;\n"
                                               'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:0 rgb(72, 97, 145), stop:1 rgb(222, 202, 175),stop:2 rgb(70, 32, 14));')
            # self.frame_left_menu.setStyleSheet('background-color: {}'.format(color.name()))
            self.frame_left_menu.setStyleSheet(
                'background-color: qlineargradient(spread:pad,x1:0, y1:0.5, x2:0.5, y2:0.5,x3:1,y3:0.5, stop:0 rgb(72, 97, 145), stop:1 rgb(222, 202, 175),stop:2 rgb(70, 32, 14));')

            self.scene_to_rgb(scene)
    def scene_to_rgb(self, scene):
        s.send(scene.encode(encoding='utf_8', errors='strict'))

    def hex_to_rgb(self, hex):
        hex = hex.lstrip('#')
        print("hex",hex)
        a = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
        led = self.convert(a[0]) + self.convert(a[1]) + self.convert(a[2])
        print("led",led)
        s.send(led.encode(encoding='utf_8', errors='strict'))


    def convert(self, data):
        data = int(data)
        if len(str(data)) == 3:
            return str(data)

        elif len(str(data)) == 2:
            data = "0" + str(data)
            return data

        elif len(str(data)) == 1:
            data = "00" + str(data)
            return data

    def showColorDlg(self):
        # 색상 대화상자 생성
        color = QColorDialog.getColor()

        # 색상이 유효한 값이면 참, QFrame에 색 적용
        if color.isValid():
            self.lightcolor = color
            self.DialogButton.setStyleSheet('background-color: {}'.format(color.name()))
            # self.view.scene.setBackgroundBrush(color)
            self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                               "	background-position: center;\n"
                                               "	background-repeat: no-reperat;\n"
                                               'background-color:{}'.format(color.name()))
            self.frame_left_menu.setStyleSheet('background-color: {}'.format(color.name()))

            self.lineEdit_machines.setText(color.name())
            self.hex_to_rgb(color.name())

        return color
    def changeValue(self):
        strip_num=60
        temp = self.horizontalSlider2.value()*10
        print("temp:",str(temp))
        # self.lineEdit_color_tem.setText(str(temp))
        self.lineEdit_color_tem.setText(str(temp))
        color = self.colorTemperatureToRGB(temp)
        convert_color = QColor(color["r"], color["g"], color["b"])
        print("convert_color", convert_color.name())

        hex = convert_color.name().lstrip('#')
        a = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
        led = self.convert(a[0]) + self.convert(a[1]) + self.convert(a[2])
        print("led", led)
        # s.send(led.encode(encoding='utf_8', errors='strict'))
        # data = s.recv(1024)
        # print('result: ' + data.decode())

        # self.view.scene.setBackgroundBrush(convert_color)
        self.btn_toggle_menu.setStyleSheet("	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-reperat;\n"
                                           'background-color:{}'.format(convert_color.name()))
        self.frame_left_menu.setStyleSheet('background-color: {}'.format(convert_color.name()))

        self.lineEdit_machines.setText(convert_color.name())
        self.DialogButton.setStyleSheet('background-color: {}'.format(convert_color.name()))

        return convert_color



    def inputValue(self):

        temp=self.lineEdit_machines()
        color=self.colorTemperatureToRGB(temp)
        self.input_text.setText(str(temp))
        print('RGB=', "(", color["r"], color["g"], color["b"], ")")

    def clamp(self,x,min,max):
        if x<min :
            return min
        elif x>max:
            return max
        return x

    def colorTemperatureToRGB(self, kelvin):
        temp = kelvin / 100
        if temp <= 66:
            red = 255
            green = temp
            green = 99.4708025861 * math.log(green) - 161.1195681661

            if temp <= 19:
                blue = 0
            else:
                blue = temp - 10
                blue = 138.5177312231 * math.log(blue) - 305.0447927307
        else:
            red = temp - 60
            red = 329.698727446 * math.pow(red, -0.1332047592)

            green = temp - 60
            green = 288.1221695283 * math.pow(green, -0.0755148492)

            blue = 255

        return {'r': int(self.clamp(red, 0, 255)), 'g': int(self.clamp(green, 0, 255)),
                'b': int(self.clamp(blue, 0, 255))}

    def Music_checkClicked(self):

        th2=Thread(target=self.mic1,args=())
        th1 =Thread(target=self.mic2,args=())
        th1.start()
        th2.start()






    def microphonedata(self):

        self.pred = np.zeros(8)
        self.model = load_model('custom_cnn_2d_78.h5')

        chunk = 33000  # 3000ms ->3초 33000
        Format = pyaudio.paFloat32
        channels = 1
        rate = 22050

        p2 = pyaudio.PyAudio()
        chosen_device_index = -1

        stream2 = p2.open(format=Format,
                          channels=channels,
                          rate=rate,
                          input_device_index=chosen_device_index,
                          input=True,
                          output=True,
                          frames_per_buffer=chunk)

        #################################################################################
        p1 = pyaudio.PyAudio()
        frames_per_buffer = int(config.MIC_RATE / config.FPS)
        stream1 = p1.open(format=pyaudio.paInt16,
                          channels=1,
                          rate=config.MIC_RATE,
                          input=True,
                          frames_per_buffer=frames_per_buffer)
        overflows = 0
        prev_ovf_time = time.time()

        while True:
            try:
                ###############음악 데이터##############
                y = np.fromstring(stream1.read(frames_per_buffer, exception_on_overflow=False), dtype=np.int16)
                y = y.astype(np.float32)
                # stream1.read(stream1.get_read_available(), exception_on_overflow=False)
                s.send(y)
                data = s.recv(1024)
                # print("y:", y)
                print(y.shape)

            ###############장르 데이터##############
            # data2 = stream2.read(chunk)
            # data_float = struct.unpack(str(chunk) + 'f', data2)
            # y2=np.fromstring(data_float)
            # x = librosa.feature.melspectrogram(np.array(data_float), n_fft=1024,
            #                                    hop_length=256, n_mels=128)
            # x = x.reshape(1, 128, 129, 1)
            # print(x)
            # self.dopreds(x, self.model)

            except IOError:
                overflows += 1
                if time.time() > prev_ovf_time + 1:
                    prev_ovf_time = time.time()
                    print('Audio buffer has overflowed {} times'.format(overflows))
        stream1.stop_stream()
        stream2.stop_stream()
        stream1.close()
        stream2.close()
        p1.terminate()
        p2.terminate()




    def mic1(self):
        overflows = 0
        prev_ovf_time = time.time()
        p1 = pyaudio.PyAudio()
        frames_per_buffer = int(config.MIC_RATE / config.FPS)

        stream1 = p1.open(format=pyaudio.paInt16,
                          channels=1,
                          rate=config.MIC_RATE,
                          input=True,
                          frames_per_buffer=frames_per_buffer)
        overflows = 0
        prev_ovf_time = time.time()

        while True:
            try:

                y = np.fromstring(stream1.read(frames_per_buffer, exception_on_overflow=False), dtype=np.int16)
                y = y.astype(np.float32)
                # print("y:",len(y),y)
                stream1.read(stream1.get_read_available(), exception_on_overflow=False)



                s.send(y)
                data = s.recv(1024)

                # print("y:", y)
                # print(y.shape)
                # p1.terminate()
            except IOError:
                overflows += 1
                if time.time() > prev_ovf_time + 1:
                    prev_ovf_time = time.time()
                    print('Audio buffer has overflowed {} times'.format(overflows))
        stream1.stop_stream()
        stream1.close()
        p1.terminate()


    def mic2(self):
        overflows = 0
        prev_ovf_time = time.time()
        self.pred = np.zeros(8)
        xValue = self.pred
        self.model = load_model('custom_cnn_2d_78.h5')

        chunk = 33000  # 3000ms ->3초 33000
        Format = pyaudio.paFloat32
        channels = 1
        rate = 22050

        p2 = pyaudio.PyAudio()
        chosen_device_index = -1

        stream2 = p2.open(format=Format,
                          channels=channels,
                          rate=rate,
                          input_device_index=chosen_device_index,
                          input=True,
                          output=True,
                          frames_per_buffer=chunk)

        tick_label = ['Ballad', 'Classical', 'Trot', 'HipHop', 'Jazz', 'Dance', 'Reggae', 'Rock/Metal']
        color = ["yellow", QColor(120, 50, 5).name(), QColor(170, 85, 255).name(), "blue", "orange", "purple", "green", "red"]
        # color = ["yellow", "brown", "pink", "blue", "orange", "purple", "green","red"]

        while True:
            try:
                data2 = stream2.read(chunk)
                data_float = struct.unpack(str(chunk) + 'f', data2)

                x = librosa.feature.melspectrogram(np.array(data_float), n_fft=1024,
                                                   hop_length=256, n_mels=128)
                x = x.reshape(1, 128, 129, 1)
                preds = self.model.predict(x)
                # print("preds",preds)
                preds = np.array(
                    [preds[0, 0] + preds[0, 2], preds[0, 1], preds[0, 3], preds[0, 4], preds[0, 5], preds[0, 7],
                     preds[0, 8],
                     preds[0, 9] + preds[0, 6]])
                self.pred = (preds + (3 * self.pred)) / 4


                # i = np.argmax(xValue)
                # print("asd:",tick_label[i],color[i])
                # print("###########################")

                i = np.argmax(self.pred)
                print("asd:",  np.argmax(self.pred),tick_label[i], color[i])
                Color = QColor(color[i])
                print("Color name :", Color.name())
                print("###########################")

                self.hex_to_rgb_music(Color.name(),i)



            except IOError:
                overflows += 1
                if time.time() > prev_ovf_time + 1:
                    prev_ovf_time = time.time()
                    print('Audio buffer has overflowed {} times'.format(overflows))
        stream2.stop_stream()
        stream2.close()
        p2.terminate()

    def hex_to_rgb_music(self, hex,i):
        hex = hex.lstrip('#')
        print("hex2", hex)
        a = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
        led = str(i)+self.convert(a[0]) + self.convert(a[1]) + self.convert(a[2])
        print("led", led)
        s.send(led.encode(encoding='utf_8', errors='strict'))




    def dopreds(self,x, model):
        # global pred
        preds = model.predict(x)
        # print("preds",preds)
        preds = np.array(
            [preds[0, 0] + preds[0, 2], preds[0, 1], preds[0, 3], preds[0, 4], preds[0, 5], preds[0, 7], preds[0, 8],
             preds[0, 9] + preds[0, 6]])
        self.pred = (preds + (3 * self.pred)) / 4
        print("asd:",np.argmax(self.pred))
        print("###########################")