n = int(input("Enter a number: "))
try:
    print(10/n)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a valid number.")
finally:
    print("This block will always execute.")