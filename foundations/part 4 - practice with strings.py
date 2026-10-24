company = "Coding for all"

#allows us to print length of company, change all letters to lower and upper case
print(len(company), company.upper(), company.lower())

#changes format so that there are capital letters at right places, format as if it were a title and swaps cases of letters
print(company.capitalize(), company.title(), company.swapcase())

#cuts coding
print(company[6:])

print(company.rfind("Coding"))

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

number_1, number_2 = 8, 6
print(f"{number_1} + {number_2} = {number_1+number_2}")
print(f"{number_1} - {number_2} = {number_1-number_2}")
print(f"{number_1} * {number_2} = {number_1*number_2}")
print(f"{number_1} / {number_2} = {number_1/number_2}")
print(f"{number_1} % {number_2} = {number_1%number_2}")
print(f"{number_1} // {number_2} = {number_1//number_2}")
print(f"{number_1} ** {number_2} = {number_1**number_2}")
print(f"{number_1} - {number_2} = {number_1-number_2}")