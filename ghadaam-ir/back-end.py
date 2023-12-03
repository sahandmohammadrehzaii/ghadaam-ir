import csv
import tkinter as tk
from tkinter import messagebox

# -*- coding: utf-8 -*-

def register(username, password):
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    messagebox.showinfo('Registration', 'Registration successful!')

def login(username, password):
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                messagebox.showinfo('Login', 'Login successful!')
                return
        messagebox.showerror('Login', 'Invalid username or password.')

def handle_choice(choice):
    if choice == '1':
        register_window = tk.Toplevel(main_window)
        register_window.title('Register')
        register_window.geometry('300x150')

        username_label = tk.Label(register_window, text='\nUsername:')
        username_label.pack()

        username_entry = tk.Entry(register_window)
        username_entry.pack()

        password_label = tk.Label(register_window, text='\nPassword:')
        password_label.pack()

        password_entry = tk.Entry(register_window, show='*')
        password_entry.pack()

        register_button = tk.Button(register_window, text='Register', command=lambda: register(username_entry.get(), password_entry.get()))
        register_button.pack()

    elif choice == '2':
        login_window = tk.Toplevel(main_window)
        login_window.title('Login')
        login_window.geometry('300x150')

        username_label = tk.Label(login_window, text='\nUsername:')
        username_label.pack()

        username_entry = tk.Entry(login_window)
        username_entry.pack()

        password_label = tk.Label(login_window, text='\nPassword:')
        password_label.pack()

        password_entry = tk.Entry(login_window, show='*')
        password_entry.pack()

        login_button = tk.Button(login_window, text='Login', command=lambda: login(username_entry.get(), password_entry.get()))
        login_button.pack()

def main():
    global main_window
    main_window = tk.Tk()
    main_window.title('The registration or login section to use artificial intelligence is coming')
    main_window.geometry('550x200')

    choice_label = tk.Label(main_window, text='Choose an option:')
    choice_label.pack()

    register_button = tk.Button(main_window, text='Register', command=lambda: handle_choice('1'))
    register_button.pack()

    login_button = tk.Button(main_window, text='Login', command=lambda: handle_choice('2'))
    login_button.pack()
    

    exit_button = tk.Button(main_window, text='Exit', command=main_window.quit)
    exit_button.pack()

    main_window.mainloop()

if __name__ == '__main__':
    main()
