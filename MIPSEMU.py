import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QTabWidget, QVBoxLayout,
                             QWidget, QLabel, QPushButton, QFileDialog, QHBoxLayout, QCheckBox,
                             QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtCore import Qt

class EmulatorBackend:
    def __init__(self):
        self.rom_loaded = False

    def load_rom(self, filepath):
        print(f"Loading ROM from {filepath}")
        self.rom_loaded = True

    def start_emulation(self):
        if not self.rom_loaded:
            print("No ROM loaded. Can't start emulation.")
            return
        print("Starting emulation.")

    def stop_emulation(self):
        if not self.rom_loaded:
            print("No ROM loaded. Nothing to stop.")
            return
        print("Stopping emulation.")

class EMUaiMainWindow(QMainWindow):
    def __init__(self, backend):
        super().__init__()
        self.backend = backend
        self.initUI()

    def initUI(self):
        self.setWindowTitle('EMUai - Emulator')
        self.setGeometry(300, 300, 800, 600)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        
        load_rom_action = QAction('&Load ROM', self)
        load_rom_action.triggered.connect(self.openFileDialog)
        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)

        file_menu.addAction(load_rom_action)
        file_menu.addAction(exit_action)

        self.statusBar().showMessage('Ready')

        tab_widget = QTabWidget()
        self.setCentralWidget(tab_widget)

        tab_widget.addTab(self.createStatusTab(), 'Status')
        tab_widget.addTab(self.createControlsTab(), 'Controls')
        tab_widget.addTab(self.createSettingsTab(), 'Settings')

    def createStatusTab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        rom_status_label = QLabel("ROM Status: Not Loaded")
        start_button = QPushButton('Start Emulation', tab)
        stop_button = QPushButton('Stop Emulation', tab)
        
        start_button.clicked.connect(self.backend.start_emulation)
        stop_button.clicked.connect(self.backend.stop_emulation)
        
        layout.addWidget(rom_status_label)
        layout.addWidget(start_button)
        layout.addWidget(stop_button)
        tab.setLayout(layout)

        return tab

    def createControlsTab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        controls_info_label = QLabel("Configure your controls here")
        layout.addWidget(controls_info_label)
        # Add more controls configuration widgets here
        tab.setLayout(layout)

        return tab

    def createSettingsTab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        settings_info_label = QLabel("Adjust emulator settings here")
        layout.addWidget(settings_info_label)
        # Add more settings widgets here
        tab.setLayout(layout)

        return tab

    def openFileDialog(self):
        options = QFileDialog.Options()
        filepath, _ = QFileDialog.getOpenFileName(self, "Load ROM", "",
                                                  "N64 ROM Files (*.z64 *.n64);;All Files (*)", options=options)
        if filepath:
            self.backend.load_rom(filepath)
            self.statusBar().showMessage(f'Loaded ROM: {filepath}')

def main():
    app = QApplication(sys.argv)
    backend = EmulatorBackend()
    main_window = EMUaiMainWindow(backend)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
