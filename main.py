import tkinter as tk
from tkinter import scrolledtext

class FriendChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Friend 1.0")

        self.chat_display = scrolledtext.ScrolledText(
            master, wrap=tk.WORD, width=40, height=10,
            font=("Arial", 12), bg="#f0f0f0", fg="#333"
        )
        # Set the background color for the chat display
        self.chat_display.config(bg="#e6e6e6")
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.entry_label = tk.Label(
            master, text="Votre message:", font=("Arial", 12), bg="#e6e6e6", fg="#333"
        )
        self.entry_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_var = tk.StringVar()
        self.entry_field = tk.Entry(
            master, textvariable=self.entry_var, width=30, font=("Arial", 12), bg="white", fg="#333"
        )
        self.entry_field.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        # Bind the 'Return' key (Enter key) to the send_message function
        self.entry_field.bind("<Return>", self.send_message)

        self.send_button = tk.Button(
            master, text="Envoyer", command=self.send_message,
            font=("Arial", 12), bg="#4caf50", fg="white", relief=tk.FLAT
        )
        self.send_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Set grid weights to make the chat display expand with the window
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

    def send_message(self, event=None):
        user_message = self.entry_var.get()
        response_message = generate_response(user_message)
        self.chat_display.insert(tk.END, f"You: {user_message}\n")
        self.chat_display.insert(tk.END, f"Friend 1.0: {response_message}\n")
        self.chat_display.see(tk.END)
        self.entry_var.set("")

def generate_response(user_message):
    # Your response generation logic here
    return f"'{user_message}' a été reçu!"

def main():
    root = tk.Tk()
    app = FriendChatApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
