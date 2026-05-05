#!/usr/bin/env python3
import subprocess
import time

print("Détection active... (Ctrl+C pour arrêter)\n")
 
dernier_titre = ""

print("Détection active... (Ctrl+C pour arrêter)\n")

dernier_titre = ""
while True:
    try:
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            capture_output=True, text=True
        )
        titre = result.stdout.strip()
        if titre and titre != dernier_titre:
            dernier_titre = titre
            print(f"→ {titre}")
    except:
        pass
    time.sleep(0.5)
