import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMovie


class CustomWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.offset = None
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(300, 300, 500, 300)
        self.setStyleSheet("background-color: black; color: white;")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        title_bar = self.create_title_bar()

        self.gif_label = QLabel()
        self.gif_label.setAlignment(Qt.AlignCenter)
        gif_path = os.path.join(os.path.dirname(__file__), "jarvis.gif")
        self.movie = QMovie(gif_path)
        self.gif_label.setMovie(self.movie)
        self.movie.start()  # бесконечная анимация

        self.content = QLabel("🔊 Jarvis ждёт команды...")
        self.content.setAlignment(Qt.AlignCenter)
        self.content.setStyleSheet("font-size: 16px; padding: 15px; color: #ccc;")

        main_layout.addLayout(title_bar)
        main_layout.addWidget(self.gif_label)
        main_layout.addWidget(self.content)
        self.setLayout(main_layout)

    def create_title_bar(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 5, 10, 5)

        title = QLabel("J.A.R.V.I.S")
        title.setStyleSheet("font-weight: bold; font-size: 16px; color: white;")

        btn_minimize = QPushButton("–")
        btn_close = QPushButton("×")

        btn_minimize.clicked.connect(self.showMinimized)
        btn_close.clicked.connect(self.close)

        btn_style = """
            QPushButton {
                background-color: transparent;
                border: none;
                color: white;
                font-size: 16px;
                width: 30px;
                height: 30px;
            }
            QPushButton:hover {
                background-color: #444;
                border-radius: 5px;
            }
        """
        btn_minimize.setStyleSheet(btn_style)
        btn_close.setStyleSheet(btn_style)

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(btn_minimize)
        layout.addWidget(btn_close)

        return layout

    def update_status(self, status: str):
        self.content.setText(status)

    def start_speaking_animation(self):
        self.update_status("🗣️ Jarvis говорит...")

    def stop_speaking_animation(self):
        self.update_status("🔊 Jarvis ждёт команды...")

    def set_listening_status(self):
        self.update_status("🟣 Jarvis слушает...")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.offset = None
