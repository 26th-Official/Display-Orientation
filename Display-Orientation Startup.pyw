import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import rotatescreen
    import keyboard
except ImportError:
    install("rotate-screen")
    import rotatescreen
    install("keyboard")
    import keyboard



screen = rotatescreen.get_primary_display()

keyboard.add_hotkey('ctrl+alt+up', screen.set_landscape_flipped, suppress=True)
keyboard.add_hotkey('ctrl+alt+right', screen.set_portrait, suppress=True)
keyboard.add_hotkey('ctrl+alt+down', screen.set_landscape, suppress=True)
keyboard.add_hotkey('ctrl+alt+left', screen.set_portrait_flipped, suppress=True)

keyboard.wait('ctrl+alt+esc')
