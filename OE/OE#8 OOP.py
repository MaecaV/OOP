import tkinter as tk

root = tk.Tk()
root.title("Task Management")
root.geometry("300x200")
root.configure(bg="green")

frame = tk.Frame(root)
frame.grid(pady=20)

pangalan = tk.Entry(root)
pangalan.grid(row=0, column=0, padx=20)

counter = 1
def display_text():
    global counter
    print(f"{counter}. {pangalan.get()}")
    counter += 1  
   

button_print = tk.Button(root, text="Submit", command=display_text)
button_print.grid(row=0, column=1, padx=20, pady=20)

root.mainloop()
