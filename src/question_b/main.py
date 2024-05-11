#add import


from question_b import Stock, stock_purchase_history

def main():
    # Creating stock instances
    stocks = {
        "AAPL": Stock("AAPL", "Apple Inc"),
        "CAT": Stock("CAT", "Caterpillar"),
        "EK": Stock("EK", "Eastman Kodak"),
        "GOOG": Stock("GOOG", "Google"),
        "MSFT": Stock("MSFT", "Microsoft")
    }

    # Menu system
    while True:
        print("\nMenu")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            stock_purchase_history(stocks)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
