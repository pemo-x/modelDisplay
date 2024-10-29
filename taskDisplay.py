import sys

# PySide6
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QLabel

from UI.taskDisplay_ui import Ui_Form


class taskDisplayWindow(Ui_Form, QWidget):
    def __init__(self, taskResult: dict):
        super(taskDisplayWindow, self).__init__()
        self.setupUi(self)
        self.taskResult = taskResult
        self.fileResults = None
        if "visoutput_result_dir" in self.taskResult:
            self.fileResults = self.taskResult.pop("visoutput_result_dir")
        keys = list(self.taskResult.keys())
        self.tableWidget.setColumnCount(len(keys))
        self.tableWidget.setHorizontalHeaderLabels(keys)
        for key in keys:
            self.tableWidget.setItem(
                0, keys.index(key), QTableWidgetItem(str(self.taskResult[key]))
            )
        if self.fileResults:
            for file in self.fileResults:
                self.openfile(file)

    def openfile(self, file):
        # 利用pyside6的图片显示模块显示图片在新建label上，然后添加到self.mdiview中作为子窗口
        if file.endswith(".png"):
            from PySide6.QtGui import QPixmap

            pixmap = QPixmap(file)
            label = QLabel()
            label.setPixmap(pixmap)
            self.mdiArea.addSubWindow(label)
            label.show()
            self.mdiArea.subWindowList()[-1].setWindowTitle(file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = taskDisplayWindow({"123": "456", "789": "101112"})
    win.show()
    app.exec()
