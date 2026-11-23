import sys
from PySide6.QtCore import Qt ,QTimer
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QSpinBox,
    QWidget,
)

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Spinbox Control")
        self.setGeometry(100, 100, 400, 400)

        self.counter = 0
                
        self.spinbox = QSpinBox()
        self.spinbox.setRange(0, 10000)
        self.spinbox.setReadOnly(True)
        self.spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.spinbox.setAlignment(Qt.AlignCenter)
        self.spinbox.setStyleSheet("QSpinBox { font-size: 24px; }")
                           
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_method)
        
        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.button_method)

        layout = QHBoxLayout()
        layout.addWidget(self.spinbox)
        layout.addWidget(self.toggle_button)
        self.setLayout(layout)

    def button_method(self, running: bool) -> None:
        self.toggle_button.setText("Stop" if running else "Start")
        if running:
            self.timer.start(10)
        else:
            self.timer.stop()
    
    def timer_method(self) -> None:        
        self.counter += 1
        self.spinbox.setValue(self.counter)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
