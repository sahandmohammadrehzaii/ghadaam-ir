import tkinter as tk
import os

def open_language(language):
    if language == "english":
        file_path = os.path.join("Userinformation", "back-end-english.py")
    elif language == "persian":
        file_path = os.path.join("Userinformation", "back-end-persain.py")
    else:
        return

    os.system(f"python {file_path}")

window = tk.Tk()
window.title(' ')
button_frame = tk.Frame(window)
button_frame.pack(pady=20)  # افزودن فاصله بالای فریم

english_button = tk.Button(button_frame, text="English", command=lambda: open_language("english"))
english_button.pack(side=tk.LEFT, padx=25)  # افزودن فاصله بین دکمه و چپ فریم

persian_button = tk.Button(button_frame, text="فارسی", command=lambda: open_language("persian"))
persian_button.pack(side=tk.LEFT, padx=25)  # افزودن فاصله بین دکمه و چپ دکمه قبلی

window.mainloop()