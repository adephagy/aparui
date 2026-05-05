#1source venv/bin/activate

import tkinter as tk
import psutil
import time
import threading

target = ""

def set_target():
    global target
    target = entry.get()
    print("New target:", target)

def monitor():
    while True:
        if target:
            for proc in psutil.process_iter(['name', 'open_files']):
                try:
                    files = proc.info['open_files']
                    if files:
                        for f in files:
                            if f.path == target:
                                print("DETECTED:", proc.info['name'])
                except:
                    pass
        time.sleep(2)

root = tk.Tk()

entry = tk.Entry(root, width=50)
entry.pack()

btn = tk.Button(root, text="Set target", command=set_target)
btn.pack()

threading.Thread(target=monitor, daemon=True).start()

root.mainloop()