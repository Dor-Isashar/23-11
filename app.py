import sys

from PySide6.QtCore import Qt
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
        self.spinbox = QSpinBox()
        self.spinbox.setRange(0, 10000)
        self.spinbox.setReadOnly(True)
        self.spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.spinbox.setAlignment(Qt.AlignCenter)
        self.spinbox.setStyleSheet("""
            QSpinBox {
                min-width: 150px;
                min-height: 42px;
                padding: 8px 16px;
                border: 2px solid #cbd5e1;
                border-radius: 10px;
                background-color: #ffffff;
                color: #1e293b;
                font-size: 16px;
                font-weight: 600;
            }

            QSpinBox:focus {
                border-color: #4f46e5;
            }
        """)
        
        
        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.button_method)

        layout = QHBoxLayout()
        layout.addWidget(self.spinbox)
        layout.addWidget(self.toggle_button)
        self.setLayout(layout)

    def button_method(self, running: bool) -> None:
        self.toggle_button.setText("Stop" if running else "Start")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
