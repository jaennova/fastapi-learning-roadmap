def reverse_string(my_string: str):
    reversed = ""
    for i in range(len(my_string)-1, -1, -1):
        reversed += my_string[i]
    return reversed

user_input = input("ingrese una cadena de texto")
reversed_string = reverse_string(user_input)
print(f"el resultado de invertir la cadena {user_input} es {reversed_string}")