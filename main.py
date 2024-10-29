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
import utils.dealData as dealData
import os
from UI.Main_ui import Ui_MainWindow
from UI.glWidget import myGLWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    """主窗口类，负责应用程序的主界面和功能处理"""

    def __init__(self):
        """初始化主窗口，设置UI和连接信号与槽"""
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
        # 初始化OpenGL的窗口，避免闪屏
        GLWidget = myGLWidget()
        self.mdiArea.addSubWindow(GLWidget)
        GLWidget.show()
        self.mdiArea.closeAllSubWindows()
        self.mdiArea.subWindowActivated.connect(self.updatelistWidget)
        self.listWidget.doubleClicked.connect(self.listWidgetOnDoubleClicked)

    def listWidgetOnDoubleClicked(self, index: QModelIndex):
        """处理列表项双击事件，打开对应的GL窗口"""
        subWindow = self.mdiArea.activeSubWindow()
        if subWindow:
            glWidget: myGLWidget = subWindow.widget()
            glWidget.setDatas(index.row())

    def updatelistWidget(self, subWindow: QMdiSubWindow):
        """更新列表窗口，根据激活的子窗口的样本数量填充列表"""
        self.listWidget.clear()
        if subWindow:
            length = subWindow.widget().SamplesLength
            for i in range(length):
                self.listWidget.addItem(f"{i}")

    def treeViewOnDoubleClicked(self, index):
        """处理树形视图双击事件，打开选中的文件"""
        fileInfo: QFileInfo = self.model.fileInfo(index)
        if fileInfo.isFile():
            filePath = fileInfo.absoluteFilePath()
            self.openFile(filePath)

    def oldOpenFile(self, filePath):
        """处理旧格式文件的打开逻辑，支持.skeleton和.npy格式"""
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

        if len(datas["points"].shape) == 3:
            GLWidget = myGLWidget(datas)
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
            self.mdiArea.subWindowList()[-1].setWindowTitle(file_name)

    def openFile(self, filePath):
        """打开选定的文件，创建GL窗口并显示"""
        file_name = os.path.basename(filePath)
        file_suffix = os.path.splitext(file_name)[1]
        if file_suffix == ".skeleton" or file_suffix == ".npy":
            GLWidget = myGLWidget(filePath)
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
            self.mdiArea.subWindowList()[-1].setWindowTitle(file_name)

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
