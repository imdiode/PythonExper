from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.blue)
app.setStyleSheet("QPushButton { margin: 10ex; background-color: #4747D2 }")
app.setPalette(palette)
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()