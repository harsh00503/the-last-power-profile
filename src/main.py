import sys
import os

#import subprocess
#from PySide6.QtCore import QTimer

os.environ["GDK_BACKEND"] = "x11"
os.environ["QT_QPA_PLATFORM"] = "xcb"

from PySide6.QtWidgets import QApplication
from ui.overlay import AvatarOverlay
from services.power_profile import PowerProfileMonitor
from pathlib import Path
from app_paths import resource_path

ASSET_DIR = resource_path("assets", "aang")

def get_avatar_state(profile):

    states = {
    "performance": (
        str(ASSET_DIR / "aang_performance.png"),
        "Avatar State activated!"
    ),
    "balanced": (
        str(ASSET_DIR / "aang_balanced.png"),
        "The Avatar is at peace."
    ),
    "power-saver": (
        str(ASSET_DIR / "aang_power_saver.png"),
        "Saving energy..."
    )
}

    return states.get(
    profile,
    (str(ASSET_DIR / "meditating.png"), f"Power profile: {profile}")
)



def main():
    
    app = QApplication(sys.argv)
    app.setApplicationName("The Last Power Profile")
    
    window = AvatarOverlay()
    
    def handle_profile_changed(profile):

        character, message = get_avatar_state(profile)

        print(f"Power profile changed: {profile}")

        window.play_animation(character, message)


    monitor = PowerProfileMonitor(handle_profile_changed)
    

    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main() 