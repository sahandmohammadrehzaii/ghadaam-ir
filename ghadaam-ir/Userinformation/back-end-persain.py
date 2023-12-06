import csv
import tkinter as tk
from tkinter import messagebox
import os

# -*- coding: utf-8 -*-

def register(username  ,   password):
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    messagebox.showinfo('ثبت اطلاعات جدید', 'ثبت نام موفقیت آمیز بود')
    main_window.destroy()  # بستن پنجره اصلی بعد از ثبت نام
    run_main_script()

def login(username, password):
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                messagebox.showinfo('اطلاعات حساب درست است', 'ورود شما به حساب کاربری تان موفقیت آمیز بود')
                main_window.destroy()  # بستن پنجره اصلی بعد از ورود
                run_main_script()
                return
        messagebox.showerror('اطلاعات حساب  نادرست است', 'نام کاربری یا رمز عبور نامعتبر است')

def handle_choice(choice):
    if choice == '1':
        register_window = tk.Toplevel(main_window)
        register_window.title('فرم ثبت نام')
        register_window.geometry('300x150')

        username_label = tk.Label(register_window, text='\nنام کاربری:')
        username_label.pack()

        username_entry = tk.Entry(register_window)
        username_entry.pack()

        password_label = tk.Label(register_window, text='\nرمز عبور:')
        password_label.pack()

        password_entry = tk.Entry(register_window, show='*')
        password_entry.pack()

        register_button = tk.Button(register_window, text='ثبت نام', command=lambda: register(username_entry.get(), password_entry.get()))
        register_button.pack()

    elif choice == '2':
        login_window = tk.Toplevel(main_window)
        login_window.title('فرم ورود')
        login_window.geometry('300x150')

        username_label = tk.Label(login_window, text='\nنام کاربری:')
        username_label.pack()

        username_entry = tk.Entry(login_window)
        username_entry.pack()

        password_label = tk.Label(login_window, text='\nرمز عبور:')
        password_label.pack()

        password_entry = tk.Entry(login_window, show='*')
        password_entry.pack()

        login_button = tk.Button(login_window, text='ورود', command=lambda: login(username_entry.get(), password_entry.get()))
        login_button.pack()

def run_main_script():
    # تغییر مسیر کاری به پوشه englishbot
    script_dir = os.path.dirname(os.path.abspath(__file__))
    englishbot_dir = os.path.join(script_dir, 'englishbot')
    os.chdir(englishbot_dir)

    # تغییر مسیر کاری به پوشه بیرون
    parent_dir = os.path.abspath(os.path.join(englishbot_dir, os.pardir))
    os.chdir(parent_dir)

    # اجرای فایل main.py از داخل پوشه englishbot
    os.system('python persianbot/main.py')

def main():
    global main_window
    main_window = tk.Tk()
    main_window.title('بخش ثبت نام یا ورود برای استفاده از هوش مصنوعی قادم')
    main_window.geometry('550x250')

    choice_label = tk.Label(main_window, text='یکی از مراحل را برای استفاده از هوش مصتوعی انتخاب کنید')
    choice_label.pack()

    space_label = tk.Label(main_window, text='\n')  # فاصله بین دکمه‌ها
    space_label.pack()

    register_button = tk.Button(main_window, text='ثبت نام', command=lambda: handle_choice('1'))
    register_button.pack()

    space_label = tk.Label(main_window, text='\n')  # فاصله بین دکمه‌ها
    space_label.pack()

    login_button = tk.Button(main_window, text='ورود', command=lambda: handle_choice('2'))
    login_button.pack()

    space_label = tk.Label(main_window, text='\n')  # فاصله بین دکمه‌ها
    space_label.pack()

    exit_button = tk.Button(main_window, text='خروج', command=main_window.quit)
    exit_button.pack()

    main_window.mainloop()

if __name__ == '__main__':
    main()

is_registered = True  # متغیر برای بررسی وضعیت ثبت نام/ورود

