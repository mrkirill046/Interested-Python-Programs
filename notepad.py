import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog


class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.init_menu()

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Простой блокнот')
        self.show()

    def init_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('Файл')

        new_action = QAction('Новый', self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction('Открыть', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction('Сохранить', self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        exit_action = QAction('Выход', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def new_file(self):
        self.text_edit.clear()

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '', 'Текстовые файлы (*.txt)')
        if file_path:
            with open(file_path, 'r') as file:
                self.text_edit.setText(file.read())

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '', 'Текстовые файлы (*.txt)')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_edit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())
