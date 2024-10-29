# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'initTask.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(280, 208)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.datasetName = QLabel(Form)
        self.datasetName.setObjectName(u"datasetName")

        self.horizontalLayout.addWidget(self.datasetName)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.sample_spinBox = QSpinBox(Form)
        self.sample_spinBox.setObjectName(u"sample_spinBox")

        self.horizontalLayout.addWidget(self.sample_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.explainthealgorithm_comboBox = QComboBox(Form)
        self.explainthealgorithm_comboBox.setObjectName(u"explainthealgorithm_comboBox")

        self.horizontalLayout_3.addWidget(self.explainthealgorithm_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_commandlineinstructions = QLineEdit(Form)
        self.lineEdit_commandlineinstructions.setObjectName(u"lineEdit_commandlineinstructions")

        self.horizontalLayout_4.addWidget(self.lineEdit_commandlineinstructions)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_commandlineRundirectory = QLineEdit(Form)
        self.lineEdit_commandlineRundirectory.setObjectName(u"lineEdit_commandlineRundirectory")

        self.horizontalLayout_5.addWidget(self.lineEdit_commandlineRundirectory)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.pushButton_StartRun = QPushButton(Form)
        self.pushButton_StartRun.setObjectName(u"pushButton_StartRun")

        self.verticalLayout.addWidget(self.pushButton_StartRun)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u7684\u6570\u636e\uff1a", None))
        self.datasetName.setText(QCoreApplication.translate("Form", u"\u8bf7\u6253\u5f00\u6570\u636e\u96c6", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6837\u672c\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5f85\u89e3\u91ca\u7684\u8bc6\u522b\u6a21\u578b\uff1a", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"stgcn", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u7684\u89e3\u91ca\u7b97\u6cd5\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u547d\u4ee4\u884c\u6307\u4ee4\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u547d\u4ee4\u884c\u8fd0\u884c\u76ee\u5f55\uff1a", None))
        self.pushButton_StartRun.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8fd0\u884c", None))
    # retranslateUi

