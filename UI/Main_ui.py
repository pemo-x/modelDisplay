# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QHeaderView,
    QLabel, QListView, QMainWindow, QMdiArea,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QToolBar, QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1158, 839)
        self.action_OpenFile = QAction(MainWindow)
        self.action_OpenFile.setObjectName(u"action_OpenFile")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.action_OpenFile.setIcon(icon)
        self.action_OpenFolder = QAction(MainWindow)
        self.action_OpenFolder.setObjectName(u"action_OpenFolder")
        icon1 = QIcon(QIcon.fromTheme(u"folder-open"))
        self.action_OpenFolder.setIcon(icon1)
        self.action_CloseFolder = QAction(MainWindow)
        self.action_CloseFolder.setObjectName(u"action_CloseFolder")
        self.action_Tile = QAction(MainWindow)
        self.action_Tile.setObjectName(u"action_Tile")
        self.action_Tile.setMenuRole(QAction.MenuRole.NoRole)
        self.action_Cascade = QAction(MainWindow)
        self.action_Cascade.setObjectName(u"action_Cascade")
        self.action_Cascade.setMenuRole(QAction.MenuRole.NoRole)
        self.action_AllClose = QAction(MainWindow)
        self.action_AllClose.setObjectName(u"action_AllClose")
        self.action_AllClose.setMenuRole(QAction.MenuRole.NoRole)
        self.action_AllMinimize = QAction(MainWindow)
        self.action_AllMinimize.setObjectName(u"action_AllMinimize")
        self.action_AllMinimize.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setEnabled(True)

        self.horizontalLayout.addWidget(self.mdiArea)

        self.horizontalLayout.setStretch(0, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1158, 20))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menut3 = QMenu(self.menubar)
        self.menut3.setObjectName(u"menut3")
        MainWindow.setMenuBar(self.menubar)
        self.dockWidget_2 = QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeView = QTreeView(self.dockWidgetContents_2)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setAnimated(True)

        self.verticalLayout.addWidget(self.treeView)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget_2)
        self.dockWidget_3 = QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName(u"dockWidget_3")
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.dockWidgetContents_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.dockWidget_3)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listView = QListView(self.dockWidgetContents)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_3.addWidget(self.listView)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menut3.menuAction())
        self.menu.addAction(self.action_OpenFile)
        self.menu.addAction(self.action_OpenFolder)
        self.menu.addAction(self.action_CloseFolder)
        self.toolBar.addAction(self.action_OpenFile)
        self.toolBar.addAction(self.action_OpenFolder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Tile)
        self.toolBar.addAction(self.action_Cascade)
        self.toolBar.addAction(self.action_AllClose)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_OpenFile.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.action_OpenFolder.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.action_CloseFolder.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u6587\u4ef6\u5939", None))
        self.action_Tile.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u94fa\u7a97\u53e3", None))
        self.action_Cascade.setText(QCoreApplication.translate("MainWindow", u"\u5c42\u53e0\u7a97\u53e3", None))
#if QT_CONFIG(tooltip)
        self.action_Cascade.setToolTip(QCoreApplication.translate("MainWindow", u"\u5c42\u53e0\u7a97\u53e3", None))
#endif // QT_CONFIG(tooltip)
        self.action_AllClose.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u5173\u95ed", None))
#if QT_CONFIG(tooltip)
        self.action_AllClose.setToolTip(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.action_AllMinimize.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u6700\u5c0f\u5316", None))
#if QT_CONFIG(tooltip)
        self.action_AllMinimize.setToolTip(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u6700\u5c0f\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menut3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8d44\u6e90\u7ba1\u7406\u5668", None))
        self.dockWidget_3.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u7ed3\u679c", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5bf9\u8c61\u7ba1\u7406\u5668", None))
    # retranslateUi

