import os
import subprocess
import sys

# PySide6
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
)

from UI.glWidget import myGLWidget
from UI.initTask_ui import Ui_Form

from taskDisplay import taskDisplayWindow


class initTaskWindow(Ui_Form, QWidget):
    """初始化任务窗口类，负责配置算法和数据集，创建任务等功能."""

    def __init__(
        self,
        datasetWidget: myGLWidget = None,
        algorithm=None,
    ):
        """初始化方法，设置数据集和算法的初始状态."""
        super(initTaskWindow, self).__init__()
        self.setupUi(self)
        self.skeletonalgorithms = [
            "gradcam",
            "gradcampp",
            "ablation",
            "scorecam",
            "isgcam",
            "shapleycam",
        ]
        self.formationalgorithms = [
            "crcam",
            "gradcam",
            "bicam",
            "ablationcam",
            "scorecam",
            "gradcampp",
            "gtcam",
            "wblrp",
        ]
        datasetPath = datasetWidget.filePath
        if os.path.splitext(datasetPath)[1] == ".skeleton":
            # 数据集初始化
            self.datasetName.setText(os.path.basename(datasetPath))
            # 算法列表初始化
            self.explainthealgorithm_comboBox.clear()
            for each in self.skeletonalgorithms:
                self.explainthealgorithm_comboBox.addItem(each)

            index = self.skeletonalgorithms.index(algorithm)
            self.explainthealgorithm_comboBox.setCurrentIndex(index)
            # 命令行初始化

            pass
        else:
            # 数据集初始化
            self.datasetName.setText(os.path.basename(datasetPath))
            self.sample_spinBox.setMinimum(0)
            self.sample_spinBox.setMaximum(datasetWidget.SamplesLength - 1)
            # 算法列表初始化
            self.explainthealgorithm_comboBox.clear()
            for each in self.formationalgorithms:
                self.explainthealgorithm_comboBox.addItem(each)
            index = self.formationalgorithms.index(algorithm)
            self.explainthealgorithm_comboBox.setCurrentIndex(index)
            # 命令行初始化

        self.pushButton_StartRun.clicked.connect(self.createTask)

    def createTask(self):
        """创建任务，将命令和目录作为参数传入
        ## args: command 要执行的命令
        ## args: directory 命令执行的目录
        """
        command = self.lineEdit_commandlineinstructions.text()
        directory = self.lineEdit_commandlineRundirectory.text()
        self.process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=directory,
        )

    def func(self):
        """利用动画显示进度条并用getRunstatu()获取任务运行状态."""
        # 先清空当前窗体内容

    def getRunstatu(self):
        """获取任务运行状态，返回退出代码."""
        exit_code = self.process.poll()
        return exit_code

    def getReturn(self):
        """获取任务返回结果，如果任务已完成，则处理输出."""
        if self.getRunstatu() is not None:
            stdout, stderr = self.process.communicate()
            result = self.dealReturn(stdout)
            self.taskdisplaywindow = taskDisplayWindow(result)
            self.taskdisplaywindow.show()
        else:
            stdout, stderr = "", ""

    def dealReturn(self, stdout):
        """处理返回结果，解析标准输出并返回结果字典."""
        result = {}
        # TODO 处理返回结果
        return result


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = initTaskWindow()
    win.show()
    app.exec()
