import time

def natural_numbers_sum(number):
    start = time.time()
    sum = 0
    for i in range(1,number +1):
        sum+=1
    end = time.time()
    total_time = end - start
    return sum, total_time

user_number = int(input("ingrese un numero entero:"))
result, total_time = natural_numbers_sum(user_number)

print(result)
print(time)