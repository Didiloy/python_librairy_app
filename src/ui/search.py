# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/search.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(79, 70, 721, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButtonSearch = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.gridLayout.addWidget(self.pushButtonSearch, 0, 2, 1, 1)
        self.lineEditSearch = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEditSearch.setInputMask("")
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.gridLayout.addWidget(self.lineEditSearch, 0, 1, 1, 1)
        self.answerLabel = QtWidgets.QLabel(self.centralwidget)
        self.answerLabel.setGeometry(QtCore.QRect(200, 280, 521, 181))
        self.answerLabel.setText("")
        self.answerLabel.setObjectName("answerLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
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
        self.label.setText(_translate("MainWindow", "Chercher quelque chose :"))
        self.pushButtonSearch.setText(_translate("MainWindow", "Rechercher"))
        self.lineEditSearch.setText(_translate("MainWindow", "Rechercher.."))
