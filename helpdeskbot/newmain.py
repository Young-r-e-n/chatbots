import tkinter as tk
import json
import re
import random_responses


# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()


def send_message():
    user_input = user_input_entry.get()
    bot_response = get_response(user_input)
    conversation_text.configure(state=tk.NORMAL)
    conversation_text.insert(tk.END, "You: " + user_input + "\n")
    conversation_text.insert(tk.END, "Bot: " + bot_response + "\n")
    conversation_text.insert(tk.END, "\n")
    conversation_text.configure(state=tk.DISABLED)
    user_input_entry.delete(0, tk.END)


# Create the GUI window
window = tk.Tk()
window.title("Helpdesk Chatbot")
window.geometry("600x500")
window.configure(bg="#f0f0f0")

# Create the conversation text widget
conversation_text = tk.Text(window, state=tk.DISABLED, bg="#ffffff", padx=10, pady=10)
conversation_text.pack(fill=tk.BOTH, expand=True)

# Create the user input entry widget
user_input_entry = tk.Entry(window, bg="#ffffff", relief=tk.SOLID, bd=1, font=("Arial", 12))
user_input_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create the send button
send_button = tk.Button(window, text="Send", command=send_message, relief=tk.RAISED, bd=1, font=("Arial", 12))
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()

#0748653542