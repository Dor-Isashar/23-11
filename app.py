import sys

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
