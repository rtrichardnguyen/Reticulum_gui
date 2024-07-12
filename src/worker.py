import sys
import subprocess
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal


class Worker(QThread):
    output_signal = pyqtSignal(str)

    def run(self):
        process = subprocess.Popen(
            ['nomadnet'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                self.output_signal.emit(output.strip())

            remaining = process.communicate()[0]
            
            if remaining:
                self.output_signal.emit(remaining.strip())