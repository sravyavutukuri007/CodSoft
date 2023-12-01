def simple_chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching
    
    # Define some predefined rules and responses
    greetings = ['hello', 'hi', 'hey', 'greetings']
    farewells = ['bye', 'goodbye', 'see you', 'take care']
    about_bot = ['what can you do', 'who are you', 'what are you']

    # Check user input against predefined rules and provide responses
    if user_input in greetings:
        return "Hello! How can I assist you today?"
    elif user_input in farewells:
        return "Goodbye! Have a great day!"
    elif any(word in user_input for word in about_bot):
        return "I am a simple chatbot programmed to assist you. Feel free to ask me anything!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Example usage
while True:
    user_query = input("You: ")
    if user_query.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    else:
        bot_response = simple_chatbot(user_query)
        print("Chatbot:", bot_response)
