import sys
import subprocess
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal

class Worker(QThread):
    output_signal = pyqtSignal(str)

    def run(self):
        pass