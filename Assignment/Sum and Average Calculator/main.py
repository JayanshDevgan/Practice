# 95 / 100 cause forgot to add the case in which list is empty

"""

Objective:
Write a Python program that calculates the sum and average of a list of numbers.

Requirements:

Create a function calculate_sum that takes a list of numbers as input and returns the sum of these numbers.

Create a function calculate_average that takes a list of numbers as input and returns the average of these numbers.

In the main function, prompt the user to enter a list of numbers. The user should enter the numbers separated by spaces.

Call the calculate_sum function with the entered list and print the result.

Call the calculate_average function with the entered list and print the result.

Enter a list of numbers separated by spaces: 10 20 30 40 50
Sum: 150
Average: 30.0

"""

def calculate_sum_avg(L: list):
    if len(L) == 0:
        return "List is empty. Cannot calculate sum and average."

    SUM = sum(L)
    AVG = SUM / len(L)
    return f"Sum: {SUM}\nAverage: {AVG}"

if __name__ == "__main__":
    L = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    result = calculate_sum_avg(L)
    print(result)
