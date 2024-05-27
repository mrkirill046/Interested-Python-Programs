import sys
import pyshorteners
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QWidget, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сокращение ссылок")
        self.setGeometry(100, 100, 500, 150)
        self.shortener = pyshorteners.Shortener()

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        self.label_long_url = QLabel("Введите длинную ссылку:")
        layout.addWidget(self.label_long_url, 0, 0)

        self.entry_long_url = QLineEdit()
        self.entry_long_url.setFixedWidth(300)
        layout.addWidget(self.entry_long_url, 0, 1)

        self.button_shorten = QPushButton("Сократить")
        self.button_shorten.clicked.connect(self.shorten_link)
        layout.addWidget(self.button_shorten, 0, 2)

        self.label_short_url = QLabel("Сокращенная ссылка:")
        layout.addWidget(self.label_short_url, 1, 0)

        self.entry_short_url = QLineEdit()
        self.entry_short_url.setFixedWidth(300)
        self.entry_short_url.setReadOnly(True)
        layout.addWidget(self.entry_short_url, 1, 1)

        self.button_copy = QPushButton("Copy")
        self.button_copy.clicked.connect(self.copy_to_clipboard)
        layout.addWidget(self.button_copy, 1, 2)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def shorten_link(self):
        long_url = self.entry_long_url.text()
        if long_url:
            try:
                short_url = self.shortener.tinyurl.short(long_url)
                self.entry_short_url.setText(short_url)
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сократить ссылку: {e}")
        else:
            QMessageBox.warning(self, "Предупреждение", "Введите длинную ссылку!")

    def copy_to_clipboard(self):
        short_url = self.entry_short_url.text()
        if short_url:
            QApplication.clipboard().setText(short_url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
