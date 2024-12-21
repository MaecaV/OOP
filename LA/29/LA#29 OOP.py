import tkinter as tk

your_name = "MAECA_VINSON"
your_section = "BSIT-2A" 
root = tk.Tk()
root.title("OOP")
root.geometry("300x200")
root.configure(bg="white")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text=f"OOP {your_name} {your_section}")
label.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
