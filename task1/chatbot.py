def chatbot():
    print("Chatbot: Hi! I am your simple chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thank you!")
        
        elif user_input == "thanks":
            print("Chatbot: You're welcome!")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        
        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
