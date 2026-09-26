# main.py

from analyzer import analyze_password
from storage import save_result, view_history

while True:
    print("\n===== SecurePass =====")
    print("1. Analyze Password")
    print("2. View History")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        password = input("Enter password: ")

        score, risk, suggestions = analyze_password(password)

        print("\n--- Result ---")
        print("Score :", score, "/100")
        print("Risk  :", risk)

        if suggestions:
            print("\nSuggestions:")
            for tip in suggestions:
                print("-", tip)
        else:
            print("Strong password!")

        save_result(password, score, risk)

    elif choice == "2":
        print("\n--- History ---")
        print(view_history())

    elif choice == "3":
        print("Thank you for using SecurePass!")
        break

    else:
        print("Invalid choice!")
