def conversation_program():
    print("welcom to my conversation program")
    print("I will keep asking questions until you type 'exit'.\n")

    questions = [
        "What is your name?",
        "What is your favorite show?",
        "Do you like programming?",
         "What is your favorite sport?"
    ]

    count = 0
    for i, question in enumerate(questions, 1):
        answer = input(f"{i}. {question} ").strip()
        if answer.lower() == "exit":
            break
        count += 1

    if count == 0:
        print("\nToo bad you did not want to chat! maybe next time!")
    else:
        print(f"\nThanks for chatting with me!")
        print(f"You answered {count} question{'s' if count > 1 else ''}.")

conversation_program()
