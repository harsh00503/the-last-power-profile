import sys
import os

os.environ["GDK_BACKEND"] = "x11"
os.environ["QT_QPA_PLATFORM"] = "xcb"

from PySide6.QtWidgets import QApplication
from ui.overlay import AvatarOverlay

def main():
    
    app = QApplication(sys.argv)
    app.setApplicationName("The Last Power Profile")
    
    window = AvatarOverlay()
    window.play_animation()
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main() 