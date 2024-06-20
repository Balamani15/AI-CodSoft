def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "nice to meet you!" in user_input:
        return "The pleasure all mine!"
    elif "how are you?" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "weather" in user_input:
        return "I'm not able to check the weather right now. Please check a weather app or website."
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif "day" in user_input:
        from datetime import datetime
        return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have any other questions, feel free to ask."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "I can assist with questions about the time, day, weather, and general greetings. How can I help you?"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    print("Welcome to the Rule-Based Chatbot!")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()