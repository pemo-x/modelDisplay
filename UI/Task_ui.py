# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Task.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMdiArea,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(405, 396)
        self.horizontalLayout_7 = QHBoxLayout(Form)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mdiArea = QMdiArea(self.groupBox)
        self.mdiArea.setObjectName(u"mdiArea")

        self.verticalLayout_2.addWidget(self.mdiArea)

        self.textBrowser = QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.horizontalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.datasetName = QLabel(self.groupBox_2)
        self.datasetName.setObjectName(u"datasetName")

        self.horizontalLayout.addWidget(self.datasetName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_Sample = QLabel(self.groupBox_2)
        self.label_Sample.setObjectName(u"label_Sample")
        self.label_Sample.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_Sample)

        self.sample_spinBox = QSpinBox(self.groupBox_2)
        self.sample_spinBox.setObjectName(u"sample_spinBox")
        self.sample_spinBox.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.sample_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.line_3 = QFrame(self.groupBox_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.explainthealgorithm_comboBox = QComboBox(self.groupBox_2)
        self.explainthealgorithm_comboBox.setObjectName(u"explainthealgorithm_comboBox")

        self.horizontalLayout_3.addWidget(self.explainthealgorithm_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_commandlineinstructions = QLineEdit(self.groupBox_2)
        self.lineEdit_commandlineinstructions.setObjectName(u"lineEdit_commandlineinstructions")

        self.horizontalLayout_4.addWidget(self.lineEdit_commandlineinstructions)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_commandlineRundirectory = QLineEdit(self.groupBox_2)
        self.lineEdit_commandlineRundirectory.setObjectName(u"lineEdit_commandlineRundirectory")

        self.horizontalLayout_5.addWidget(self.lineEdit_commandlineRundirectory)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.pushButton_StartRun = QPushButton(self.groupBox_2)
        self.pushButton_StartRun.setObjectName(u"pushButton_StartRun")

        self.verticalLayout.addWidget(self.pushButton_StartRun)

        self.progressBar = QProgressBar(self.groupBox_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressBar)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)


        self.horizontalLayout_7.addWidget(self.groupBox_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u7ed3\u679c\u8f93\u51fa", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u53c2\u6570\u914d\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u7684\u6570\u636e\uff1a", None))
        self.datasetName.setText(QCoreApplication.translate("Form", u"\u8bf7\u6253\u5f00\u6570\u636e\u96c6", None))
        self.label_Sample.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6837\u672c\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5f85\u89e3\u91ca\u7684\u8bc6\u522b\u6a21\u578b\uff1a", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"ST-GCN", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u7684\u89e3\u91ca\u7b97\u6cd5\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u547d\u4ee4\u884c\u6307\u4ee4\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u547d\u4ee4\u884c\u8fd0\u884c\u76ee\u5f55\uff1a", None))
        self.pushButton_StartRun.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8fd0\u884c", None))
    # retranslateUi

