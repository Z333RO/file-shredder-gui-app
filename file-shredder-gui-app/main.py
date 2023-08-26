# pip install pyqt6
# Note: On Windows need to have the sys module - otherwise the gui will flash and close down immediately for some reason
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select files')
    # print(filenames)
    message.setText('\n'.join(filenames))

def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText('File Destruction Complete.')


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('File Shredder')
layout = QVBoxLayout()

description = QLabel('Select the file you want to destroy. Files will be <font color="red">permanently deleted</font>.')
layout.addWidget(description)

open_btn = QPushButton('Open Files')
open_btn.setToolTip('Open Files')
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton('Shred Files')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()

sys.exit(app.exec())

# For troubleshooting on Windows, review this https://stackoverflow.com/questions/35051186/gui-window-in-python-pyqt-flashing-and-closing-down-immediately
