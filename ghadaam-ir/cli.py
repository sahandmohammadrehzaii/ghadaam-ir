import tkinter as tk
import webbrowser

def open_link():
    url = "back-end.py"  # آدرس لینک مورد نظر خود را در اینجا قرار دهید
    webbrowser.open(url)

window = tk.Tk()
button = tk.Button(window, text="کلیک کنید", command=open_link)
button.pack()

window.mainloop()