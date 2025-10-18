print("Welcome to Simple Chatbot!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi!")
    elif user_input == "hi":
        print("Bot: hii!")
    elif user_input == "how are you":
        print("Bot: I'm fine,how are you,thanks!")
    elif user_input == "what is your name":
        print("Bot: I'm a chat boot!")
    elif user_input == "I am fine":
        print("Bot: Good,thanks!")
    elif user_input == "i am fine":
        print("Bot: Good,thanks!")
    elif user_input == "hii":
        print("Bot: I am your assistant,what do you need help with?")
    elif user_input == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
