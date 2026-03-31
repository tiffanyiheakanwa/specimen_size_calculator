import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        res = float(entry_size.get()) / float(entry_mag.get())
        label_result.config(text=f"Actual Size: {res:.4f}")
    except:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Specimen Calculator")
root.geometry("300x200")

tk.Label(root, text="Microscope Size:").pack()
entry_size = tk.Entry(root)
entry_size.pack()

tk.Label(root, text="Magnification:").pack()
entry_mag = tk.Entry(root)
entry_mag.pack()

tk.Button(root, text="Calculate", command=calculate).pack()
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()