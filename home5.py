import sys
from PyQt5.QtWidgets import *

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()