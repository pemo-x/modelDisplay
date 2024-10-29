import pyqtgraph.opengl as gl
from pyqtgraph.Vector import Vector
from pyqtgraph.Qt import QtCore
import numpy as np
import random
from utils.dealData import getSamplesLength, getSampleDatas


# 自定义OpenGL窗口类，用于展示3D图形
class myGLWidget(gl.GLViewWidget):
    def __init__(self, filePath=None, parent=None):
        super(myGLWidget, self).__init__(parent)

        self.datas = None

        self.filePath = filePath
        self.SamplesLength = getSamplesLength(self.filePath)
        self.currentIndex = 0
        if self.SamplesLength is not None:
            self.setDatas(index=self.currentIndex)
        self.setTimer()

    # 设置网格显示
    def setGrid(self):
        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        self.addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gy.translate(0, -10, 0)
        self.addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, -10)
        self.addItem(gz)

    # 设置数据并更新图形
    def setDatas(self, index):
        self.currentIndex = index
        self.clear()
        self.setGrid()
        datas = getSampleDatas(self.filePath, index)
        if datas is None:
            return
        self.datas = datas
        self.dataLen = self.datas["points"].shape[0]
        self.frame = 0

        self.sp1 = gl.GLScatterPlotItem(
            pos=self.datas["points"][self.frame],
            size=0.05,
            color=(1.0, 1.0, 1.0, 0.5),
            pxMode=False,
        )
        self.addItem(self.sp1)

        self.linkItems = []
        if datas.get("links"):
            for each in self.datas["links"]:
                sp = gl.GLLinePlotItem(pos=self.datas["points"][(each[0], each[1])])
                self.linkItems.append(sp)
                self.addItem(sp)

        self.lineItems = []
        if datas.get("lines"):
            for line in self.datas["lines"]:
                color = list(np.random.random(4))
                for i in range(3):
                    if color[i] < 0.5:
                        color[i] += random.randint(0, 1) * 0.2 + 0.3
                color[3] = 1.0
                sp = gl.GLLinePlotItem(
                    pos=line[max(0, self.frame - self.dataLen // 10) : self.frame],
                    color=color,
                    width=2,
                )
                self.lineItems.append(sp)
                self.addItem(sp)
        centerXYZ = np.mean(self.datas["points"], axis=0).mean(axis=0)
        centerPOS = Vector(list(centerXYZ))
        self.setCameraPosition(
            pos=centerPOS, distance=np.max(self.datas["points"]) * 1.5
        )

    # 设置定时器以更新数据
    def setTimer(self):
        self.t = QtCore.QTimer(self)
        self.t.timeout.connect(self.dataUpdate)
        self.t.start(10)

    # 更新数据并刷新图形
    def dataUpdate(self):
        if self.datas is None:
            return
        self.frame = (self.frame + 1) % self.dataLen
        self.sp1.setData(pos=self.datas["points"][self.frame])

        for linkIndex in range(len(self.linkItems)):
            linkRule = (
                self.datas["links"][linkIndex][0],
                self.datas["links"][linkIndex][1],
            )
            self.linkItems[linkIndex].setData(
                pos=self.datas["points"][self.frame][[linkRule[0], linkRule[1]]]
            )

        for lineIndex in range(len(self.lineItems)):
            line = self.datas["lines"][lineIndex]
            self.lineItems[lineIndex].setData(
                pos=line[max(0, self.frame - self.dataLen // 10) : self.frame]
            )
