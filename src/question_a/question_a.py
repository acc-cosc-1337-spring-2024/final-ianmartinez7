#write functions here, don't add input('') statements here!

#main logic here
def get_numbers():
    numbers = []
    for i in range(5):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    return numbers

def find_lowest(numbers):
    return min(numbers)

def find_highest(numbers):
    return max(numbers)

def calculate_total(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)
