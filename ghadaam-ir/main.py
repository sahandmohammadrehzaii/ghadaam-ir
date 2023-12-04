import random
import tkinter as tk
from tkinter import messagebox

class ChatBot:
    def __init__(self, responses):
        self.responses = responses

    def get_response(self, user_input):
        user_input = user_input.lower()
        best_match = ''
        highest_prob = 0

        for key in self.responses:
            prob = self.calculate_similarity(user_input, key)
            if prob > highest_prob:
                highest_prob = prob
                best_match = key

        return self.responses[best_match] if highest_prob >= 0.5 else "Sorry, I don't understand."

    def calculate_similarity(self, input_text, response_key):
        input_words = input_text.split()
        response_words = response_key.split()
        common_words = set(input_words) & set(response_words)
        similarity = len(common_words) / len(response_words)
        return similarity

def send_message():
    user_input = input_entry.get()
    response = bot.get_response(user_input)
    messagebox.showinfo('Bot', response)
    input_entry.delete(0, tk.END)

# Define the responses for the bot
responses = {
    'hello': 'Hello, how can I assist you?',
    'how are you': 'I am doing well, thank you!',
    'weather': 'The weather is sunny today.',
    'goodbye': 'Goodbye! Have a nice day.',
    'default': 'Sorry, I dont have an appropriate response.'
}

# Create an instance of the chat bot
bot = ChatBot(responses)

# Create the main window
window = tk.Tk()
window.title('Chat Bot')
window.geometry('400x300')

# Create the input entry
input_entry = tk.Entry(window, width=40)
input_entry.pack(pady=20)

# Create the send button
send_button = tk.Button(window, text='Send', command=send_message)
send_button.pack()

# Start the main event loop
window.mainloop()