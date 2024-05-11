#add import

import question_a

def main():
    #main logic
    numbers = question_a.get_numbers()

    #all other functions here
    print(f"The lowest number in the list is {question_a.find_lowest(numbers)}")
    print(f"The highest number in the list is {question_a.find_highest(numbers)}")
    print(f"The total of the numbers in the list is {question_a.calculate_total(numbers)}")
    print(f"The average of the numbers in the list is {question_a.calculate_average(numbers)}")

if __name__ == "__main__":
    main()
