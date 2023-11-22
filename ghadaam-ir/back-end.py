import tkinter as tk

def register():
    # دریافت اطلاعات از ورودی‌ها
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    
    # بررسی تکمیل اطلاعات
    if not username or not password or not email:
        message_window = tk.Toplevel(window)
        message_window.title("مشکل ثبت نام")
        message_label = tk.Label(message_window, text=". لطفا تمامی اطلاعات لازم و خواسته شده را وارد بکنید")
        message_label.pack(padx=40, pady=20)
        return
    
    # نمایش اطلاعات در کنسول
    print("نام کاربری:", username)
    print("رمز عبور:", password)
    print("ایمیل:", email)
    
    # ذخیره اطلاعات در فایل
    with open("datebass.api", "a") as file:
        file.write(f"username: {username}\n")
        file.write("\n")
        file.write("|-----------------|\n")
        file.write("\n")
        file.write(f"password: {password}\n")
        file.write("\n")
        file.write("|-----------------|\n")
        file.write("\n")
        file.write(f"email: {email}\n")
        file.write("\n")
        file.write("|-----------------|\n")
        file.write("\n")
    
    # نمایش پیام با استفاده از ویجت Toplevel
    message_window = tk.Toplevel(window)
    message_window.title("ثبت نام")
    message_label = tk.Label(message_window, text="ثبت نام با موفقیت انجام شد.")
    message_label.pack(padx=20, pady=10)

# ایجاد پنجره اصلی
window = tk.Tk()
window.title("فرم ثبت نام - ghadaam-IR")
window.geometry("400x400")

# تنظیم رنگ پس زمینه
window.configure(bg="blue")

# عنوان فرم
label_title = tk.Label(window, text="فرم ثبت نام", font=("Arial", 20), bg="blue", fg="white")
label_title.pack(pady=20)

# فیلد نام کاربری
label_username = tk.Label(window, text="نام کاربری:", bg="blue", fg="white")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

# فیلد رمز عبور
label_password = tk.Label(window, text="رمز عبور:", bg="blue", fg="white")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# فیلد ایمیل
label_email = tk.Label(window, text="ایمیل:", bg="blue", fg="white")
label_email.pack()
entry_email = tk.Entry(window)
entry_email.pack()

# دکمه ثبت نام
button_register = tk.Button(window, text="ثبت نام", command=register)
button_register.pack(pady=20)

# شروع حلقه رویدادها
window.mainloop()