# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftPanel = QtWidgets.QWidget(self.centralwidget)
        self.leftPanel.setMinimumSize(QtCore.QSize(210, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leftPanel.setFont(font)
        self.leftPanel.setStyleSheet("background-color : #464646;")
        self.leftPanel.setObjectName("leftPanel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameLeftPanel = QtWidgets.QFrame(self.leftPanel)
        self.frameLeftPanel.setStyleSheet("background-color : #464646;")
        self.frameLeftPanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLeftPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLeftPanel.setObjectName("frameLeftPanel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameLeftPanel)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.leftPanelButtonSearch = QtWidgets.QPushButton(self.frameLeftPanel)
        self.leftPanelButtonSearch.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leftPanelButtonSearch.setFont(font)
        self.leftPanelButtonSearch.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius : 0px;\n"
"    border-left: 3px solid #464646;\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid #848484;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border-left: 3px solid #323232;\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/assets/res/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftPanelButtonSearch.setIcon(icon)
        self.leftPanelButtonSearch.setIconSize(QtCore.QSize(25, 25))
        self.leftPanelButtonSearch.setObjectName("leftPanelButtonSearch")
        self.verticalLayout_2.addWidget(self.leftPanelButtonSearch)
        self.leftPanelButtonHome = QtWidgets.QPushButton(self.frameLeftPanel)
        self.leftPanelButtonHome.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leftPanelButtonHome.setFont(font)
        self.leftPanelButtonHome.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius : 0px;\n"
"    border-left: 3px solid #464646;\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid #848484;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border-left: 3px solid #323232;\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/assets/res/recommendation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftPanelButtonHome.setIcon(icon1)
        self.leftPanelButtonHome.setIconSize(QtCore.QSize(25, 25))
        self.leftPanelButtonHome.setObjectName("leftPanelButtonHome")
        self.verticalLayout_2.addWidget(self.leftPanelButtonHome)
        self.leftPanelButtonBibliotheque = QtWidgets.QPushButton(self.frameLeftPanel)
        self.leftPanelButtonBibliotheque.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leftPanelButtonBibliotheque.setFont(font)
        self.leftPanelButtonBibliotheque.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius : 0px;\n"
"    border-left: 3px solid #464646;\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid #848484;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border-left: 3px solid #323232;\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/assets/res/bookshelf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftPanelButtonBibliotheque.setIcon(icon2)
        self.leftPanelButtonBibliotheque.setIconSize(QtCore.QSize(25, 25))
        self.leftPanelButtonBibliotheque.setObjectName("leftPanelButtonBibliotheque")
        self.verticalLayout_2.addWidget(self.leftPanelButtonBibliotheque)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frameLeftPanel)
        self.horizontalLayout.addWidget(self.leftPanel)
        self.centerPanel = QtWidgets.QVBoxLayout()
        self.centerPanel.setObjectName("centerPanel")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.searchWidget = QtWidgets.QWidget()
        self.searchWidget.setStyleSheet("")
        self.searchWidget.setObjectName("searchWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.searchWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayoutSearchWidget = QtWidgets.QGridLayout()
        self.gridLayoutSearchWidget.setObjectName("gridLayoutSearchWidget")
        self.gridLayoutSearchBar = QtWidgets.QGridLayout()
        self.gridLayoutSearchBar.setContentsMargins(-1, 20, -1, 20)
        self.gridLayoutSearchBar.setObjectName("gridLayoutSearchBar")
        self.searchButton = QtWidgets.QPushButton(self.searchWidget)
        self.searchButton.setIcon(icon)
        self.searchButton.setIconSize(QtCore.QSize(20, 20))
        self.searchButton.setObjectName("searchButton")
        self.gridLayoutSearchBar.addWidget(self.searchButton, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutSearchBar.addItem(spacerItem1, 0, 0, 1, 1)
        self.searchLineEdit = QtWidgets.QLineEdit(self.searchWidget)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.gridLayoutSearchBar.addWidget(self.searchLineEdit, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutSearchBar.addItem(spacerItem2, 0, 3, 1, 1)
        self.gridLayoutSearchWidget.addLayout(self.gridLayoutSearchBar, 0, 0, 1, 1)
        self.scrollAreaSearch = QtWidgets.QScrollArea(self.searchWidget)
        self.scrollAreaSearch.setWidgetResizable(True)
        self.scrollAreaSearch.setObjectName("scrollAreaSearch")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 842, 586))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelRechercheEnCours = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRechercheEnCours.sizePolicy().hasHeightForWidth())
        self.labelRechercheEnCours.setSizePolicy(sizePolicy)
        self.labelRechercheEnCours.setMinimumSize(QtCore.QSize(300, 20))
        self.labelRechercheEnCours.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelRechercheEnCours.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelRechercheEnCours.setText("")
        self.labelRechercheEnCours.setObjectName("labelRechercheEnCours")
        self.verticalLayout_5.addWidget(self.labelRechercheEnCours, 0, QtCore.Qt.AlignHCenter)
        self.widgetScrollAreaSearchAnswer = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widgetScrollAreaSearchAnswer.setObjectName("widgetScrollAreaSearchAnswer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetScrollAreaSearchAnswer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widgetWidgetScrollAreaSearchAnswer = QtWidgets.QWidget(self.widgetScrollAreaSearchAnswer)
        self.widgetWidgetScrollAreaSearchAnswer.setObjectName("widgetWidgetScrollAreaSearchAnswer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widgetWidgetScrollAreaSearchAnswer)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_2.addWidget(self.widgetWidgetScrollAreaSearchAnswer, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.widgetScrollAreaSearchAnswer)
        self.scrollAreaSearch.setWidget(self.scrollAreaWidgetContents)
        self.gridLayoutSearchWidget.addWidget(self.scrollAreaSearch, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayoutSearchWidget)
        self.stackedWidget.addWidget(self.searchWidget)
        self.bookDetailWidget = QtWidgets.QWidget()
        self.bookDetailWidget.setObjectName("bookDetailWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.bookDetailWidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.bookDetailCoverWidget = QtWidgets.QWidget(self.bookDetailWidget)
        self.bookDetailCoverWidget.setObjectName("bookDetailCoverWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.bookDetailCoverWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.bookDetailCoverLabel = QtWidgets.QLabel(self.bookDetailCoverWidget)
        self.bookDetailCoverLabel.setMinimumSize(QtCore.QSize(200, 260))
        self.bookDetailCoverLabel.setText("")
        self.bookDetailCoverLabel.setObjectName("bookDetailCoverLabel")
        self.verticalLayout_8.addWidget(self.bookDetailCoverLabel, 0, QtCore.Qt.AlignHCenter)
        self.bookDetailTitleLabel = QtWidgets.QLabel(self.bookDetailCoverWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bookDetailTitleLabel.setFont(font)
        self.bookDetailTitleLabel.setText("")
        self.bookDetailTitleLabel.setObjectName("bookDetailTitleLabel")
        self.verticalLayout_8.addWidget(self.bookDetailTitleLabel, 0, QtCore.Qt.AlignLeft)
        self.bookDetailAuthorLabel = QtWidgets.QLabel(self.bookDetailCoverWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bookDetailAuthorLabel.setFont(font)
        self.bookDetailAuthorLabel.setText("")
        self.bookDetailAuthorLabel.setObjectName("bookDetailAuthorLabel")
        self.verticalLayout_8.addWidget(self.bookDetailAuthorLabel)
        self.verticalLayout_7.addWidget(self.bookDetailCoverWidget)
        self.bookDetailDescriptionWidget = QtWidgets.QWidget(self.bookDetailWidget)
        self.bookDetailDescriptionWidget.setObjectName("bookDetailDescriptionWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.bookDetailDescriptionWidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.bookDetailDescriptionLabel = QtWidgets.QLabel(self.bookDetailDescriptionWidget)
        self.bookDetailDescriptionLabel.setText("")
        self.bookDetailDescriptionLabel.setWordWrap(True)
        self.bookDetailDescriptionLabel.setObjectName("bookDetailDescriptionLabel")
        self.verticalLayout_9.addWidget(self.bookDetailDescriptionLabel)
        self.bookDetaillRetourButton = QtWidgets.QPushButton(self.bookDetailDescriptionWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/assets/res/turn-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookDetaillRetourButton.setIcon(icon3)
        self.bookDetaillRetourButton.setIconSize(QtCore.QSize(25, 25))
        self.bookDetaillRetourButton.setObjectName("bookDetaillRetourButton")
        self.verticalLayout_9.addWidget(self.bookDetaillRetourButton)
        self.verticalLayout_7.addWidget(self.bookDetailDescriptionWidget)
        self.stackedWidget.addWidget(self.bookDetailWidget)
        self.homeWidget = QtWidgets.QWidget()
        self.homeWidget.setStyleSheet("")
        self.homeWidget.setObjectName("homeWidget")
        self.gridlayout_10 = QtWidgets.QGridLayout(self.homeWidget)
        self.gridlayout_10.setObjectName("gridlayout_10")
        self.labelRecommendations = QtWidgets.QLabel(self.homeWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRecommendations.sizePolicy().hasHeightForWidth())
        self.labelRecommendations.setSizePolicy(sizePolicy)
        self.labelRecommendations.setMinimumSize(QtCore.QSize(50, 30))
        self.labelRecommendations.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelRecommendations.setFont(font)
        self.labelRecommendations.setObjectName("labelRecommendations")
        self.gridlayout_10.addWidget(self.labelRecommendations, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.widgetFramesRecommendations = QtWidgets.QWidget(self.homeWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFramesRecommendations.sizePolicy().hasHeightForWidth())
        self.widgetFramesRecommendations.setSizePolicy(sizePolicy)
        self.widgetFramesRecommendations.setMaximumSize(QtCore.QSize(3000, 250))
        self.widgetFramesRecommendations.setObjectName("widgetFramesRecommendations")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widgetFramesRecommendations)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frameRecommendationGenre = QtWidgets.QFrame(self.widgetFramesRecommendations)
        self.frameRecommendationGenre.setStyleSheet("QFrame {\n"
"    border: 1px solid #606060;\n"
"    border-radius: 15px;\n"
"    background-color: #9388b1;\n"
"    margin: 0px 10px opx 10px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 2px solid white;\n"
"}")
        self.frameRecommendationGenre.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRecommendationGenre.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameRecommendationGenre.setObjectName("frameRecommendationGenre")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frameRecommendationGenre)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.buttonRecommendationGenre = QtWidgets.QPushButton(self.frameRecommendationGenre)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonRecommendationGenre.setFont(font)
        self.buttonRecommendationGenre.setStyleSheet("QPushButton{\n"
"    background-color : #9388b1;\n"
"    border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color : #b8aade;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/assets/res/romantic-novel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRecommendationGenre.setIcon(icon4)
        self.buttonRecommendationGenre.setIconSize(QtCore.QSize(50, 50))
        self.buttonRecommendationGenre.setObjectName("buttonRecommendationGenre")
        self.gridLayout_4.addWidget(self.buttonRecommendationGenre, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frameRecommendationGenre, 0, 0, 1, 1)
        self.frameRecommendationAuteur = QtWidgets.QFrame(self.widgetFramesRecommendations)
        self.frameRecommendationAuteur.setStyleSheet("QFrame {\n"
"    border: 1px solid #606060;\n"
"    border-radius: 15px;\n"
"    background-color: #2A6212;\n"
"    margin: 0px 10px opx 10px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 2px solid white;\n"
"}")
        self.frameRecommendationAuteur.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRecommendationAuteur.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameRecommendationAuteur.setObjectName("frameRecommendationAuteur")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frameRecommendationAuteur)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.buttonRecommendationAuteur = QtWidgets.QPushButton(self.frameRecommendationAuteur)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonRecommendationAuteur.setFont(font)
        self.buttonRecommendationAuteur.setStyleSheet("QPushButton{\n"
"    background-color : #2A6212;\n"
"    border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color : #548141;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/assets/res/writer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRecommendationAuteur.setIcon(icon5)
        self.buttonRecommendationAuteur.setIconSize(QtCore.QSize(50, 50))
        self.buttonRecommendationAuteur.setObjectName("buttonRecommendationAuteur")
        self.gridLayout_7.addWidget(self.buttonRecommendationAuteur, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frameRecommendationAuteur, 0, 1, 1, 1)
        self.gridlayout_10.addWidget(self.widgetFramesRecommendations, 1, 0, 1, 1)
        self.frameBlague = QtWidgets.QFrame(self.homeWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameBlague.sizePolicy().hasHeightForWidth())
        self.frameBlague.setSizePolicy(sizePolicy)
        self.frameBlague.setMinimumSize(QtCore.QSize(0, 0))
        self.frameBlague.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frameBlague.setStyleSheet("QFrame {\n"
"    border: 1px solid #606060;\n"
"    border-radius: 15px;\n"
"    background-color: #323232;\n"
"    margin: 0px 10px opx 10px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 2px solid white;\n"
"}")
        self.frameBlague.setObjectName("frameBlague")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frameBlague)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.labelBlague = QtWidgets.QLabel(self.frameBlague)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBlague.sizePolicy().hasHeightForWidth())
        self.labelBlague.setSizePolicy(sizePolicy)
        self.labelBlague.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelBlague.setFont(font)
        self.labelBlague.setStyleSheet("border: none;")
        self.labelBlague.setObjectName("labelBlague")
        self.verticalLayout_13.addWidget(self.labelBlague, 0, QtCore.Qt.AlignHCenter)
        self.widget_2 = QtWidgets.QWidget(self.frameBlague)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollAreaLabelImageBlague = QtWidgets.QScrollArea(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaLabelImageBlague.sizePolicy().hasHeightForWidth())
        self.scrollAreaLabelImageBlague.setSizePolicy(sizePolicy)
        self.scrollAreaLabelImageBlague.setStyleSheet("border: none;")
        self.scrollAreaLabelImageBlague.setWidgetResizable(True)
        self.scrollAreaLabelImageBlague.setObjectName("scrollAreaLabelImageBlague")
        self.scrollAreaLabelImageBlagueWidgetContents = QtWidgets.QWidget()
        self.scrollAreaLabelImageBlagueWidgetContents.setGeometry(QtCore.QRect(0, 0, 580, 284))
        self.scrollAreaLabelImageBlagueWidgetContents.setObjectName("scrollAreaLabelImageBlagueWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaLabelImageBlagueWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.labelImageBlague = QtWidgets.QLabel(self.scrollAreaLabelImageBlagueWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelImageBlague.sizePolicy().hasHeightForWidth())
        self.labelImageBlague.setSizePolicy(sizePolicy)
        self.labelImageBlague.setMinimumSize(QtCore.QSize(0, 0))
        self.labelImageBlague.setStyleSheet("border: none;")
        self.labelImageBlague.setText("")
        self.labelImageBlague.setObjectName("labelImageBlague")
        self.gridLayout_6.addWidget(self.labelImageBlague, 0, 0, 1, 1)
        self.scrollAreaLabelImageBlague.setWidget(self.scrollAreaLabelImageBlagueWidgetContents)
        self.gridLayout_5.addWidget(self.scrollAreaLabelImageBlague, 2, 0, 1, 1)
        self.buttonBlague = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBlague.sizePolicy().hasHeightForWidth())
        self.buttonBlague.setSizePolicy(sizePolicy)
        self.buttonBlague.setMinimumSize(QtCore.QSize(200, 0))
        self.buttonBlague.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/assets/res/cycle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBlague.setIcon(icon6)
        self.buttonBlague.setIconSize(QtCore.QSize(20, 20))
        self.buttonBlague.setAutoDefault(False)
        self.buttonBlague.setDefault(False)
        self.buttonBlague.setFlat(False)
        self.buttonBlague.setObjectName("buttonBlague")
        self.gridLayout_5.addWidget(self.buttonBlague, 2, 1, 1, 1, QtCore.Qt.AlignBottom)
        self.verticalLayout_13.addWidget(self.widget_2)
        self.gridlayout_10.addWidget(self.frameBlague, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.homeWidget)
        self.bibliothequeWidget = QtWidgets.QWidget()
        self.bibliothequeWidget.setStyleSheet("")
        self.bibliothequeWidget.setObjectName("bibliothequeWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.bibliothequeWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bibliothequeLabel = QtWidgets.QLabel(self.bibliothequeWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.bibliothequeLabel.setFont(font)
        self.bibliothequeLabel.setStyleSheet("")
        self.bibliothequeLabel.setObjectName("bibliothequeLabel")
        self.verticalLayout_3.addWidget(self.bibliothequeLabel, 0, QtCore.Qt.AlignHCenter)
        self.scrollAreaBibliotheque = QtWidgets.QScrollArea(self.bibliothequeWidget)
        self.scrollAreaBibliotheque.setWidgetResizable(True)
        self.scrollAreaBibliotheque.setObjectName("scrollAreaBibliotheque")
        self.scrollAreaBibliothequeWidgetContent = QtWidgets.QWidget()
        self.scrollAreaBibliothequeWidgetContent.setGeometry(QtCore.QRect(0, 0, 844, 617))
        self.scrollAreaBibliothequeWidgetContent.setObjectName("scrollAreaBibliothequeWidgetContent")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaBibliothequeWidgetContent)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaBibliothequeWidgetContent)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.scrollAreaBibliotheque.setWidget(self.scrollAreaBibliothequeWidgetContent)
        self.verticalLayout_3.addWidget(self.scrollAreaBibliotheque)
        self.stackedWidget.addWidget(self.bibliothequeWidget)
        self.centerPanel.addWidget(self.stackedWidget)
        self.horizontalLayout.addLayout(self.centerPanel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bibliothèque"))
        self.leftPanelButtonSearch.setText(_translate("MainWindow", "Rechercher"))
        self.leftPanelButtonHome.setText(_translate("MainWindow", "Recommendations"))
        self.leftPanelButtonBibliotheque.setText(_translate("MainWindow", "Bibliothèque"))
        self.searchButton.setText(_translate("MainWindow", "Rechercher"))
        self.searchLineEdit.setPlaceholderText(_translate("MainWindow", "Tapez un nom de livre ici..."))
        self.bookDetaillRetourButton.setText(_translate("MainWindow", "Retour"))
        self.labelRecommendations.setText(_translate("MainWindow", "Recommendations"))
        self.buttonRecommendationGenre.setText(_translate("MainWindow", "Recommendations par genre"))
        self.buttonRecommendationAuteur.setText(_translate("MainWindow", "Recommendations par auteurs"))
        self.labelBlague.setText(_translate("MainWindow", "Blague du jour"))
        self.buttonBlague.setText(_translate("MainWindow", "Une autre !"))
        self.bibliothequeLabel.setText(_translate("MainWindow", "Bibliothèque"))
import ressources_rc
