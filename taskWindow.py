import os
import subprocess
import sys

# PySide6
from PySide6.QtWidgets import QApplication, QWidget, QLabel

from PySide6.QtCore import Qt
import PySide6.QtCore as QtCore

from glWidget import myGLWidget
from UI.Task_ui import Ui_Form

from utils.debug import message
from utils.task import Task

algorithmconversiontable = {
    "Grad-CAM": "gradcam",
    "Grad-CAM++": "gradcampp",
    "Ablation-CAM": "ablation",
    "Score-CAM": "scorecam",
    "BI-CAM": "bicam",
    "CR-CAM": "crcam",
    "GT-CAM": "gtcam",
    "Isg-CAM": "isgcam",
    "WP-LPR": "wblrp",
    "Shapley-CAM": "shapleycam",
}


class taskWindow(Ui_Form, QWidget):
    """初始化任务窗口类，负责配置算法和数据集，创建任务等功能."""

    def __init__(
        self,
        task: Task,
        parent=None,
    ):
        """初始化方法，设置数据集和算法的初始状态."""
        super(taskWindow, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.task = task

        self.skeletonalgorithms = [
            "Grad-CAM",
            "Grad-CAM++",
            "Ablation-CAM",
            "Score-CAM",
            "Isg-CAM",
            "Shapley-CAM",
        ]
        self.formationalgorithms = [
            "CR-CAM",
            "Grad-CAM",
            "BI-CAM",
            "Ablation-CAM",
            "Score-CAM",
            "Grad-CAM++",
            "GT-CAM",
            "WP-LPR",
        ]
        if self.task.datasetSuffix == ".skeleton":
            # 数据集初始化
            self.datasetName.setText(os.path.basename(self.task.datasetPath))
            self.sample_spinBox.setVisible(False)
            self.label_Sample.setVisible(False)
            # 算法列表初始化
            self.explainthealgorithm_comboBox.clear()
            for each in self.skeletonalgorithms:
                self.explainthealgorithm_comboBox.addItem(each)
            # 命令行初始化
            self.createcommandline()

        else:
            # 数据集初始化
            self.datasetName.setText(os.path.basename(self.task.datasetPath))
            self.sample_spinBox.setMinimum(0)
            self.sample_spinBox.setMaximum(self.task.samplesLength - 1)
            self.sample_spinBox.setValue(self.task.datasetIndex)
            # 算法列表初始化
            self.explainthealgorithm_comboBox.clear()
            for each in self.formationalgorithms:
                self.explainthealgorithm_comboBox.addItem(each)
            # 命令行初始化
            self.createcommandline()
        self.pushButton_StartRun.clicked.connect(self.executeTask)
        self.sample_spinBox.valueChanged.connect(self.createcommandline)
        self.explainthealgorithm_comboBox.currentTextChanged.connect(
            self.createcommandline
        )
        self.displayDataset()
        self.progressBar.setVisible(False)

    def createcommandline(self):
        """创建命令行，将算法、数据集、样本数、命令行指令、运行目录作为参数传入."""
        python = "/data/home/temp/Desktop/model/.conda/bin/python"
        algorithm = self.explainthealgorithm_comboBox.currentText()
        self.task.algorithm = algorithm
        dataset = self.task.datasetName
        sample = self.task.datasetIndex
        programs = {
            "rechange_val_data_plane_Radar.npy": "/data/home/temp/Desktop/model/final/model_final/data/home/yr/YRR/suweipeng/test_twoairplanes-v0.1/main.py",
            "ship_dataset.npy": "/data/home/temp/Desktop/model/final/model_final/test_ship/main.py",
            "five_planes.npy": "/data/home/temp/Desktop/model/final/model_final/test_fiveairplanes-v0.1/main.py",
        }
        if dataset in programs:
            program = programs[dataset]
            self.task.command = f"{python} {program} --methodx {algorithmconversiontable[algorithm]} --frame_N {sample}"
            self.task.directory = os.path.dirname(os.path.realpath(program))
            self.lineEdit_commandlineinstructions.setText(self.task.command)
            self.lineEdit_commandlineRundirectory.setText(self.task.directory)
        elif self.task.datasetSuffix == ".skeleton":
            program = (
                "/data/home/temp/Desktop/model/final/model_final/st-gcn-cam-org/main.py"
            )
            self.task.command = f"{python} {program} shapleycam --skeleton {dataset.split('.')[0]} --cam_type {algorithmconversiontable[algorithm]}"
            self.task.directory = os.path.dirname(os.path.realpath(program))
            self.lineEdit_commandlineinstructions.setText(self.task.command)
            self.lineEdit_commandlineRundirectory.setText(self.task.directory)

    def executeTask(self):
        """创建任务，将命令和目录作为参数传入
        ## args: command 要执行的命令
        ## args: directory 命令执行的目录
        """
        try:
            self.task.command = self.lineEdit_commandlineinstructions.text().split(" ")
            self.task.directory = self.lineEdit_commandlineRundirectory.text()
            self.process = subprocess.Popen(
                self.task.command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=self.task.directory,
            )
            self.progressBar.setVisible(True)
            self.pushButton_StartRun.setEnabled(False)
            self.explainthealgorithm_comboBox.setEnabled(False)
            self.pushButton_StartRun.setText("正在运行...")
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.getReturn)
            self.timer.start(1000)
        except Exception as e:
            message(str(e), "创建任务失败", parent=self.parent)

    def getRunstatu(self):
        """获取任务运行状态，返回退出代码."""
        exit_code = self.process.poll()
        return exit_code

    def getReturn(self):
        """获取任务返回结果，如果任务已完成，则处理输出."""
        exit_code = self.getRunstatu()
        if exit_code is not None:
            if exit_code == 0:
                stdout, stderr = self.process.communicate()
                # print(f"stdout:{stdout}")
                # print(f"stderr:{stderr}")
                self.task.result = self.dealReturn(stdout)

                self.displayResult()

                # 把task对象保存到文件
                taskDict = self.task.__dict__
                print(taskDict)
                # 保存结果到文件
                algorithm = self.task.algorithm
                dataset = self.task.datasetName
                sample = self.task.datasetIndex
                # 以当前时间和三个参数为文件名，保存result这个字典到文件
                import time
                import json
                import os

                time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime())
                file_name = f"{algorithm}__{dataset}_{sample}__{time_str}.json"

                if not os.path.exists("historyTaskResult"):
                    os.makedirs("historyTaskResult")
                file_path = os.path.join("historyTaskResult", file_name)
                with open(file_path, "w") as f:
                    json.dump(taskDict, f)
                message(f"保存结果到{file_path}成功", "提示", parent=self.parent)
                # 打开结果文件并存取成Task对象
                # with open(file_path, "r") as f:
                #     taskDict = json.load(f)
                #     task = Task()
                #     task.__dict__ = taskDict

            else:
                message(
                    f"任务运行失败，退出码：{exit_code}", "提示", parent=self.parent
                )
                stdout, stderr = self.process.communicate()
                self.textBrowser.append(f"stdout:{stdout}")
                self.textBrowser.append(f"stderr:{stderr}")

            self.progressBar.setVisible(False)
            self.pushButton_StartRun.setEnabled(False)
            self.explainthealgorithm_comboBox.setEnabled(False)
            self.pushButton_StartRun.setText("运行结束")
            self.process.kill()
            self.timer.stop()

        else:
            self.pushButton_StartRun.setText(f"获取进程运行状态码为：{exit_code}")

    def displayResult(self):
        self.taskResult = self.task.result
        self.fileResults = None
        if "visoutput_result_dir" in self.taskResult:
            self.fileResults = self.taskResult.pop("visoutput_result_dir")
        keys = list(self.taskResult.keys())
        for key in keys:
            self.textBrowser.append(f"{key}: {self.taskResult[key]}")
        if self.fileResults:
            for file in self.fileResults:
                self.openfile(file)
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

    def displayDataset(self):
        if self.task.datasetPath is not None and self.task.datasetIndex is not None:
            gl_widget = myGLWidget(self.task, parent=self.mdiArea)
            gl_widget.show()
            self.mdiArea.addSubWindow(gl_widget)
            self.mdiArea.subWindowList()[-1].setWindowTitle(
                self.task.datasetName + "样本：" + str(self.task.datasetIndex)
            )
            self.mdiArea.tileSubWindows()

    def dealReturn(self, stdout):
        """处理返回结果，解析标准输出并返回结果字典."""
        result = {}

        def plane_ship_two_five_rec_total(stdout_l):
            r1 = "top1"
            r2 = "top2"
            label = "0"
            count = 0
            index = 0
            data = {}

            list_out = stdout.split(" ")
            # print(list_out)

            for i in list_out:
                if r1 in i:
                    label = i[:-6]
                    index = count
                    break
                count = count + 1

            data["top1"] = list_out[index + 2] + " " + list_out[index + 3]

            count = 0
            index = 0

            for i in list_out:
                if r2 in i:
                    index = count
                    break
                count = count + 1

            data["top2"] = list_out[index + 2] + " " + list_out[index + 3]

            list_out = stdout.split("------------------")
            # print(list_out)
            data["visoutput_result_dir"] = [
                self.task.directory + "/" + list_out[-6].strip("\n").replace("./", "")
            ]
            data["ave_drop"] = list_out[-5].strip("\n")
            data["ave_increase"] = list_out[-4].strip("\n")
            data["inse_auc"] = list_out[-3].strip("\n")
            data["del_auc"] = list_out[-2].strip("\n")
            data["label"] = list_out[-1].strip("\n")
            data["predit"] = list_out[-7].strip("\n")

            # print(data)

            return data

        def skeleton_rec_cam(stdout_l):
            data = {}
            list_out = stdout_l.split(" ")
            # print(list_out)
            # print(list_out[-8])
            data["visoutput_result_dir"] = [
                self.task.directory + "/" + (list_out[-8].split("\n")[1].split("./"))[1]
            ]
            data["ave_drop"] = list_out[-7]
            data["ave_increase"] = list_out[-5]
            data["inse_auc"] = list_out[-3]
            data["del_auc"] = list_out[-1].split("\n")[0]

            # print(data)

            return data

        dataset = self.datasetName.text()
        dealFuncs = {
            "rechange_val_data_plane_Radar.npy": plane_ship_two_five_rec_total,
            "ship_dataset.npy": plane_ship_two_five_rec_total,
            "five_planes.npy": plane_ship_two_five_rec_total,
        }

        if dataset in dealFuncs:
            result = dealFuncs[dataset](stdout)
        elif os.path.splitext(dataset)[1] == ".skeleton":
            result = skeleton_rec_cam(stdout)
        return result


if __name__ == "__main__":
    app = QApplication(sys.argv)
    task = Task()
    task.datasetPath = (
        "D:\\pemo\\code\\python\\software\\datas\\rechange_val_data_plane_Radar.npy"
    )
    task.datasetIndex = 5
    task.datasetSuffix = ".npy"
    task.algorithm = "Grad-CAM"
    task.command = "python main.py --methodx gradcam --frame_N 5"
    task.directory = (
        "D:\\pemo\\code\\python\\software\\model\\final\\model_final\\test_ship"
    )
    task.samplesLength = 100
    task.result = {"123": "456", "789": "101112"}
    win = taskWindow(task)
    win.displayResult()
    win.show()
    app.exec()
