import sys

# PySide6
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QFileDialog,
    QFileSystemModel,
    QMdiSubWindow,
)
from PySide6.QtCore import QDir, QFileInfo, QModelIndex


# utils
import os
from UI.Main_ui import Ui_MainWindow
from glWidget import myGLWidget
from taskWindow import taskWindow
from utils.debug import message
from utils.task import Task


class MainWindow(QMainWindow, Ui_MainWindow):
    """主窗口类，负责应用程序的主界面和功能处理"""

    def __init__(self):
        """初始化主窗口，设置UI和连接信号与槽"""
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Sorfware")

        self.initTreeView()

        self.initMdiArea()

        self.initListWidget()

        self.initAction()
        self.initTabWidget()
        self.statusBar.showMessage("Ready")

    def initTabWidget(self):
        self.tabWidget.tabCloseRequested.connect(self.tabWidgetOnCloseRequested)

    def tabWidgetOnCloseRequested(self, index):
        if index != 0:
            self.tabWidget.removeTab(index)

    def initListWidget(self):
        self.listWidget.doubleClicked.connect(self.listWidgetOnDoubleClicked)

    def initAction(self):
        self.action_Tile.triggered.connect(self.mdiArea.tileSubWindows)
        self.action_Cascade.triggered.connect(self.mdiArea.cascadeSubWindows)
        self.action_AllClose.triggered.connect(self.mdiArea.closeAllSubWindows)
        self.action_OpenFile.triggered.connect(self.open_file_dialog)
        self.action_OpenFolder.triggered.connect(self.open_folder_dialog)
        self.action_CreateTasks.triggered.connect(self.createtasksOnTriggered)

    def initMdiArea(self):
        # 初始化OpenGL的窗口，避免闪屏
        GLWidget = myGLWidget(Task())
        self.mdiArea.addSubWindow(GLWidget)
        GLWidget.show()
        self.mdiArea.closeAllSubWindows()
        self.mdiArea.subWindowActivated.connect(self.updatelistWidget)

    def initTreeView(self):
        self.model = QFileSystemModel()
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.setRootPath(QDir.currentPath()))
        self.treeView.doubleClicked.connect(self.treeViewOnDoubleClicked)

    def createtasksOnTriggered(self):
        inittaskWindow = taskWindow(
            self.mdiArea.currentSubWindow().widget().task, parent=self
        )
        self.tabWidget.addTab(inittaskWindow, "任务")

        self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

    def listWidgetOnDoubleClicked(self, index: QModelIndex):
        """处理列表项双击事件，打开对应的GL窗口"""
        subWindow = self.mdiArea.activeSubWindow()
        if subWindow:
            glWidget: myGLWidget = subWindow.widget()
            glWidget.setDatas(index.row())
            subWindow.setWindowTitle(
                glWidget.task.datasetName + "--样本" + str(glWidget.task.datasetIndex)
            )

    def updatelistWidget(self, subWindow: QMdiSubWindow):
        """更新列表窗口，根据激活的子窗口的样本数量填充列表"""
        self.listWidget.clear()
        if subWindow:
            length = subWindow.widget().task.samplesLength
            for i in range(length):
                self.listWidget.addItem(f"样本{i}")

    def treeViewOnDoubleClicked(self, index):
        """处理树形视图双击事件，打开选中的文件"""
        fileInfo: QFileInfo = self.model.fileInfo(index)
        if fileInfo.isFile():
            filePath = fileInfo.absoluteFilePath()
            self.openFile(filePath)

    def openFile(self, filePath):
        """打开选定的文件，创建GL窗口并显示"""
        file_name = os.path.basename(filePath)
        file_suffix = os.path.splitext(file_name)[1]
        if file_suffix == ".skeleton" or file_suffix == ".npy":
            newTask = Task()
            newTask.datasetPath = filePath
            newTask.datasetName = file_name
            newTask.datasetSuffix = file_suffix
            newTask.datasetIndex = 0
            GLWidget = myGLWidget(task=newTask, parent=self.mdiArea)
            # 把mdiArea当前窗口取消最大化
            currentSubWindow = self.mdiArea.currentSubWindow()
            if currentSubWindow:
                currentSubWindow.showNormal()
            self.mdiArea.addSubWindow(GLWidget)
            GLWidget.show()
            self.mdiArea.subWindowList()[-1].adjustSize()
            self.mdiArea.subWindowList()[-1].setMinimumSize(400, 300)
            self.mdiArea.subWindowList()[-1].setGeometry(
                len(self.mdiArea.subWindowList()) * 20,
                len(self.mdiArea.subWindowList()) * 20,
                400,
                300,
            )
            self.mdiArea.subWindowList()[-1].setWindowTitle(
                file_name + "--样本" + str(GLWidget.task.datasetIndex)
            )
            self.tabWidget.setCurrentIndex(0)

    def open_file_dialog(self):
        """弹出文件选择对话框，选择文件并打开"""
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if file_path:
            self.openFile(file_path)

    def open_folder_dialog(self):
        """弹出文件夹选择对话框，设置树形视图的根目录"""
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder_path:
            self.treeView.setRootIndex(self.model.setRootPath(folder_path))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
