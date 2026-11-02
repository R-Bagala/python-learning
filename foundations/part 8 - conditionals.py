person = {'name':'Robert','start':1244,'end':1255}
house = {'House 1':[], 'House 2':[], 'House 3':[], 'House 4':[]}

# Implement your if statement so that it determins the value of a variable called what_bin
# Put your code here
what_house = 'House ?'
if person["start"] < 1245 and person["end"] < 1256:
    what_house = "House 1"
elif (person["start"] < 1245 and person["end"] < 1256) and person["name"].startswith("R"):
    what_house = "House 2"
elif 1245 < person['start'] < 1256 and person['name'][0]<'F':
    what_house = 'House 3'
else:
    what_house = 'House 4'
# Uncomment the following line to see if the person went into the correct bin
house[what_house].append(person)
print(house)

Name = input('What name are you looking for? ')
if Name == "Robert":
    print(1)
elif Name == "Thomas":
    print(2)
elif Name == "Oscar":
    print(3)
elif Name == "Jane":
    print(4)
else:
    print("Name Doesn't exist.")

phonebook = {'Robert': 3453,'Thomas': 6854,'Tom': 9812,'Robby': 1255,'Greta': 3800,'Harry': 6987}
search = input('What name are you looking for? ')
# write your code here
if search == "Robert":
    print(phonebook["Robert"])
elif search == "Thomas":
    print(phonebook["Thomas"])
elif search == "Tom":
    print(phonebook["Tom"])
elif search == "Robby":
    print(phonebook["Robby"])
elif search == "Greta":
    print(phonebook["Greta"])
else:
    print(phonebook["Harry"])
