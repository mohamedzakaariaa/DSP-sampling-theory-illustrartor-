from os import sep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QSlider
from numpy.core.numerictypes import maximum_sctype
import pyqtgraph
from GUI import Ui_MainWindow
import sys
import csv
import numpy as np
from math import *
import numpy.fft as fft


class MainWindow(QtWidgets.QMainWindow):
    time_interval = list(np.arange(0, 100, 0.01))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.main_graph_time_interval = []
        self.main_graph_data = []
        self.current_function_values = []
        self.dic_of_sins = {}
        self.sampledTime = []
        self.sampledData = []
        self.final_output = [0.0]*10000
        self.number_of_sins = 0
        self.gui.current_wave_graph.setXRange(0, 2)
        self.gui.current_wave_graph.setYRange(-10, 10)
        self.gui.final_output_graph.setXRange(0, 2)
        self.gui.final_output_graph.setYRange(-10, 10)
        self.gui.main_graph.setXRange(0, 10)
        self.gui.secondary_graph.setXRange(0, 10)
        self.gui.main_graph.plotItem.showGrid(
            x=True, y=True, alpha=0.5)
        self.gui.secondary_graph.plotItem.showGrid(
            x=True, y=True, alpha=0.5)
        self.gui.final_output_graph.plotItem.showGrid(
            x=True, y=True, alpha=0.5)
        self.gui.current_wave_graph.plotItem.showGrid(
            x=True, y=True, alpha=0.5)
        self.gui.slider.setMinimum(0)
        self.gui.slider.setMaximum(10)
        self.gui.slider.setValue(0)
        self.gui.slider.setTickInterval(1)
        self.gui.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.pen1 = pyqtgraph.mkPen((255, 0, 0), width=3)
        self.pen2 = pyqtgraph.mkPen((0, 255, 0), width=3)
        self.gui.amplitude_input.textChanged.connect(self.plot_current_sin)
        self.gui.frequency_input.textChanged.connect(self.plot_current_sin)
        self.gui.phase_shift_input.textChanged.connect(self.plot_current_sin)
        self.gui.add_botton.clicked.connect(self.add_wave)
        self.gui.move_botton.clicked.connect(self.move_signal)
        self.gui.list_of_sinusoidals.itemDoubleClicked.connect(
            self.remove_wave)
        self.gui.open_action.triggered.connect(self.Open_Signal)
        self.gui.slider.valueChanged.connect(self.sampleSignal)
        self.gui.Reconstruct_botton.clicked.connect(self.reconstruct)
        self.show()

    def Open_Signal(self):
        self.main_graph_data.clear()
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            None, "Open File", r"D:/SBME_3/1st_term/DSP/tasks/task2", "Signals(*.csv)", options=options)
        with open(fileName, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            # next(csv_reader)
            for line in csv_reader:
                self.main_graph_data.append(line[1])
        for counter in range(len(self.main_graph_data)):
            self.main_graph_data[counter] = float(
                self.main_graph_data[counter])
        self.plot_main_graph()
        self.calculate_fmax()

    def move_signal(self):
        self.main_graph_data = self.final_output
        self.plot_main_graph()
        self.gui.slider.setValue(0)
        self.gui.secondary_graph.plotItem.clear()
        self.calculate_fmax()

    def plot_main_graph(self):
        self.main_graph_time_interval = list(np.arange(
            0, (len(self.main_graph_data)*0.01), 0.01))
        maximum_value = max(self.main_graph_data)
        minimum_value = min(self.main_graph_data)
        self.gui.main_graph.setYRange((minimum_value-0.5), (maximum_value+0.5))
        print(len(self.main_graph_data))
        print(len(self.main_graph_time_interval))
        self.gui.main_graph.plotItem.clear()
        self.gui.main_graph.plotItem.plot(
            self.main_graph_time_interval, self.main_graph_data, pen=self.pen1)

    def calculate_fmax(self):
        spectrum = np.fft.fft(self.main_graph_data)
        freq = np.fft.fftfreq(len(spectrum))
        threshold = 0.5 * max(abs(spectrum))
        mask = abs(spectrum) > threshold
        peaks = freq[mask]
        peaks = abs(peaks)
        max_samplling_frequency = 3 * int(max(peaks)*100)
        self.gui.slider.setMaximum(max_samplling_frequency)
        self.gui.fmax_label.setText(f"fmax = {int(max(peaks)*100)}")

    def sampleSignal(self):
        self.sampledData.clear()
        self.sampledTime.clear()
        slider_value = int(self.gui.slider.value())
        self.gui.slider_value_label.setText(str(slider_value))
        samplingFrequency = slider_value
        if samplingFrequency == 0:
            self.gui.main_graph.plotItem.clear()
            self.gui.main_graph.plotItem.plot(
                self.main_graph_time_interval, self.main_graph_data, pen=self.pen1)
            self.sampledData.clear()
            self.sampledTime.clear()
        else:
            sample_step = 1/samplingFrequency
            self.sampledTime = list(np.arange(
                0, (len(self.main_graph_data)*0.01), sample_step))
            self.build_samples_list()
            self.gui.main_graph.plotItem.clear()
            self.gui.main_graph.plotItem.plot(
                self.main_graph_time_interval, self.main_graph_data, pen=self.pen1)
            self.gui.main_graph.plotItem.plot(
                self.sampledTime, self.sampledData, symbol='o', pen=None)
        print(len(self.sampledData))
        print(len(self.sampledTime))

    def build_samples_list(self):
        new_step = 0
        search_element = self.sampledTime[1]
        for item in self.main_graph_time_interval:
            if item >= search_element:
                new_step = self.main_graph_time_interval.index(item)
                break
        length = 0
        while length < (len(self.main_graph_data)):
            self.sampledData.append(self.main_graph_data[length])
            length += new_step
        if len(self.sampledData) < len(self.sampledTime):
            self.sampledTime = self.sampledTime[:len(self.sampledData)]
        if len(self.sampledData) > len(self.sampledTime):
            self.sampledData = self.sampledData[:len(self.sampledTime)]

    def reconstruct(self):
        fs = int(self.gui.slider.value())
        time = np.array(self.main_graph_time_interval)
        samples = np.array(self.sampledData)
        # num_coeffs = len(self.sampledTime)  # sample points
        x_reconstructed = 0
        for k in range(len(self.sampledTime)):  # since function is real, need both sides
            x_reconstructed += (((samples[k]) * (
                np.sinc(k - fs * time))))

        self.gui.secondary_graph.plotItem.clear()
        self.gui.secondary_graph.plotItem.plot(
            self.main_graph_time_interval, x_reconstructed, pen=self.pen1)
        self.gui.main_graph.plotItem.clear()
        self.gui.main_graph.plotItem.plot(
            self.main_graph_time_interval, self.main_graph_data, pen=self.pen1)
        self.gui.main_graph.plotItem.plot(
            self.main_graph_time_interval, x_reconstructed, pen=pyqtgraph.mkPen(color=(0, 255, 0), style=QtCore.Qt.DotLine))
        

    def plot_current_sin(self):
        self.current_function_values.clear()
        amplitude = self.gui.amplitude_input.text()
        frequency = self.gui.frequency_input.text()
        phase = self.gui.phase_shift_input.text()
        if amplitude != "" and frequency != "" and phase != "":
            amplitude = float(amplitude)
            frequency = float(frequency)
            phase = float(phase)
            for time in self.time_interval:
                self.current_function_values.append(
                    amplitude*(np.sin((2*pi*frequency*time)+np.deg2rad(phase))))
            # print(len(self.time_interval))
            self.gui.current_wave_graph.plotItem.clear()
            self.gui.current_wave_graph.plotItem.plot(
                self.time_interval, self.current_function_values, pen=pyqtgraph.mkPen((255, 0, 0), width=3))
            global current_sins
            current_sins = []
            for i in range(0, len(self.current_function_values)):
                current_sins.append(self.current_function_values[i])
            # print(current_sins)

        else:
            self.gui.current_wave_graph.plotItem.clear()

    def add_wave(self):
        # self.current_sins.append(self.current_function_values)
        # print(current_sins)
        self.dic_of_sins[f"Sinusoidal number  {self.number_of_sins}"] = current_sins
        # print(self.dic_of_sins)
        for key in self.dic_of_sins.keys():
            print(key+" "+str(self.dic_of_sins.get(key)[10]))
        self.increment_final_output(self.current_function_values)
        # print(
        #     f"after adding sin {self.number_of_sins} final[10] {self.final_output[10]}")

        self.plot_final_output()
        self.gui.list_of_sinusoidals.addItem(QtWidgets.QListWidgetItem(
            f"Sinusoidal number  {self.number_of_sins}"))
        self.number_of_sins += 1

    def increment_final_output(self, current_values):
        for counter in range(len(self.final_output)):
            self.final_output[counter] += current_values[counter]

    def plot_final_output(self):
        self.gui.final_output_graph.plotItem.clear()
        self.gui.final_output_graph.plotItem.plot(
            self.time_interval, self.final_output, pen=pyqtgraph.mkPen((0, 255, 0), width=3))

    def remove_wave(self):
        current_item = self.gui.list_of_sinusoidals.currentItem()
        name = current_item.text()
        # print(name)
        current_row = self.gui.list_of_sinusoidals.currentRow()
        # print(current_row)
        self.gui.list_of_sinusoidals.takeItem(current_row)
        # print(self.gui.list_of_sinusoidals.items())
        selected_values = self.dic_of_sins.get(name)
        self.dic_of_sins.pop(name)
        # print(self.dic_of_sins.keys())
        # self.rebuild_final_output()
        self.decrement_final_output(selected_values)
        print(f"after removing {name} final[10] = {self.final_output[10]}")
        self.plot_final_output()
        self.number_of_sins -= 1

    # def rebuild_final_output(self):
    #     self.final_output = [0.0]*5100
    #     # print(self.dic_of_sins.keys())
    #     for item in (self.dic_of_sins.keys()):
    #         # print(item)
    #         current_values = self.dic_of_sins.get(item)
    #         self.increment_final_output(current_values)

    def decrement_final_output(self, selected_values):
        for counter in range(len(self.final_output)):
            self.final_output[counter] -= selected_values[counter]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    illustrator = MainWindow()
    sys.exit(app.exec_())
