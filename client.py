import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTabWidget, QVBoxLayout, QWidget, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import Qt

class EmulatorBackend:
    def __init__(self):
        # Placeholder for actual emulator backend logic.
        pass
    
    def load_rom(self, filepath):
        # Placeholder for ROM loading logic.
        print(f"Loading ROM from {filepath}")
        # In a real emulator, this is where you would parse and load the ROM into memory.
    
    def start_emulation(self):
        # Placeholder for starting emulation.
        print("Starting emulation.")

    def stop_emulation(self):
        # Placeholder for stopping emulation.
        print("Stopping emulation.")

class EMUaiMainWindow(QMainWindow):
    def __init__(self, backend):
        super().__init__()
        self.backend = backend
        self.initUI()

    def initUI(self):
        # Main window settings
        self.setWindowTitle('EMUai - Emulator')
        self.setGeometry(300, 300, 680, 576)  # Set the window size to 680x576
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # Disable maximize button

        # Menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        
        # File menu actions
        load_rom_action = QAction('&Load ROM', self)
        load_rom_action.triggered.connect(self.openFileDialog)
        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)

        file_menu.addAction(load_rom_action)
        file_menu.addAction(exit_action)

        # Status bar
        self.statusBar().showMessage('Ready')

        # Central widget with tabs
        tab_widget = QTabWidget()
        self.setCentralWidget(tab_widget)

        # Add tabs
        tab_widget.addTab(self.createTab('Status'), 'Status')
        tab_widget.addTab(self.createTab('Controls'), 'Controls')
        tab_widget.addTab(self.createTab('Settings'), 'Settings')

    def createTab(self, name):
        """ Helper function to create tabs with a label and a button. """
        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel(name)
        button = QPushButton('Start Emulation', tab)
        button.clicked.connect(self.backend.start_emulation)
        layout.addWidget(label)
        layout.addWidget(button)
        tab.setLayout(layout)
        return tab

    def openFileDialog(self):
        # Open a file dialog to load a ROM file
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
