import tkinter as tk

fav_anime = ("One Punch Man")
root = tk.Tk()
root.title("OOP")
root.geometry("300x200")
frame = tk.Frame(root)
frame.pack(pady=20)

def display_text():
    print(f"My Favorite anime {fav_anime}")
   

button_print = tk.Button(root, text="Run", command=display_text)
button_print.pack(pady=20)

root.mainloop()
