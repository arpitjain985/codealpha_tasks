def simple_chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if not user_input:
            print("Chatbot: Please say something!")
            continue
            
        # check condition 
        if any(word in user_input for word in ["bye", "goodbye", "exit", "quit"]):
            print("Chatbot: Goodbye! Have a nice day!")
            break
            
        
        elif any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
            print("Chatbot: Hi there!")
            
        elif "how are you" in user_input:
            print("Chatbot: I'm doing well, thank you for asking!")
            
        elif "your name" in user_input:
            print("Chatbot: I'm just a simple chatbot!")
            
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            print(f"Chatbot: The current time is {current_time}")
            
        elif "date" in user_input:
            from datetime import datetime
            current_date = datetime.now().strftime("%B %d, %Y")
            print(f"Chatbot: Today's date is {current_date}")
            
        elif "help" in user_input:
            print("Chatbot: I can respond to greetings, tell you the time/date, or chat about simple things!")
            
        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking about the time or date!")

if __name__ == "__main__":
    simple_chatbot()
