import tkinter as tk
from tkinter import ttk
from database import databasecli

class ChatBot:
    def __init__(self, databasecli):
        self.databasecli = databasecli
        self.default_font = ('Arial', 12)
        self.custom_font = ('Your_Custom_Font_Name', 12)  # جایگزین "Your_Custom_Font_Name" با نام فونت مورد نظر خود شوید

    def get_response(self, user_input):
        user_input = user_input.lower()
        best_match = ''
        highest_prob = 0

        for key in self.databasecli:
            prob = self.calculate_similarity(user_input, key)
            if prob > highest_prob:
                highest_prob = prob
                best_match = key

        return self.databasecli[best_match] if highest_prob >= 0.5 else "I'm sorry, I can't answer the request you asked me"

    def calculate_similarity(self, input_text, response_key):
        input_words = input_text.split()
        response_words = response_key.split()
        common_words = set(input_words) & set(response_words)
        similarity = len(common_words) / len(response_words)
        return similarity

def send_message(event=None):
    user_input = input_entry.get()
    response = bot.get_response(user_input)

    message_text.config(state=tk.NORMAL)
    message_text.insert(tk.END, "You: " + user_input + "\n")
    message_text.insert(tk.END, "\nghadaam-ir: " + response + "\n\n")
    message_text.config(state=tk.DISABLED)
    input_entry.delete(0, tk.END)



bot = ChatBot(databasecli)

window = tk.Tk()
window.title('Chat Bot - ghadaam-ir')
window.geometry('400x300')

style = ttk.Style()
style.configure('TLabel', font=bot.custom_font)
style.configure('TEntry', font=bot.custom_font)
style.configure('TButton', font=bot.custom_font, foreground='black', background='white', padding=10)
style.map('TButton', foreground=[('active', '!disabled', 'green')])

message_text = tk.Text(window, width=40, height=10, font=bot.custom_font)
message_text.pack(pady=20)
message_text.config(state=tk.DISABLED)

input_frame = ttk.Frame(window)
input_frame.pack()

input_entry = ttk.Entry(input_frame, width=30, font=bot.custom_font)
input_entry.pack(side=tk.LEFT)
input_entry.bind("<Return>", send_message)
input_entry.focus()

send_button = ttk.Button(input_frame, text='Send', command=send_message, style='TButton')
send_button.pack(side=tk.LEFT, padx=5)




window.mainloop()