try:
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError:
    print("Divided a number by zero.")
except ValueError:
    print("Invalid input")