import tkinter as tk
from tkinter import ttk
import datetime

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Diary")
        self.root.geometry("800x600")

        self.date_label = ttk.Label(root, text="Date:")
        self.date_label.grid(row=0, column=0, padx=10, pady=10)

        self.date_entry = ttk.Entry(root)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)

        self.entry_label = ttk.Label(root, text="Entry:")
        self.entry_label.grid(row=1, column=0, padx=10, pady=10)

        self.entry_text = tk.Text(root, height=20, width=60)
        self.entry_text.grid(row=1, column=1, padx=10, pady=10)

        self.save_button = ttk.Button(root, text="Save", command=self.save_entry)
        self.save_button.grid(row=2, column=1, padx=10, pady=10)

        self.load_button = ttk.Button(root, text="Load", command=self.load_entry)
        self.load_button.grid(row=2, column=0, padx=10, pady=10)

        self.clear_button = ttk.Button(root, text="Clear", command=self.clear_entry)
        self.clear_button.grid(row=3, column=0, padx=10, pady=10)

        self.date_entry.insert(0, datetime.date.today().strftime("%Y-%m-%d"))

    def save_entry(self):
        date = self.date_entry.get()
        entry = self.entry_text.get("1.0", tk.END)

        if date and entry:
            with open("diary.txt", "a") as f:
                f.write(f"{date}\n{entry}\n\n")
            self.entry_text.delete("1.0", tk.END)
            self.date_entry.delete(0, tk.END)

    def load_entry(self):
        date = self.date_entry.get()

        if date:
            with open("diary.txt", "r") as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.strip() == date:
                        self.entry_text.delete("1.0", tk.END)
                        self.entry_text.insert(tk.END, "".join(lines[i+1:]))
                        break

    def clear_entry(self):
        self.entry_text.delete("1.0", tk.END)
        self.date_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()