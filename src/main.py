import sys
import os

import subprocess
from PySide6.QtCore import QTimer

os.environ["GDK_BACKEND"] = "x11"
os.environ["QT_QPA_PLATFORM"] = "xcb"

from PySide6.QtWidgets import QApplication
from ui.overlay import AvatarOverlay

def get_avatar_state(profile):

    states = {
        "performance": (
            "🔥",
            "Avatar State activated!"
        ),
        "balanced": (
            "🌪️",
            "The Avatar is at peace."
        ),
        "power-saver": (
            "😴",
            "Saving energy..."
        )
    }

    return states.get(
        profile,
        ("🌪️", f"Power profile: {profile}")
    )

def main():
    
    app = QApplication(sys.argv)
    app.setApplicationName("The Last Power Profile")
    
    window = AvatarOverlay()
    
    last_profile = None

    def check_power_profile():
        nonlocal last_profile

        try:
            result = subprocess.run(
                ["powerprofilesctl", "get"],
                capture_output=True,
                text=True,
                check=True
            )

            current_profile = result.stdout.strip()

            # Only animate when the profile changes
            if current_profile != last_profile:

                last_profile = current_profile

                character, message = get_avatar_state(
                    current_profile
                )

                window.play_animation(character, message)

                print(f"Power profile changed: {current_profile}")

        except (FileNotFoundError, subprocess.CalledProcessError) as error:
            print(f"Could not read power profile: {error}")
    
    timer = QTimer(app)
    timer.timeout.connect(check_power_profile)
    timer.start(1500)

    # Detect the current profile immediately
    check_power_profile()
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main() 