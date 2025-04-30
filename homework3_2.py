user_input = input("Enter the list numbers separated by a space: ")

numbers = [int(num) for num in user_input.split()] \
    if user_input else []

if len(numbers) > 1:
    numbers = [numbers[-1]] + numbers[:-1]

print("result:", numbers)