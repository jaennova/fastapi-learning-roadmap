def calculate_factorial(number: int):
    if number == 0:
        return 1
    else:
        return number * calculate_factorial(number - 1)

user_input = int(input("ingrese un numero: "))
factorial = calculate_factorial(user_input)
print(f"el factorial de {user_input} es {factorial}")

