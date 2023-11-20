import time

from timer import Timer
from tkinter import Tk, Button, Entry, Text, INSERT, Label, StringVar
import random

root = Tk()
root.title("Type faster!")
root.geometry("650x170")

entry_text = StringVar()
entry_text.set("")

TEXTS = [
    "No horizonte distante, o sol se despede, pintando o ceu com tons de saudade.",
    "Entre suspiros de vento, as folhas dancam, celebrando a poesia silenciosa da natureza.",
    "No silencio da madrugada, as estrelas sussurram segredos cosmicos aos sonhadores."
]

sorted_text = TEXTS[random.randint(0, 2)]

timer = Timer(root)


def verify_text(e):
    timer.start_timer()
    new_text = entry.get()
    if new_text == sorted_text and timer.status:
        finish_text = Label(root, text=f'Você levou {timer.stop_timer()} segundos!')
        finish_text.pack()


text = Label(root, text=sorted_text)
text.pack()

entry = Entry(root)
entry.pack(pady=5)

entry.bind("<KeyRelease>", verify_text)

root.mainloop()
