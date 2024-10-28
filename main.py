import sys

# PySide6
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QFileDialog,
    QFileSystemModel,
    QSplitter,
    QTreeView,
    QMdiArea,
)
from PySide6.QtCore import QDir, QFileInfo

# pyqtgraph
import pyqtgraph as pg
import pyqtgraph.opengl as gl

# utils
import utils.dealData as dealData
import os
from UI.Main_ui import Ui_MainWindow
from UI.glWidget import myGLWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.action_OpenFile.triggered.connect(self.open_file_dialog)
        self.action_OpenFolder.triggered.connect(self.open_folder_dialog)

        self.model = QFileSystemModel()
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.setRootPath(QDir.currentPath()))
        self.treeView.doubleClicked.connect(self.treeViewOnDoubleClicked)
        self.action_Tile.triggered.connect(self.mdiArea.tileSubWindows)
        self.action_Cascade.triggered.connect(self.mdiArea.cascadeSubWindows)
        self.action_AllClose.triggered.connect(self.mdiArea.closeAllSubWindows)
        self.statusBar.showMessage("Ready")

    def treeViewOnDoubleClicked(self, index):
        fileInfo: QFileInfo = self.model.fileInfo(index)
        if fileInfo.isFile():
            filePath = fileInfo.absoluteFilePath()
            self.openFile(filePath)

    def openFile(self, filePath):
        file_name = os.path.basename(filePath)
        file_suffix = os.path.splitext(file_name)[1]
        datas = None
        try:
            if file_suffix == ".skeleton":
                datas = dealData.dealSkeleton(filePath)
            elif file_suffix == ".npy":
                datas = dealData.dealNpy(filePath)
            else:
                self.statusBar.showMessage("不支持打开的文件")
                return 0
        except Exception as e:
            # 如果发生了其他类型的异常，执行这里的代码
            self.statusBar.showMessage(f"发生错误：{e}")
            return 0
        GLWidget = myGLWidget(datas)
        self.mdiArea.addSubWindow(GLWidget)
        self.mdiArea.subWindowList()[-1].setGeometry(100, 100, 300, 200)
        # self.mdiArea.subWindowList()[-1].adjustSize()
        # self.mdiArea.subWindowList()[-1].showMaximized()
        self.mdiArea.subWindowList()[-1].show()
        self.mdiArea.subWindowList()[-1].setWindowTitle(file_name)
        # self.mdiArea.tileSubWindows()

    def open_file_dialog(self):
        # 弹出文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path:
            self.openFile(file_path)

    def open_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder_path:
            self.treeView.setRootIndex(self.model.setRootPath(folder_path))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
