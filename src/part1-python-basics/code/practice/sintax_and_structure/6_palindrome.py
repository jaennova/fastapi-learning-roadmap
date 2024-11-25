def palindrome_indentifier(my_string: str):
    is_palindrome = False
    reversed = ""
    for i in range(len(my_string) -1, -1, -1):
        reversed+= my_string[i]
    return reversed == my_string

user_input = input("ingrese una cadena de texto: ")
palindrome = palindrome_indentifier(user_input)
print(f"La palabra '{user_input}' {'es' if palindrome else 'no es'} un palíndromo.")