
from PySide6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QApplication, QGraphicsOpacityEffect)

from PySide6.QtCore import (Qt, QPropertyAnimation, QEasingCurve)

from PySide6.QtCore import QSequentialAnimationGroup, QPauseAnimation

class AvatarOverlay(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(
                Qt.WindowType.FramelessWindowHint |
                Qt.WindowType.WindowStaysOnTopHint |
                Qt.WindowType.Tool
            )
        
        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.setFixedSize(520, 380)
        
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2

        self.move(x, y)

        layout = QVBoxLayout(self)

        self.avatar = QLabel("🌪️")
        self.avatar.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.avatar.setStyleSheet("font-size: 300px;")

        self.status = QLabel("The Avatar has awakened!")
        self.status.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        
        self.status.setStyleSheet("""
            color: white;
            font-size: 14px;
            font-weight: bold;
            background-color: rgba(0, 0, 0, 160);
            border-radius: 10px;
            padding: 8px;
        """)

        layout.addWidget(self.avatar)
        layout.addWidget(self.status)

        self.opacity = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(0.0)

        self.animation_group = QSequentialAnimationGroup(self)

        # Fade in
        self.fade_in = QPropertyAnimation(self.opacity, b"opacity")
        self.fade_in.setDuration(700)
        self.fade_in.setStartValue(0.0)
        self.fade_in.setEndValue(1.0)
        self.fade_in.setEasingCurve(QEasingCurve.Type.OutCubic)

        # Stay visible
        self.pause = QPauseAnimation(1800)

        # Fade out
        self.fade_out = QPropertyAnimation(self.opacity, b"opacity")
        self.fade_out.setDuration(700)
        self.fade_out.setStartValue(1.0)
        self.fade_out.setEndValue(0.0)
        self.fade_out.setEasingCurve(QEasingCurve.Type.InCubic)

        # Sequence
        self.animation_group.addAnimation(self.fade_in)
        self.animation_group.addAnimation(self.pause)
        self.animation_group.addAnimation(self.fade_out)

        # Hide when complete
        self.animation_group.finished.connect(self.hide)
        
    
        
    def play_animation(self, character="🌪️", message="The Avatar has awakened!"):

        self.animation_group.stop()

        self.avatar.setText(character)
        self.status.setText(message)

        self.opacity.setOpacity(0.0)

        self.show()
        self.animation_group.start()