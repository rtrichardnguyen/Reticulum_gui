# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ret_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# pyuic5 -x ui_file.ui -o py_file.py

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import re
import os
import sys
import serial.tools.list_ports
from config_profile import Profile


class Ui_ReticulumGUI(object):
    def setupUi(self, ReticulumGUI):
        ReticulumGUI.setObjectName("ReticulumGUI")
        ReticulumGUI.resize(732, 560)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "../../Downloads/reticulum_logo_512.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ReticulumGUI.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ReticulumGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.freqCombo = QtWidgets.QComboBox(self.centralwidget)
        self.freqCombo.setGeometry(QtCore.QRect(180, 170, 101, 31))
        self.freqCombo.setObjectName("freqCombo")
        self.freqCombo.addItem("")
        self.freqCombo.addItem("")
        self.freqCombo.addItem("")
        self.freqCombo.addItem("")
        self.spreadCombo = QtWidgets.QComboBox(self.centralwidget)
        self.spreadCombo.setGeometry(QtCore.QRect(180, 210, 101, 31))
        self.spreadCombo.setObjectName("spreadCombo")
        self.spreadCombo.addItem("")
        self.spreadCombo.addItem("")
        self.spreadCombo.addItem("")
        self.spreadCombo.addItem("")
        self.spreadCombo.addItem("")
        self.spreadCombo.addItem("")
        self.codingCombo = QtWidgets.QComboBox(self.centralwidget)
        self.codingCombo.setGeometry(QtCore.QRect(180, 250, 101, 31))
        self.codingCombo.setObjectName("codingCombo")
        self.codingCombo.addItem("")
        self.codingCombo.addItem("")
        self.codingCombo.addItem("")
        self.codingCombo.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 180, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 300, 161, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 340, 161, 16))
        self.label_5.setObjectName("label_5")
        self.jumpCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.jumpCheck.setGeometry(QtCore.QRect(10, 130, 111, 31))
        self.jumpCheck.setObjectName("jumpCheck")
        self.outputText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.outputText.setGeometry(QtCore.QRect(383, 30, 331, 91))
        self.outputText.setReadOnly(True)
        self.outputText.setObjectName("descriptionText")
        self.descriptionText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.descriptionText.setGeometry(QtCore.QRect(380, 140, 331, 291))
        self.descriptionText.setReadOnly(True)
        self.descriptionText.setObjectName("outputText")
        self.uploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadButton.setGeometry(QtCore.QRect(380, 450, 91, 24))
        self.uploadButton.setObjectName("meshchat_button")
        self.meshchat_button = QtWidgets.QPushButton(self.centralwidget)
        self.meshchat_button.setGeometry(QtCore.QRect(500, 450, 91, 24))
        self.meshchat_button.setObjectName("meshchat_button")
        self.jump_button = QtWidgets.QPushButton(self.centralwidget)
        self.jump_button.setGeometry(QtCore.QRect(620, 450, 91, 24))
        self.jump_button.setObjectName("jump_button")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(10, 450, 75, 24))
        self.saveButton.setObjectName("saveButton")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(100, 450, 75, 24))
        self.loadButton.setObjectName("loadButton")
        self.bandCombo = QtWidgets.QLineEdit(self.centralwidget)
        self.bandCombo.setGeometry(QtCore.QRect(180, 300, 113, 21))
        self.bandCombo.setObjectName("bandCombo")
        self.txCombo = QtWidgets.QLineEdit(self.centralwidget)
        self.txCombo.setGeometry(QtCore.QRect(180, 340, 113, 21))
        self.txCombo.setObjectName("txCombo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(323, 20, 20, 451))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(380, 120, 331, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 40, 111, 111))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../reticulum_logo_512.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(390, 10, 211, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.txCombo_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txCombo_2.setGeometry(QtCore.QRect(10, 410, 281, 21))
        self.txCombo_2.setObjectName("txCombo_2")

        # DROP DOWN =================

        self.loadDropDown = QtWidgets.QComboBox(self.centralwidget)
        self.loadDropDown.setGeometry(QtCore.QRect(190, 450, 131, 24))
        self.loadDropDown.setObjectName("cloadDropDown")

        # END DROP DOWN =============

        self.label_7.raise_()
        self.freqCombo.raise_()
        self.spreadCombo.raise_()
        self.codingCombo.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.jumpCheck.raise_()
        self.descriptionText.raise_()
        self.outputText.raise_()
        self.uploadButton.raise_()
        self.meshchat_button.raise_()
        self.jump_button.raise_()
        self.saveButton.raise_()
        self.loadButton.raise_()
        self.bandCombo.raise_()
        self.txCombo.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_8.raise_()
        #self.progressBar.raise_()
        self.pushButton.raise_()
        self.txCombo_2.raise_()
        self.label_6.raise_()

        self.loadDropDown.raise_()  # edited

        ReticulumGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ReticulumGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 22))
        self.menubar.setObjectName("menubar")
        self.menuReticulum_GUI = QtWidgets.QMenu(self.menubar)
        self.menuReticulum_GUI.setObjectName("menuReticulum_GUI")
        self.menuNew_Tab = QtWidgets.QMenu(self.menubar)
        self.menuNew_Tab.setObjectName("menuNew_Tab")
        ReticulumGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ReticulumGUI)
        self.statusbar.setObjectName("statusbar")
        ReticulumGUI.setStatusBar(self.statusbar)
        self.actionTest = QtGui.QAction(ReticulumGUI)
        self.actionTest.setObjectName("actionTest")
        self.actionTest_2 = QtGui.QAction(ReticulumGUI)
        self.actionTest_2.setObjectName("actionTest_2")
        self.actionHelp = QtGui.QAction(ReticulumGUI)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExit = QtGui.QAction(ReticulumGUI)
        self.actionExit.setObjectName("actionExit")
        self.menuReticulum_GUI.addAction(self.actionTest)
        self.menuReticulum_GUI.addAction(self.actionTest_2)
        self.menuReticulum_GUI.addAction(self.actionHelp)
        self.menuReticulum_GUI.addAction(self.actionExit)
        self.menubar.addAction(self.menuReticulum_GUI.menuAction())
        self.menubar.addAction(self.menuNew_Tab.menuAction())
        self.label.setBuddy(self.freqCombo)
        self.label_2.setBuddy(self.spreadCombo)
        self.label_3.setBuddy(self.codingCombo)
        self.label_4.setBuddy(self.bandCombo)
        self.label_5.setBuddy(self.txCombo)
        self.label_8.setBuddy(self.descriptionText)

        self.retranslateUi(ReticulumGUI)
        self.jumpCheck.toggled.connect(
            self.spreadCombo.setHidden)  # type: ignore
        self.jumpCheck.toggled.connect(
            self.codingCombo.setHidden)  # type: ignore
        #self.uploadButton.clicked.connect(
        #    self.progressBar.show)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ReticulumGUI)
        ReticulumGUI.setTabOrder(self.jumpCheck, self.freqCombo)
        ReticulumGUI.setTabOrder(self.freqCombo, self.spreadCombo)
        ReticulumGUI.setTabOrder(self.spreadCombo, self.codingCombo)
        ReticulumGUI.setTabOrder(self.codingCombo, self.bandCombo)
        ReticulumGUI.setTabOrder(self.bandCombo, self.txCombo)
        ReticulumGUI.setTabOrder(self.txCombo, self.saveButton)
        ReticulumGUI.setTabOrder(self.saveButton, self.loadButton)
        ReticulumGUI.setTabOrder(self.loadButton, self.uploadButton)
        ReticulumGUI.setTabOrder(self.uploadButton, self.descriptionText)
        ReticulumGUI.setTabOrder(self.descriptionText, self.outputText)

        ### REST OF THE FUNCTION WAS PROGRAMMED MANUALLY ###
        os.system("echo Installing Reticulum and NomadNet >> ../output.txt")
        os.system("pip install rns >> ../output.txt")
        os.system("pip install nomadnet >> ../output.txt")

        output_file = open("../output.txt", "r")
        self.descriptionText.appendPlainText(output_file.read())
        output_file.close()
        self.descriptionText.appendPlainText("Finished installing RNS and NomadNet\n")
        os.system("rm ../output.txt")

        self.profile_list = {}
        self.load_profiles(self.profile_list)

        instruction_file = open("../instructions.txt", "r")
        self.outputText.appendPlainText(instruction_file.read())

        self.uploadButton.clicked.connect(self.run_nomadnet)
        self.meshchat_button.clicked.connect(self.run_meshchat)
        self.jump_button.clicked.connect(self.run_rnsd)

        self.saveButton.clicked.connect(self.save_profile)
        instruction_file.close()

        self.w = None  # No external window yet.
        self.loadButton.clicked.connect(self.delete_profile)

        self.loadDropDown.addItems([*self.profile_list])
        self.loadDropDown.currentIndexChanged.connect(self.fill_profile)

        self.pushButton.clicked.connect(self.flash_ports)

    def retranslateUi(self, ReticulumGUI):
        _translate = QtCore.QCoreApplication.translate
        ReticulumGUI.setWindowTitle(_translate("ReticulumGUI", "MainWindow"))
        self.freqCombo.setItemText(0, _translate("ReticulumGUI", "433 MHz"))
        self.freqCombo.setItemText(1, _translate("ReticulumGUI", "868 MHz"))
        self.freqCombo.setItemText(2, _translate("ReticulumGUI", "915 MHz"))
        self.freqCombo.setItemText(3, _translate("ReticulumGUI", "2.4 GHz*"))
        self.spreadCombo.setItemText(0, _translate("ReticulumGUI", "7"))
        self.spreadCombo.setItemText(1, _translate("ReticulumGUI", "8"))
        self.spreadCombo.setItemText(2, _translate("ReticulumGUI", "9"))
        self.spreadCombo.setItemText(3, _translate("ReticulumGUI", "10"))
        self.spreadCombo.setItemText(4, _translate("ReticulumGUI", "11"))
        self.spreadCombo.setItemText(5, _translate("ReticulumGUI", "12"))
        self.codingCombo.setItemText(0, _translate("ReticulumGUI", "5"))
        self.codingCombo.setItemText(1, _translate("ReticulumGUI", "6"))
        self.codingCombo.setItemText(2, _translate("ReticulumGUI", "7"))
        self.codingCombo.setItemText(3, _translate("ReticulumGUI", "8"))
        self.label.setText(_translate("ReticulumGUI", "Frequency (Hz)"))
        self.label_2.setText(_translate("ReticulumGUI", "Spreading Factor"))
        self.label_3.setText(_translate("ReticulumGUI", "Coding Rate"))
        self.label_4.setText(_translate("ReticulumGUI", "Bandwidth (KHz)"))
        self.label_5.setText(_translate(
            "ReticulumGUI", "Transmit Power (dBm)"))
        self.jumpCheck.setText(_translate("ReticulumGUI", "Jump Node?"))
        self.uploadButton.setText(_translate("ReticulumGUI", "NomadNet"))
        self.meshchat_button.setText(_translate("ReticulumGUI", "MeshChat"))
        self.jump_button.setText(_translate("ReticulumGUI", "Terminal"))
        self.txCombo_2.setText(_translate("ReticulumGUI", "Profile Name"))
        self.saveButton.setText(_translate("ReticulumGUI", "Save"))
        self.loadButton.setText(_translate("ReticulumGUI", "Delete"))
        self.label_6.setText(_translate("ReticulumGUI", "Reticulum GUI"))
        self.label_8.setText(_translate("ReticulumGUI", "Output:"))
        self.pushButton.setText(_translate("ReticulumGUI", "Flash"))
        self.menuReticulum_GUI.setTitle(_translate("ReticulumGUI", "Menu"))
        self.menuNew_Tab.setTitle(_translate("ReticulumGUI", "New Tab"))
        self.actionTest.setText(_translate("ReticulumGUI", "New.."))
        self.actionTest_2.setText(_translate("ReticulumGUI", "Edit.."))
        self.actionHelp.setText(_translate("ReticulumGUI", "Help.."))
        self.actionExit.setText(_translate("ReticulumGUI", "Exit."))

    def run_nomadnet(self):
        if self.parse_fields():
            os.system("nomadnet")

    def run_meshchat(self):
        if self.parse_fields():
            os.system("python3 ../reticulum-meshchat/meshchat.py")

    def run_rnsd(self):
        if self.parse_fields():
            os.system("rnsd -vvv")

    def parse_fields(self):

        enable_transport = self.jumpCheck.isChecked()

        frequency = self.freqCombo.currentText()
        spreading_factor = 0
        coding_rate = 0
        bandwidth = 0
        transmit_power = 0
        try:

            if not enable_transport:
                spreading_factor = int(self.spreadCombo.currentText())
                coding_rate = int(self.codingCombo.currentText())

            bandwidth = int(self.bandCombo.text())
            transmit_power = int(self.txCombo.text())

            print(bandwidth)
            print(transmit_power)

            if frequency == '2.4 GHz*':
                frequency = 240000000000  # correct this
            elif frequency == '433 MHz':
                frequency = 433000000  # correct this
            elif frequency == '868 MHz':
                frequency = 867200000
            elif frequency == '915 MHz':
                frequency = 915000000  # correct this
            else:
                frequency = int(re.search('[0-9]{3}', frequency).group())

        except:
            self.descriptionText.appendPlainText(
                "Incorrect bandwidth or transmit power field format.\n")
            return False

        try:
            # try absolute path
            config = open("../../.reticulum/config", "w")

            config.write("[reticulum]\n\n" +
                         f"  enable_transport = {enable_transport}\n\n" +
                         "  shared_instance_port = 37428\n" +
                         "  instance_control_port = 37429\n\n" +
                         "  panic_on_interface_error = No\n\n")

            config.write("[logging]\n" +
                         "  loglevel = 4\n\n")

            config.write("[interfaces]\n" +
                         "  [[Default Interface]]\n" +
                         "    type = AutoInterface\n" +
                         "    interface_enabled = True\n\n")

            config.write("  [[RNode LoRa Interface]]\n\n" +
                         "    type = RNodeInterface\n"
                         "    interface_enabled = True\n" +
                         "    port = /dev/ttyACM0\n" +  # can also be ttyUSB0, create try catch conversion
                         f"    frequency = {frequency}\n" +
                         f"    bandwidth = {bandwidth}\n" +
                         f"    txpower = {transmit_power}\n")

            if enable_transport:
                config.write("    spreadingfactor = 8\n" +
                             "    codingrate = 5\n")
            else:
                config.write(f"    spreadingfactor = {spreading_factor}\n" +
                             f"    codingrate = {coding_rate}\n")
            config.close()
        finally:
            self.descriptionText.appendPlainText("File writing finished\n")
            return True

    def load_profiles(self, list):

        saves = open("../profiles.txt", "r")
        profiles = saves.readlines()
        for x in profiles:
            image = x.split(", ")
            image[len(image) - 1] = image[len(image) - 1].rstrip()

            new_profile = Profile(
                image[1], image[2], image[3], image[4], image[5], image[6])
            if image[1] == 'True':
                image[1] = True
            else:
                image[1] = False

            list.update({image[0]: new_profile})

        saves.close()

    def save_profile(self):

        profile_name = self.txCombo_2.text()

        if profile_name == '':
            profile_name = 'Unnamed Profile'

        enable_transport = self.jumpCheck.isChecked()

        frequency = self.freqCombo.currentText()
        spreading_factor = 0
        coding_rate = 0
        bandwidth = 0
        transmit_power = 0
        try:

            if not enable_transport:
                spreading_factor = int(self.spreadCombo.currentText())
                coding_rate = int(self.codingCombo.currentText())

            bandwidth = int(self.bandCombo.text())
            transmit_power = int(self.txCombo.text())

        except:
            self.descriptionText.appendPlainText(
                "Incorrect bandwidth or transmit power field format.\n")

        saves = open("../profiles.txt", "a")

        if profile_name not in list(self.profile_list.keys()):
            saves.write(
                f"{profile_name}, {enable_transport}, {frequency}, {spreading_factor}, {coding_rate}, {bandwidth}, {transmit_power}\n")
        else:
            self.descriptionText.appendPlainText("Needs new profile name\n")
            return
        saves.close()

        self.loadDropDown.addItem(profile_name)
        self.profile_list.update({profile_name: Profile(
            enable_transport, frequency, spreading_factor, coding_rate, bandwidth, transmit_power)})
        self.descriptionText.appendPlainText(f"Profile '{profile_name}' added succesfully.\n")

    def show_load(self, checked):
        if self.w is None:
            self.w = LoadWindow()
            self.w.show()

        else:
            self.w.close()  # Close window.
            self.w = None  # Discard reference.

    def fill_profile(self):
        profile = self.profile_list.get(self.loadDropDown.currentText())

        if profile.is_transport == 'True':
            self.jumpCheck.setChecked(True)
        else:
            self.jumpCheck.setChecked(False)

        if profile.frequency == '433 MHz':
            self.freqCombo.setCurrentIndex(0)
        elif profile.frequency == '868 MHz':
            self.freqCombo.setCurrentIndex(1)
        elif profile.frequency == '915 MHz':
            self.freqCombo.setCurrentIndex(2)
        elif profile.frequency == '2.4 GHz*':
            self.freqCombo.setCurrentIndex(3)

        self.spreadCombo.setCurrentIndex(int(profile.spreading_factor) - 7)
        self.codingCombo.setCurrentIndex(int(profile.coding_rate) - 5)
        self.bandCombo.setText(str(profile.bandwidth))
        self.txCombo.setText(str(profile.transmit_power))

    def delete_profile(self):
        profile_name = self.loadDropDown.currentText()

        if profile_name == 'Select Profile' or profile_name == 'Default':
            self.descriptionText.appendPlainText(
                "Profile cannot be deleted, please select another.\n")
            return

        if profile_name:
            # Remove the profile from the dictionary
            if profile_name in self.profile_list:
                del self.profile_list[profile_name]

            # Rewrite the profiles.txt file without the deleted profile
            with open("../profiles.txt", "w") as saves:
                for name, profile in self.profile_list.items():
                    saves.write(
                        f"{name}, {profile.is_transport}, {profile.frequency}, {profile.spreading_factor}, {profile.coding_rate}, {profile.bandwidth}, {profile.transmit_power}\n")

            # Remove the profile from the drop-down list
            index = self.loadDropDown.findText(profile_name)
            if index != -1:
                self.loadDropDown.removeItem(index)

            # Optionally, clear the fields if the deleted profile was selected
            self.clear_fields()
            self.descriptionText.appendPlainText(
                f"Profile '{profile_name}' deleted successfully.\n")

    def clear_fields(self):
        self.jumpCheck.setChecked(False)
        self.freqCombo.setCurrentIndex(0)
        self.spreadCombo.setCurrentIndex(0)
        self.codingCombo.setCurrentIndex(0)
        self.bandCombo.clear()
        self.txCombo.clear()
        self.txCombo_2.clear()

    def flash_ports(self):
        ports = serial.tools.list_ports.comports()
        self.descriptionText.appendPlainText("Found Ports:\n")
        for port, desc, hwid in sorted(ports):
            self.descriptionText.appendPlainText("{}: {} [{}]\n".format(port, desc, hwid))
        os.system("rnodeconf --autoinstall")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReticulumGUI = QtWidgets.QMainWindow()
    ui = Ui_ReticulumGUI()
    ui.setupUi(ReticulumGUI)
    ReticulumGUI.show()
    sys.exit(app.exec())
