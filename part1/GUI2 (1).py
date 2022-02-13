# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import QScreen
from PyQt5.Qt import QFileInfo
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import QFileDialog, QSlider
from scipy import signal
from fpdf import FPDF
# from numpy.lib.function_base import average
# from numpy.core.fromnumeric import mean, std
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd
# import pyqtgraph.exporters
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os
# from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib
from pandas.core.base import SpecificationError
# from pyqtgraph.widgets.ComboBox import ComboBox
# matplotlib.use('Qt5Agg')


class signalType(object):
    def __init__(self, time=[], value=[]):
        self.time = time
        self.value = value


latestWave = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 631)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName("tab_widget")
        self.Sampling = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Sampling.setFont(font)
        self.Sampling.setObjectName("Sampling")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Sampling)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Reconstruct_botton = QtWidgets.QPushButton(self.Sampling)
        self.Reconstruct_botton.setObjectName("Reconstruct_botton")
        self.horizontalLayout_2.addWidget(self.Reconstruct_botton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.splitter = QtWidgets.QSplitter(self.Sampling)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.uper_widget = QtWidgets.QWidget(self.splitter)
        self.uper_widget.setObjectName("uper_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.uper_widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_graph_title_label = QtWidgets.QLabel(self.uper_widget)
        self.main_graph_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_graph_title_label.setObjectName("main_graph_title_label")
        self.verticalLayout_2.addWidget(self.main_graph_title_label)
        self.main_graph = PlotWidget(self.uper_widget)
        self.main_graph.setObjectName("main_graph")
        self.verticalLayout_2.addWidget(self.main_graph)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slider = QtWidgets.QSlider(self.uper_widget)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.slider.setMinimum(10)
        self.slider.setMaximum(100)
        self.slider.setValue(0)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.horizontalLayout.addWidget(self.slider)
        self.slider_value_label = QtWidgets.QLabel(self.uper_widget)
        self.slider_value_label.setMinimumSize(QtCore.QSize(20, 0))
        self.slider_value_label.setObjectName("slider_value_label")
        self.horizontalLayout.addWidget(self.slider_value_label)
        self.aampling_botton = QtWidgets.QPushButton(self.uper_widget)
        self.aampling_botton.setObjectName("aampling_botton")
        self.horizontalLayout.addWidget(self.aampling_botton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.lower_widget = QtWidgets.QWidget(self.splitter)
        self.lower_widget.setObjectName("lower_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.lower_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sec_graph_title_label = QtWidgets.QLabel(self.lower_widget)
        self.sec_graph_title_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sec_graph_title_label.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.sec_graph_title_label.setObjectName("sec_graph_title_label")
        self.verticalLayout_3.addWidget(self.sec_graph_title_label)
        self.secondary_graph = PlotWidget(self.lower_widget)
        self.secondary_graph.setObjectName("secondary_graph")
        self.verticalLayout_3.addWidget(self.secondary_graph)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addWidget(self.splitter)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tab_widget.addTab(self.Sampling, "")
        self.Composer = QtWidgets.QWidget()
        self.Composer.setObjectName("Composer")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Composer)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.up_left_layout = QtWidgets.QVBoxLayout()
        self.up_left_layout.setObjectName("up_left_layout")
        self.current_wave_title_label = QtWidgets.QLabel(self.Composer)
        self.current_wave_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_wave_title_label.setObjectName("current_wave_title_label")
        self.up_left_layout.addWidget(self.current_wave_title_label)
        self.current_wave_graph = PlotWidget(self.Composer)
        self.current_wave_graph.setObjectName("current_wave_graph")
        self.up_left_layout.addWidget(self.current_wave_graph)
        self.horizontalLayout_3.addLayout(self.up_left_layout)
        self.up_right_layout = QtWidgets.QVBoxLayout()
        self.up_right_layout.setObjectName("up_right_layout")
        self.amplitude_label = QtWidgets.QLabel(self.Composer)
        self.amplitude_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.amplitude_label.sizePolicy().hasHeightForWidth())
        self.amplitude_label.setSizePolicy(sizePolicy)
        self.amplitude_label.setBaseSize(QtCore.QSize(0, 0))
        self.amplitude_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.amplitude_label.setAlignment(QtCore.Qt.AlignCenter)
        self.amplitude_label.setObjectName("amplitude_label")
        self.up_right_layout.addWidget(self.amplitude_label)
        self.amplitude_input = QtWidgets.QLineEdit(self.Composer)
        self.amplitude_input.setObjectName("amplitude_input")
        self.up_right_layout.addWidget(self.amplitude_input)
        self.frequency_label = QtWidgets.QLabel(self.Composer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frequency_label.sizePolicy().hasHeightForWidth())
        self.frequency_label.setSizePolicy(sizePolicy)
        self.frequency_label.setAlignment(QtCore.Qt.AlignCenter)
        self.frequency_label.setObjectName("frequency_label")
        self.up_right_layout.addWidget(self.frequency_label)
        self.frequency_input = QtWidgets.QLineEdit(self.Composer)
        self.frequency_input.setObjectName("frequency_input")
        self.up_right_layout.addWidget(self.frequency_input)
        self.phase_shift_label = QtWidgets.QLabel(self.Composer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.phase_shift_label.sizePolicy().hasHeightForWidth())
        self.phase_shift_label.setSizePolicy(sizePolicy)
        self.phase_shift_label.setAlignment(QtCore.Qt.AlignCenter)
        self.phase_shift_label.setObjectName("phase_shift_label")
        self.up_right_layout.addWidget(self.phase_shift_label)
        self.phase_shift_input = QtWidgets.QLineEdit(self.Composer)
        self.phase_shift_input.setObjectName("phase_shift_input")
        self.up_right_layout.addWidget(self.phase_shift_input)
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.up_right_layout.addItem(spacerItem)
        self.add_botton = QtWidgets.QPushButton(self.Composer)
        self.add_botton.setObjectName("add_botton")
        self.up_right_layout.addWidget(self.add_botton)
        spacerItem1 = QtWidgets.QSpacerItem(
            18, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.up_right_layout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.up_right_layout)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.down_lef_layour = QtWidgets.QVBoxLayout()
        self.down_lef_layour.setObjectName("down_lef_layour")
        self.final_graph_title_label = QtWidgets.QLabel(self.Composer)
        self.final_graph_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.final_graph_title_label.setObjectName("final_graph_title_label")
        self.down_lef_layour.addWidget(self.final_graph_title_label)
        self.final_output_graph = PlotWidget(self.Composer)
        self.final_output_graph.setObjectName("final_output_graph")
        self.down_lef_layour.addWidget(self.final_output_graph)
        self.horizontalLayout_4.addLayout(self.down_lef_layour)
        self.down_right_layout = QtWidgets.QVBoxLayout()
        self.down_right_layout.setObjectName("down_right_layout")
        self.list_view_title_label = QtWidgets.QLabel(self.Composer)
        self.list_view_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.list_view_title_label.setObjectName("list_view_title_label")
        self.down_right_layout.addWidget(self.list_view_title_label)
        self.list_of_sinusoidals = QtWidgets.QListView(self.Composer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.list_of_sinusoidals.sizePolicy().hasHeightForWidth())
        self.list_of_sinusoidals.setSizePolicy(sizePolicy)
        self.list_of_sinusoidals.setMovement(QtWidgets.QListView.Static)
        self.list_of_sinusoidals.setObjectName("list_of_sinusoidals")
        self.down_right_layout.addWidget(self.list_of_sinusoidals)
        self.horizontalLayout_4.addLayout(self.down_right_layout)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.move_botton = QtWidgets.QPushButton(self.Composer)
        self.move_botton.setObjectName("move_botton")
        self.verticalLayout_11.addWidget(self.move_botton)
        self.verticalLayout_8.addLayout(self.verticalLayout_11)
        self.verticalLayout_14.addLayout(self.verticalLayout_8)
        self.tab_widget.addTab(self.Composer, "")
        self.verticalLayout.addWidget(self.tab_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 23))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_action = QtWidgets.QAction(MainWindow)
        self.open_action.setObjectName("open_action")
        self.file_menu.addAction(self.open_action)
        self.menubar.addAction(self.file_menu.menuAction())

        self.pen1 = pg.mkPen((255, 0, 0), width=3)
        self.pen2 = pg.mkPen((0, 255, 0), width=3)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Signal Illustrator"))
        self.Reconstruct_botton.setText(
            _translate("MainWindow", "Reconstruct"))
        self.main_graph_title_label.setText(
            _translate("MainWindow", "main graph"))
        self.slider_value_label.setText(_translate("MainWindow", "0"))
        self.aampling_botton.setText(_translate("MainWindow", "OK"))
        self.sec_graph_title_label.setText(
            _translate("MainWindow", "Reconstructed graph"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(
            self.Sampling), _translate("MainWindow", "Sampling"))
        self.current_wave_title_label.setText(
            _translate("MainWindow", "current wave"))
        self.amplitude_label.setText(_translate("MainWindow", "Amplitude"))
        self.frequency_label.setText(_translate("MainWindow", "Frequency"))
        self.phase_shift_label.setText(_translate("MainWindow", "Phase shift"))
        self.add_botton.setText(_translate("MainWindow", "Add"))
        self.final_graph_title_label.setText(
            _translate("MainWindow", "final output"))
        self.list_view_title_label.setText(
            _translate("MainWindow", "list of sinusoidals"))
        self.move_botton.setText(_translate("MainWindow", "MOVE"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(
            self.Composer), _translate("MainWindow", "Composer"))
        self.file_menu.setTitle(_translate("MainWindow", "File"))
        self.open_action.setText(_translate("MainWindow", "open"))

#     def open_action(self):
#         global F1, time, selector
#         options = QFileDialog.Options()
#         fileName, _ = QFileDialog.getOpenFileName(
#             None, "Open File", r"E:\CUFE\Signals", "Signals(*.csv)", options=options)
#         data_set = pd.read_csv(fileName, header=1)
#         data_set = data_set[1:].astype(float)
#         File = data_set.iloc[:, 0]

#         data = []
#         time = []

#         for i in range(1, (len(File)+1)):
#             data.append(File[i])

#         for i in range(0, (len(File))):
#             time.append(i + self.x_range1[1])

#         self.main_graph.setYRange(self.ymin_scale1, self.ymax_scale1)

#         if self.x_range1[0] == 0:
#             self.main_graph.setXRange(self.xmin_scale1, self.xmax_scale1)
#         else:
#             self.main_graph.setXRange(self.x_range1[0], self.x_range1[1])
#         self.x_range1 = self.main_graph.getViewBox(
#         ).state['viewRange'][0]
#         self.y_range1 = self.main_graph.getViewBox(
#         ).state['viewRange'][1]

#     # def CreateSin(self):
#     #     # print("hello")
#     #     f = 100   # get it from the user
#     #     t = 0.1
#     #     omega = 2*np.pi*f
#     #     t_vec = np.arange(t)
#     #     Amplitude = 10    # get it from the user
#     #     phase = 0  # get it from the user
#     #     y = Amplitude*np.sin((omega*t_vec)+phase)
#     #     self.singraph.deleteLater()
#     #     self.singraph.plot(t_vec, y, pen=self.pen1)
#     #     if self.add_botton.clicked:
#     #         self.addSin(y, t_vec)

#     #         self.latestData()

#     # def addSin(self, y, t_vec):
#     #     allData.append(y)
#     #     for i in range(0, t_vec):
#     #         latestWave[i] += y[i]
#     #     self.latestgraph.plot(t_vec, latestWave, pen=self.pen2)
#     # def latestData(self):


# class sampler(object):
#     def __init__(self):
#         self.sampledSignal = signalType()

#     def sampleSignal(self, data, time, samplingFrequency):
#         samplingFrequency = int(self.speed_slider.value())
#         signalDuration = time[-1]-time[0]
#         signalLength = len(time)
#         # find sampling period in index, signalLength points in samplingDuration so how many points in sampling time?
#         # then for sampling pick 1 data from points coming in sampling duration
#         samplingIndexPeriod = np.floor(
#             signalLength/(signalDuration*samplingFrequency)).astype(int)
#         sampledDataIndex = np.arange(
#             0, signalLength, samplingIndexPeriod, dtype=int)

#         self.sampledSignal.time = time[sampledDataIndex]
#         self.sampledSignal.value = data[sampledDataIndex]

#         self.maingraph.plot(self.sampledSignal.time, self.sampledSignal.value)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
