'''TASK 4: Basic Chatbot 
Goal: Build a simple rule-based chatbot. 
Scope: 
● Input from user like: "hello", "how are you", "bye". 
● Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!". 
Key Concepts Used: if-elif, functions, loops, input/output'''



import tkinter as tk
from tkinter import scrolledtext

# Chatbot logic
def get_response(user_input):
    user_input = user_input.lower()
    if user_input == "hello":
        return "Hi!"
    elif user_input == "hi":
        return "Hello!"
    elif user_input == "hey":
        return "Hey there!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I'm a chatbot created by shifa."
    elif user_input == "what are you doing":
        return "I'm here to chat with you!"
    elif user_input == "who are you":
        return "I am AI chatbot by whom you can talk anytime."
    elif user_input == "what can you do":
        return "I can chat with you and answer simple questions."
    elif user_input == "Can you help me?":
        return "Of course! I'm here to help you."
    elif user_input == "what is your purpose":
        return "My purpose is to assist and chat with you."
    elif user_input == "In which language you are made":
        return "I am made in Python."
    elif user_input == "Can you suggest a programming language":
        return "Sure! Python is a great choice for beginners."
    elif user_input == "what is your favorite color":
        return "I don't have personal preferences, but I like all colors!"
    elif user_input == "what is the best career to choose":
        return "The best career is one that aligns with your passions and skills."
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."


# Function to send message
def send_message():
    user_text = entry_field.get().strip()
    if user_text == "":
        return

    # Display user message (right-aligned)
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"\n {' '*60} {user_text}:👱🏻")

    # Get and display bot response (left-aligned)
    bot_response = get_response(user_text)
    chat_area.insert(tk.END, f"\n🤖: {bot_response}")
    chat_area.config(state=tk.DISABLED)

    entry_field.delete(0, tk.END)


# GUI setup
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("420x550")
root.resizable(False, False)
root.configure(bg="#EAE9E9")

# Title label
title_label = tk.Label(root, text="Basic AI Chatbot", font=("Times New Roman", 20, "bold"), bg="#FFFCFC", fg="#333")
title_label.pack(pady=10)

# Chat display area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Times New Roman", 12))
chat_area.pack(padx=10, pady=10)
chat_area.config(state=tk.DISABLED)

# Bottom input frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

entry_field = tk.Entry(bottom_frame, width=30, font=("Arial", 12))
entry_field.grid(row=0, column=0, padx=10)

send_button = tk.Button(bottom_frame, text="⬆", font=("Arial", 12), command=send_message)
send_button.grid(row=0, column=1)

# Run the GUI loop
root.mainloop()
