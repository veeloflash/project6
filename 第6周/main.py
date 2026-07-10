from src.statement import detect_state
while True:
    user_input = input("Enter a question: ")
    result = detect_state(user_input)
    print(f"Detected state(s): {result}")