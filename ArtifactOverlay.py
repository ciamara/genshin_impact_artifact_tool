from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer, pyqtSignal

class ArtifactOverlay(QWidget):

    data_received = pyqtSignal(float)

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)

        self.data_received.connect(self.update_value)

        self.display_timer = QTimer(self)
        self.display_timer.setSingleShot(True)
        self.display_timer.timeout.connect(self.hide)
        
        self.label = QLabel("CV: 0.0", self)
        self.label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.label.setStyleSheet("color: #FFFFFF; background: rgba(0, 0, 0, 80); padding: 5px; border-radius: 5px;")
        
        self.setGeometry(1350, 220, 200, 60)     # x, y, w, h

    def update_value(self, new_val):
        self.label.setText(f"CV: {new_val}")
        self.show()
        self.display_timer.start(6000)
