import tkinter as tk
import random as rand

root = tk.Tk()
root.title("Test")
root.geometry("1200x800")

count=0

def on_button_click():
    global count
    count += 1
    label.config(text=f"You clicked me {count} times!")

#testing a button
button = tk.Button(root,text="Click me", command=on_button_click)
button.pack()

label = tk.Label(root,text="you clicked me!")
label.pack()

root.mainloop()