#!/usr/bin/python3
import tkinter as tk

root = tk.Tk()
root.title('Aparui')
root.minsize(800, 550)
root.geometry("300x300+50+50")
# background =


# def add_page():
#     pass

# def delete_page():
#     pass

#button = tk.Button(
#     texte='Delete',
#     width=25,
#     height=5,
# )

button = tk.Button(
    texte='Delete',
    width=25,
    height=5,
)

button.pack(padx=20, pady=20)

root.mainloop()