import os
import subprocess
import sys

# PySide6
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
)
import PySide6.QtCore as QtCore
from glWidget import myGLWidget
from UI.initTask_ui import Ui_Form

from taskDisplay import taskDisplayWindow
from utils.debug import message

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


class initTaskWindow(Ui_Form, QWidget):
    """初始化任务窗口类，负责配置算法和数据集，创建任务等功能."""

    def __init__(
        self,
        datasetWidget: myGLWidget = None,
        parent=None,
    ):
        """初始化方法，设置数据集和算法的初始状态."""
        super(initTaskWindow, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.datasetPath = datasetWidget.datasetPath
        self.datasetIndex = datasetWidget.sampleIndex
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
        datasetPath = datasetWidget.datasetPath
        if os.path.splitext(datasetPath)[1] == ".skeleton":
            # 数据集初始化
            self.datasetName.setText(os.path.basename(datasetPath))
            self.sample_spinBox.setVisible(False)
            self.label_Sample.setVisible(False)
            # 算法列表初始化
            self.explainthealgorithm_comboBox.clear()
            for each in self.skeletonalgorithms:
                self.explainthealgorithm_comboBox.addItem(each)

            # index = self.skeletonalgorithms.index(algorithm)
            # self.explainthealgorithm_comboBox.setCurrentIndex(index)
            # 命令行初始化
            self.createcommandline()

        else:
            # 数据集初始化
            self.datasetName.setText(os.path.basename(datasetPath))
            self.sample_spinBox.setMinimum(0)
            self.sample_spinBox.setMaximum(datasetWidget.SamplesLength - 1)
            self.sample_spinBox.setValue(datasetWidget.sampleIndex)
            # 算法列表初始化
            self.explainthealgorithm_comboBox.clear()
            for each in self.formationalgorithms:
                self.explainthealgorithm_comboBox.addItem(each)
            # index = self.formationalgorithms.index(algorithm)
            # self.explainthealgorithm_comboBox.setCurrentIndex(index)
            # 命令行初始化
            self.createcommandline()
        self.pushButton_StartRun.clicked.connect(self.createTask)
        self.sample_spinBox.valueChanged.connect(self.createcommandline)
        self.explainthealgorithm_comboBox.currentTextChanged.connect(
            self.createcommandline
        )

        self.progressBar.setVisible(False)

    def createcommandline(self):
        """创建命令行，将算法、数据集、样本数、命令行指令、运行目录作为参数传入."""
        python = "/data/home/temp/Desktop/model/.conda/bin/python"
        algorithm = self.explainthealgorithm_comboBox.currentText()
        dataset = self.datasetName.text()
        sample = self.sample_spinBox.value()
        programs = {
            "rechange_val_data_plane_Radar.npy": "/data/home/temp/Desktop/model/final/model_final/data/home/yr/YRR/suweipeng/test_twoairplanes-v0.1/main.py",
            "ship_dataset.npy": "/data/home/temp/Desktop/model/final/model_final/test_ship/main.py",
            "t2": "/data/home/temp/Desktop/model/final/model_final/test_fiveairplanes-v0.1/main.py",
        }
        if dataset in programs:
            program = programs[dataset]
            command = f"{python} {program} --methodx {algorithmconversiontable[algorithm]} --frame_N {sample}"
            directory = os.path.dirname(os.path.realpath(program))
            self.lineEdit_commandlineinstructions.setText(command)
            self.lineEdit_commandlineRundirectory.setText(directory)
        elif os.path.splitext(dataset)[1] == ".skeleton":
            program = (
                "/data/home/temp/Desktop/model/final/model_final/st-gcn-cam-org/main.py"
            )
            command = f"{python} {program} {algorithmconversiontable[algorithm]} --skeleton {dataset.split('.')[0]}"
            directory = os.path.dirname(os.path.realpath(program))
            self.lineEdit_commandlineinstructions.setText(command)
            self.lineEdit_commandlineRundirectory.setText(directory)

    def createTask(self):
        """创建任务，将命令和目录作为参数传入
        ## args: command 要执行的命令
        ## args: directory 命令执行的目录
        """
        try:
            self.command = self.lineEdit_commandlineinstructions.text().split(" ")
            self.directory = self.lineEdit_commandlineRundirectory.text()
            self.process = subprocess.Popen(
                self.command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=self.directory,
            )
            self.progressBar.setVisible(True)
            self.pushButton_StartRun.setEnabled(False)
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
            try:
                if exit_code == 0:
                    stdout, stderr = self.process.communicate()
                    # print(f"stdout:{stdout}")
                    # print(f"stderr:{stderr}")
                    result = self.dealReturn(stdout)
                    # 添加数据集路径和样本索引
                    result["dataset_path"] = self.datasetPath
                    result["dataset_index"] = self.datasetIndex

                    # print(f"result={result}")
                    self.taskdisplaywindow = taskDisplayWindow(
                        result, parent=self.parent
                    )
                    self.taskdisplaywindow.show()
                    # self.setVisible(False)

                    algorithm = self.explainthealgorithm_comboBox.currentText()
                    dataset = self.datasetName.text()
                    sample = self.sample_spinBox.value()
                    # 以当前时间和三个参数为文件名，保存result这个字典到文件
                    import time
                    import json
                    import os

                    time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime())
                    file_name = f"{algorithm}_{dataset}_{sample}_{time_str}.json"

                    if not os.path.exists("historyTaskResult"):
                        os.makedirs("historyTaskResult")
                    file_path = os.path.join("historyTaskResult", file_name)
                    with open(file_path, "w") as f:
                        json.dump(result, f)
                    message(f"保存结果到{file_path}成功", "提示", parent=self.parent)
                else:
                    message(
                        f"任务运行失败，退出码：{exit_code}", "提示", parent=self.parent
                    )
            except Exception as e:
                message(str(e), "获取任务返回结果失败", parent=self.parent)
            finally:
                self.progressBar.setVisible(False)
                self.pushButton_StartRun.setEnabled(False)
                self.explainthealgorithm_comboBox.setEnabled(False)
                self.pushButton_StartRun.setText("运行结束")
                self.process.kill()
                self.timer.stop()

        else:
            self.pushButton_StartRun.setText(f"获取进程运行状态码为：{exit_code}")

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
                self.directory + "/" + list_out[-6].strip("\n").replace("./", "")
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
                self.directory + "/" + (list_out[-8].split("\n")[1].split("./"))[1]
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
        }

        if dataset in dealFuncs:
            result = dealFuncs[dataset](stdout)
        elif os.path.splitext(dataset)[1] == ".skeleton":
            result = skeleton_rec_cam(stdout)
        return result


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = initTaskWindow()
    win.show()
    app.exec()
