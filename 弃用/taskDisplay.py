import sys

# PySide6
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt
from UI.taskDisplay_ui import Ui_Form
from glWidget import myGLWidget
from utils.debug import message


class taskDisplayWindow(Ui_Form, QWidget):
    def __init__(self, taskResult: dict, parent=None):
        super(taskDisplayWindow, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.taskResult = taskResult
        self.fileResults = None
        if "visoutput_result_dir" in self.taskResult:
            self.fileResults = self.taskResult.pop("visoutput_result_dir")
        keys = list(self.taskResult.keys())
        for key in keys:
            self.textBrowser.append(f"{key}: {self.taskResult[key]}")
        if self.fileResults:
            for file in self.fileResults:
                self.openfile(file)

        self.datasetPath = self.taskResult.get("dataset_path", None)
        self.datasetIndex = self.taskResult.get("dataset_index", None)
        if self.datasetPath and self.datasetIndex:
            gl_widget = myGLWidget(self.datasetPath, self.datasetIndex)
            gl_widget.show()
            self.mdiArea.addSubWindow(gl_widget)
            self.mdiArea.tileSubWindows()

    def openfile(self, file):
        # 利用pyside6的图片显示模块显示图片在新建label上，然后添加到self.mdiview中作为子窗口
        print(file)
        if file.endswith(".png"):
            from PySide6.QtGui import QPixmap

            pixmap = QPixmap(file)
            label = QLabel()
            pixmap = pixmap.scaled(
                label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio
            )
            label.setPixmap(pixmap)
            self.mdiArea.addSubWindow(label)
            label.show()
            self.mdiArea.subWindowList()[-1].setWindowTitle(file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = taskDisplayWindow({"123": "456", "789": "101112"})
    win.show()
    app.exec()
