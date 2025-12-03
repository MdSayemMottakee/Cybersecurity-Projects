from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key

def controlMouse():
    mouse = MouseController()
    mouse.position = (500, 200)
    print(f"Mouse moved to position: {mouse.position}")

def controlKeyboard():
    keyboard = KeyboardController()
    keyboard.type("Hello")

if __name__ == "__main__":
    controlMouse()
    controlKeyboard()