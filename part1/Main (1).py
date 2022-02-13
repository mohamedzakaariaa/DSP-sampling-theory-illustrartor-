from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import QScreen
from PyQt5.Qt import QFileInfo
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import QFileDialog, QSlider
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from GUI2 import Ui_MainWindow
import matplotlib
from pandas.core.base import SpecificationError
from pyqtgraph.widgets.ComboBox import ComboBox
matplotlib.use('Qt5Agg')


class signalType(object):
    def __init__(self, time=[], value=[]):
        self.time = time
        self.value = value


latestWave = []
data = []
time = []


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.open_action.triggered.connect(self.Open_Signal)
        self.gui.Reconstruct_botton.clicked.connect(self.sampleSignal)
        self.gui.slider.valueChanged.connect(self.sampleSignal)
        self.pen1 = pg.mkPen((255, 0, 0), width=3)
        self.pen2 = pg.mkPen((0, 0, 255), width=3)

        self.show()
        # self.CreateSin()

    def Open_Signal(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            None, "Open File", r"C:\Users\Hesham\Desktop\task 2", "Signals(*.csv)", options=options)
        data_set = pd.read_csv(fileName, header=1)
        data_set = data_set[1:].astype(float)
        File = data_set.iloc[:, 0]

        for i in range(1, (len(File)+1)):
            data.append(File[i])

        for i in range(0, (len(File))):
            time.append(i)

        self.gui.main_graph.plot(time, data, pen=self.pen1)

    # def CreateSin(self):
    #     # print("hello")
    #     f = 100   # get it from the user
    #     t = 100
    #     omega = 2*np.pi*f
    #     t_vec = np.arange(0, t, 10)
    #     print(t_vec)
    #     Amplitude = 1    # get it from the user
    #     phase = 0  # get it from the user
    #     y = Amplitude*np.sin((omega*t_vec)+phase)
    #     print(y)
    #     # self.gui.main_graph.deleteLater()
    #     print("hello")
    #     self.gui.main_graph.plot(t_vec, y, pen=self.pen1)
    #     if self.add_botton.clicked:
    #         self.addSin(y, t_vec)

    #         self.latestData()

    # def addSin(self, y, t_vec):
    #     allData.append(y)
    #     for i in range(0, t_vec):
    #         latestWave[i] += y[i]
    #     self.latestgraph.plot(t_vec, latestWave, pen=self.pen2)
    # def latestData(self):

    # class sampler(object):
    #     def __init__(self):
    #         self.sampledSignal = signalType()

    def sampleSignal(self):
        sampledTime = []
        sampledData = []
        samplingFrequency = int(self.gui.slider.value())
        signalDuration = time[1]-time[0]
        signalLength = len(time)
        # find sampling period in index, signalLength points in samplingDuration so how many points in sampling time?
        # then for sampling pick 1 data from points coming in sampling duration
        samplingIndexPeriod = np.floor(
            signalLength/(signalDuration*samplingFrequency)).astype(int)

        sampledDataIndex = np.arange(
            0, signalLength, samplingIndexPeriod, dtype=int)
        for i in range(0, len(sampledDataIndex)):
            sampledTime.append(time[sampledDataIndex[i]])
            sampledData.append(data[sampledDataIndex[i]])
        print(sampledTime)
        print(sampledData)
        self.gui.main_graph.clear()
        self.gui.main_graph.plot(time, data, pen=self.pen1)
        self.gui.main_graph.plot(
            sampledTime, sampledData, linestyle='dotted', pen=self.pen2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    illustrator = MainWindow()
    sys.exit(app.exec_())
