import tkinter as tk
from tkinter import messagebox
import pyautogui
import cv2  # pip install opencv-python
import numpy as np
import threading


class ScreenRecorderApp:
    def __init__(self, master):
        self.master = master
        master.title("Запись экрана")
        master.geometry("340x120")
        self.recording = False
        self.record_button = tk.Button(master, text="Начать запись", command=self.toggle_recording, height=2, width=20)
        self.record_button.pack(pady=20)

    def toggle_recording(self):
        if not self.recording:
            self.recording = True
            threading.Thread(target=self._record_screen).start()
            self.record_button.config(text="Закончить запись")
        else:
            self.recording = False
            self.record_button.config(text="Начать запись")

    def _record_screen(self):
        SCREEN_SIZE = pyautogui.size()
        FPS = 24.0
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter("output.avi", fourcc, FPS, (SCREEN_SIZE))
        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
        out.release()
        messagebox.showinfo("Запись окончена.", "Запись сохранена под именем 'output.avi'")


if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorderApp(root)
    root.mainloop()