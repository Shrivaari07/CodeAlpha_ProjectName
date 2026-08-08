def rule_based_chatbot():
    while True:
        a=input("You:").lower()
        if a=="hello":
            print("Me: Hi")
        elif a=="how are you?":
            print("Me: I am fine,thanks!")
        elif a=="bye":
            print("Me: Goodbye!")
        else:
            print("Sorry! I don't understand")
            continue
rule_based_chatbot()