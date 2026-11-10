#factorial calculator
while True:
  try:
    number = int(input("Please enter a umber to calcuate its factorial: "))
    break
  except ValueError:
    number = int(input("Incorrect input. Please enter a umber to calcuate its factorial: "))

def factorial(number):
  factorial = 1
  factorial_list = []
  if number <= 1:
    return factorial
  else:
    for i in range(number+1):
      factorial_list.append(i)
    factorial_list.pop(0)
    for j in range(len(factorial_list)):
      factorial *= factorial_list[j]
    return factorial

result = factorial(number)
print(f"{number}! = {result}")