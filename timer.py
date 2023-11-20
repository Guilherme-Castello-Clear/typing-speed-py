from tkinter import Label


class Timer:
    def __init__(self, root):
        self.root = root
        self.current_time = 0
        self.status = False

        self.label = Label(root, text="Tempo: 0 segundos")
        self.label.pack(pady=10)

    def stop_timer(self):
        if self.status:
            self.status = False
            self.update_timer()
            return self.current_time

    def start_timer(self):
        if not self.status:
            self.status = True
            self.update_timer()

    def update_timer(self):
        if self.status:
            self.current_time += 1
            self.label.config(text=f"Tempo: {self.current_time} segundos")
            self.root.after(1000, self.update_timer)


