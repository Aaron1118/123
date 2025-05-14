import tkinter as tk
from tkinter import messagebox
import subprocess

def start_task():
    subprocess.Popen(["python", "main.py"])
    messagebox.showinfo("提示", "挂机任务已启动")

root = tk.Tk()
root.title("挂机助手")
root.geometry("300x150")

btn_start = tk.Button(root, text="开始挂机", command=start_task)
btn_start.pack(pady=20)

root.mainloop()
