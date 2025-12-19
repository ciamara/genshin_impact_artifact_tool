from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer, pyqtSignal

class ArtifactOverlay(QWidget):

    data_received = pyqtSignal(float, float)

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
        
        self.label = QLabel("excel CV: 0.0\nscanned CV: 0.0", self)
        self.label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.label.setStyleSheet("color: #FFFFFF; background: rgba(0, 0, 0, 80); padding: 5px; border-radius: 5px;")
        
        self.setGeometry(1308, 215, 200, 60)     # x, y, w, h

    def update_value(self, new_val, excel_val):
        if(excel_val < 0.0):
            self.label.setText(f"excel CV: no character\nscanned CV: {new_val}")
        elif(excel_val == 'NaN'):
            self.label.setText(f"excel CV: no artifact\nscanned CV: {new_val}")
        else:
            self.label.setText(f"excel CV: {excel_val}\nscanned CV: {new_val}")
        self.show()
        self.display_timer.start(6000)
