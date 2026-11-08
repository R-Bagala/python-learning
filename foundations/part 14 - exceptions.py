from re import escape


try:
    print(10 + "5")
except:
    print("something went wrong")

def sum_of_ten_nums(*numbers):
    sum = 0
    return sum

lst = [1, 3, 4, 5, 6, 7, 8, 9, 1, 3]
print(sum_of_ten_nums(*lst))

#excercise 17

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print(nordic_countries)