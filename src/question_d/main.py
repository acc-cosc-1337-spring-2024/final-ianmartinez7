#add import

from question_d import create_multiplication_table, display_multiplication_table

def main():
    while True:
        user_input = input("Do you want to display the multiplication table? (yes/no): ")
        if user_input.lower() == 'yes':
            table = create_multiplication_table()
            display_multiplication_table(table)
        elif user_input.lower() == 'no':
            print("Exiting the program.")
            break
        else:
            print("Invalid input, please type 'yes' or 'no'.")

if __name__ == '__main__':
    main()
