from src.statement import detect_state

if __name__ == "__main__":
    while True:
        user_input = input("Enter a question (or type exit/quit): ")
        if user_input.lower().strip() in {"exit", "quit"}:
            print("Goodbye.")
            break
        result = detect_state(user_input)
        print(f"Detected state(s): {result}")
