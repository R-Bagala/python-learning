#prime calculator



def is_prime(number):
    divisible_count = 0
    prime_list = []
    for i in range(number):
        prime_list.append(i + 1)
    for j in range(1, (len(prime_list) + 1)):
        if number % j == 0:
            divisible_count += 1
    if number <= 1:
        return "is not a prime number"
    elif divisible_count == 2:
         return "is a prime number"
    else:
        return "is not a prime number"

while True:
    try:

        number = int(input("Please enter a number. The program will calculate if it is a prime or not. Enter 00 when : "))
        if number == 00:
            break
        print(f"{number} {is_prime(number)}")
    except ValueError:
        number = int(input("Please enter a suitable input: "))
