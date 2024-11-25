def count_chars(my_string:str, letter_to_find:str):
    count_char = 0
    for i in range(len(my_string)):
        if my_string[i] == letter_to_find:
            count_char+=1
            print(f"la letra '{letter_to_find}' aparece en el indice {i}")
    return count_char
        

user_input = input("ingrese una cadena: ")
letter = input("ingrese la letra a buscar: ")
total_count = count_chars(user_input, letter)
print(f"la letra {letter} aparece {total_count} veces")